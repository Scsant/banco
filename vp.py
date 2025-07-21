import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from lxml import etree
import json
import os
import time
import streamlit as st
import threading
from dotenv import load_dotenv

# Carregar o .env no início do código
load_dotenv()

# Testar se as variáveis estão carregadas
print("VALE_PEDAGIO_URL:", os.getenv('VALE_PEDAGIO_URL'))
print("VALE_PEDAGIO_URL_IMPRESSAO:", os.getenv('VALE_PEDAGIO_URL_IMPRESSAO'))
# Carregar as variáveis sensíveis
vale_pedagio_url = os.getenv('VALE_PEDAGIO_URL')
codigodeacesso_env = os.getenv('VALE_PEDAGIO_CODIGO_ACESSO')
login_env = os.getenv('VALE_PEDAGIO_LOGIN')
senha_env = os.getenv('VALE_PEDAGIO_SENHA')
vale_pedagio_url_sgf = os.getenv('VALE_PEDAGIO_URL_SGF')
vale_pedagio_url_impressao = os.getenv('VALE_PEDAGIO_URL_IMPRESSAO')

# Caminho do arquivo JSON para compras realizadas
ARQUIVO_COMPRAS = 'compras_realizadas.json'
ARQUIVO_PLACAS = 'grupos_placas.json'

# Função para carregar JSON de placas
def carregar_grupos_placas():
    if os.path.exists(ARQUIVO_PLACAS):
        with open(ARQUIVO_PLACAS, 'r') as f:
            return json.load(f)
    return {}

# Função para carregar compras realizadas
def carregar_compras_realizadas():
    if os.path.exists(ARQUIVO_COMPRAS):
        with open(ARQUIVO_COMPRAS, 'r') as f:
            return json.load(f)
    return {}

# Função para salvar compras realizadas
def salvar_compras_realizadas(compras):
    with open(ARQUIVO_COMPRAS, 'w') as f:
        json.dump(compras, f, indent=4)

# Função para verificar se a viagem já foi comprada
def viagem_ja_comprada(documento):
    compras_realizadas = carregar_compras_realizadas()
    return documento in compras_realizadas

# Função para registrar a compra realizada
def registrar_compra_realizada(documento):
    compras_realizadas = carregar_compras_realizadas()
    compras_realizadas[documento] = True
    salvar_compras_realizadas(compras_realizadas)

# Função para determinar tipo de veículo e eixos com base no JSON de placas
def determinar_tipo_veiculo(placa):
    grupos_placas = carregar_grupos_placas()
    for grupo, placas in grupos_placas.items():
        if placa in placas:
            if grupo == "Bitrem_4":
                return 'bitrem', 4, 7
            elif grupo == "Bitrem_5":
                return 'bitrem', 5, 9
            elif grupo == "Tritrem_5":
                return 'tritrem_5', 5, 9
            elif grupo == "Tritrem_6":
                return 'tritrem_6', 6, 9
    return None, None, None

# Função para remover namespaces do XML
def remove_namespaces(tree):
    for elem in tree.getiterator():
        elem.tag = elem.tag.split('}')[-1]
    etree.cleanup_namespaces(tree)
    return tree

def autenticar_usuario():
    url = 'https://app.viafacil.com.br/wsvp/ValePedagio'
    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': 'autenticarUsuario'
    }
    print("URL de autenticação:", url)  # Verifica se a URL está carregada corretamente

    # Construção do envelope SOAP
    envelope = etree.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope',
                            nsmap={
                                'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                                'xsd': 'http://www.w3.org/2001/XMLSchema',
                                'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
                                'cgmp': 'http://cgmp.com'
                            })
    body = etree.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
    autenticar_usuario = etree.SubElement(body, '{http://cgmp.com}autenticarUsuario',
                                        attrib={'{http://schemas.xmlsoap.org/soap/envelope/}encodingStyle': 'http://schemas.xmlsoap.org/soap/encoding/'})
    
    codigodeacesso = etree.SubElement(autenticar_usuario, 'codigodeacesso', attrib={etree.QName('xsi', 'type'): 'xsd:string'})
    codigodeacesso.text = codigodeacesso_env
    login = etree.SubElement(autenticar_usuario, 'login', attrib={etree.QName('xsi', 'type'): 'xsd:string'})
    login.text = login_env
    senha = etree.SubElement(autenticar_usuario, 'senha', attrib={etree.QName('xsi', 'type'): 'xsd:string'})
    senha.text = senha_env
    
    soap_request = etree.tostring(envelope, pretty_print=True, xml_declaration=True, encoding='UTF-8')
    print("Requisição SOAP de autenticação:", soap_request)

    try:
        response = requests.post(url, data=soap_request, headers=headers, timeout=30, verify=False)
        print("Status da resposta:", response.status_code)
        print("Conteúdo da resposta:", response.content)

        response.raise_for_status()
        response_content = etree.fromstring(response.content)
        response_content = remove_namespaces(response_content)

        autenticar_usuario_return = response_content.find('.//autenticarUsuarioReturn')
        if autenticar_usuario_return is not None:
            sessao_element = autenticar_usuario_return.find('.//sessao')
            if sessao_element is not None:
                print("Sessão autenticada com sucesso:", sessao_element.text)
                return sessao_element.text
        print("Autenticação falhou, sessão não encontrada.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição SOAP: {e}")
        return None

def comprar_viagem(sessao, rota, placa, n_eixos, inicio_vigencia, fim_vigencia):
    url = vale_pedagio_url
    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': 'comprarViagem'
    }
    print(f"Iniciando compra: Sessão={sessao}, Rota={rota}, Placa={placa}, Eixos={n_eixos}")

    envelope = etree.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope',
                            nsmap={
                                'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                                'xsd': 'http://www.w3.org/2001/XMLSchema',
                                'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
                                'cgmp': 'http://cgmp.com'
                            })
    body = etree.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
    comprar_viagem = etree.SubElement(body, '{http://cgmp.com}comprarViagem',
                                    attrib={'{http://schemas.xmlsoap.org/soap/envelope/}encodingStyle': 'http://schemas.xmlsoap.org/soap/encoding/'})
    etree.SubElement(comprar_viagem, 'sessao', attrib={etree.QName('xsi', 'type'): 'xsd:long'}).text = sessao
    etree.SubElement(comprar_viagem, 'rota', attrib={etree.QName('xsi', 'type'): 'xsd:string'}).text = rota
    etree.SubElement(comprar_viagem, 'placa', attrib={etree.QName('xsi', 'type'): 'xsd:string'}).text = placa
    etree.SubElement(comprar_viagem, 'nEixos', attrib={etree.QName('xsi', 'type'): 'xsd:int'}).text = str(n_eixos)
    etree.SubElement(comprar_viagem, 'inicioVigencia', attrib={etree.QName('xsi', 'type'): 'xsd:date'}).text = inicio_vigencia
    etree.SubElement(comprar_viagem, 'fimVigencia', attrib={etree.QName('xsi', 'type'): 'xsd:date'}).text = fim_vigencia

    soap_request = etree.tostring(envelope, pretty_print=True, xml_declaration=True, encoding='UTF-8')
    print("Requisição SOAP de compra:", soap_request)

    try:
        response = requests.post(url, data=soap_request, headers=headers, timeout=30)
        print("Status da resposta de compra:", response.status_code)
        print("Conteúdo da resposta de compra:", response.content)

        response.raise_for_status()
        root = etree.fromstring(response.content)
        root = remove_namespaces(root)

        numero = None
        status = None
        for element in root.iter():
            if element.tag.endswith('numero'):
                numero = element.text
            if element.tag.endswith('status'):
                status = element.text

        if status == '0':
            print(f"Compra realizada com sucesso. Número da viagem: {numero}")
            return numero
        else:
            print(f"Erro na compra. Código de status: {status}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição SOAP de compra: {e}")
        return None




# Função para imprimir recibo
def imprimir_recibo(sessao, numero_viagem, imprimir_observacoes):
    url_impressao = vale_pedagio_url_impressao
    payload = {
        'sessao': sessao,
        'viagem': numero_viagem,
        'imprimirObservacoes': str(imprimir_observacoes).lower()
    }

    try:
        response = requests.post(url_impressao, data=payload, timeout=30, verify=False)
        response.raise_for_status()
        st.write(f"Recibo da viagem {numero_viagem} foi impresso com sucesso.")
    except requests.exceptions.RequestException as e:
        st.write(f"Erro ao imprimir o recibo para a viagem {numero_viagem}: {e}")

# Função para processar viagem
def processar_viagem(documento, projeto, placa, eixos_ida, eixos_volta):
    st.write("Iniciando o processamento da viagem...")
    st.write(f"Documento: {documento}, Projeto: {projeto}, Placa: {placa}, Eixos Ida: {eixos_ida}, Eixos Volta: {eixos_volta}")

    sessao = autenticar_usuario()
    if not sessao:
        st.write("Erro na autenticação.")
        return

    inicio_vigencia = datetime.today().strftime('%Y-%m-%d')
    fim_vigencia = (datetime.today() + timedelta(days=5)).strftime('%Y-%m-%d')

    rota_ida = f"FAZ {projeto} - IDA"
    rota_volta = f"FAZ {projeto} - VOLTA"

    st.write(f"Rota de ida: {rota_ida}, Rota de volta: {rota_volta}")
    st.write(f"Período de vigência: {inicio_vigencia} a {fim_vigencia}")

    numero_viagem_ida = comprar_viagem(sessao, rota_ida, placa, eixos_ida, inicio_vigencia, fim_vigencia)
    if numero_viagem_ida:
        st.write(f"Viagem de ida registrada com sucesso. Número da viagem: {numero_viagem_ida}")
        imprimir_recibo(sessao, numero_viagem_ida, True)  # Ou False, conforme necessário

    else:
        st.write("Falha ao registrar a viagem de ida.")

    numero_viagem_volta = comprar_viagem(sessao, rota_volta, placa, eixos_volta, inicio_vigencia, fim_vigencia)
    if numero_viagem_volta:
        st.write(f"Viagem de volta registrada com sucesso. Número da viagem: {numero_viagem_volta}")
        imprimir_recibo(sessao, numero_viagem_volta, True)  # Ou False

    else:
        st.write("Falha ao registrar a viagem de volta.")
# Função para converter cookies string para dicionário
def parse_cookies(cookies_str):
    cookies = {}
    for cookie in cookies_str.split(';'):
        name, value = cookie.strip().split('=', 1)
        cookies[name] = value
    return cookies

# Função para carregar compras realizadas do arquivo JSON
def carregar_compras_realizadas():
    if os.path.exists(ARQUIVO_COMPRAS):
        with open(ARQUIVO_COMPRAS, 'r') as f:
            return json.load(f)
    return {}

# Função para salvar compras realizadas no arquivo JSON
def salvar_compras_realizadas(compras):
    with open(ARQUIVO_COMPRAS, 'w') as f:
        json.dump(compras, f, indent=4)

# Função para verificar se a viagem já foi comprada com base no número do documento
def viagem_ja_comprada(documento):
    compras_realizadas = carregar_compras_realizadas()
    return documento in compras_realizadas

# Função para registrar a compra realizada
def registrar_compra_realizada(documento):
    compras_realizadas = carregar_compras_realizadas()
    compras_realizadas[documento] = True  # Marca o documento como já processado
    salvar_compras_realizadas(compras_realizadas)
vale_pedagio_url_sgf = 'https://sgf-sp.bracell.com/sgf/Modulos/Transporte/TraOrdemTransporteRodoviarioFrm.aspx?cdprocesso=4&cdfuncao=4824'



# Função para capturar as informações usando os cookies fornecidos
def capturar_informacoes(cookies):
    url =  'https://sgf-sp.bracell.com/sgf/Modulos/Transporte/TraOrdemTransporteRodoviarioFrm.aspx?cdprocesso=4&cdfuncao=4824'
    st.write("Passei por aqui")
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6",
        "Connection": "keep-alive",
        "Referer": 'strict-origin',
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    st.write("Passei por aqui")
    # Fazendo a requisição GET com os cookies
    response = requests.get(url, headers=headers, cookies=cookies, timeout=30)
    st.write("Passei por aqui")
    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        st.write("Requisição bem-sucedida!")
        soup = BeautifulSoup(response.text, 'html.parser')
        st.write("Passei por aqui")
        # Loop para capturar informações de várias linhas (ctl03 a ctl12)
        for i in range(3, 10):  # ctl03 até ctl12
            try:
                fornecedor = soup.find('span', id=f"ctl48_ctl01_ctl{i:02}_CdFornecedorEquipamentoDESC")
                projeto = soup.find('span', id=f"ctl48_ctl01_ctl{i:02}_CdProjetoDESC")
                documento = soup.find('span', id=f"ctl48_ctl01_ctl{i:02}_CdDocumentoDESC")
                equipamento = soup.find('span', id=f"ctl48_ctl01_ctl{i:02}_CdEquipamentoDESC")
                situacao = soup.find('span', id=f"ctl48_ctl01_ctl{i:02}_TipSituacaoDESC")

                # Verificar se todos os elementos foram encontrados
                if not all([fornecedor, projeto, documento, equipamento, situacao]):
                    st.write(f"Linha {i-2}: Informações incompletas, alguns elementos não foram encontrados.")
                    st.write("-" * 50)
                    continue

                fornecedor = fornecedor.text
                projeto = projeto.text
                documento = documento.text
                equipamento = equipamento.text
                situacao = situacao.text

                # Lógica para evitar projetos ignorados
                if projeto in ["SÃO MANOEL GLEBA A - CPG", "SANTO ANTÔNIO", "NOSSA SENHORA APARECIDA XV"]:
                    st.write(f"Linha {i-2}: Projeto '{projeto}' ignorado.")
                    continue

                # Verificação de compra repetida
                if viagem_ja_comprada(documento):
                    st.write(f"Linha {i-2}: Viagem com documento {documento} e placa {equipamento} já foi comprada anteriormente. Ignorando.")
                    continue

                # Determinar tipo de veículo com base no JSON
                tipo_conjunto, eixos_ida, eixos_volta = determinar_tipo_veiculo(equipamento)
                if not tipo_conjunto:
                    st.write(f"Linha {i-2}: Tipo de veículo não reconhecido para a placa {equipamento}.")
                    continue

                # Verificação para circulação
                if situacao == "Circulacao":
                    st.write(f"Linha {i-2}: Preencher Vale-Pedágio")
                    st.write("Fornecedor:", fornecedor)
                    st.write("Projeto:", projeto)
                    st.write("Documento:", documento)
                    st.write("Equipamento:", equipamento)
                    st.write("Tipo de Conjunto:", tipo_conjunto)
                    st.write("Situação:", situacao)

                    # Processar a viagem
                    processar_viagem(documento, projeto, equipamento, eixos_ida, eixos_volta)

                    # Registrar a compra para evitar repetição futura
                    registrar_compra_realizada(documento)
                    st.write("-" * 50)

                elif situacao == "Gerada":
                    st.write(f"Linha {i-2}: Situação GERADA, tentar novamente na próxima iteração.")
                    st.write("-" * 50)
                
                elif situacao == "Finalizada":
                    st.write(f"Linha {i-2}: Situação FINALIZADA, descartando este caminhão.")
                    st.write("-" * 50)

            except AttributeError as e:
                st.write(f"Linha {i-2}: Erro ao capturar informações: {e}")
                st.write("-" * 50)
    else:
        st.write(f"Erro ao acessar a página: {response.status_code}")

    st.write("Passei por aqui")


# Função para executar o loop de compras
def executar_em_loop():
    global loop_compras_ativo
    while loop_compras_ativo:
        st.write("Iniciando processo de compra em loop...")
        capturar_informacoes(cookies)  # Substitua os cookies por reais
        st.write("Processo concluído. Aguardando 2 minutos antes da próxima execução.")
        time.sleep(120)  # Aguarda 2 minutos

def iniciar_loop():
    global loop_compras_ativo
    loop_compras_ativo = True
    threading.Thread(target=executar_em_loop).start()

def parar_loop():
    global loop_compras_ativo
    loop_compras_ativo = False
# Interface Streamlit
st.title("Sistema de Vale Pedágio - Inserir Cookies")

# Caixa de texto para inserir os cookies
cookies_input = st.text_area("Insira os valores atualizados dos cookies:")

# Estado do botão para começar e parar o processo
processar = st.button("Processar Viagem")
parar = st.button("Parar Execução")

# Verifica se o botão "Processar Viagem" foi pressionado
if processar:
    if cookies_input:
        # Converte a string de cookies para dicionário
        cookies = parse_cookies(cookies_input)
        
        # Captura as informações usando os cookies inseridos
        while True:
            capturar_informacoes(cookies)  # Executa a função principal do seu script
            time.sleep(120) 
    else:
        st.warning("Por favor, insira os cookies antes de processar a viagem.")
# Loop infinito para rodar o script a cada 5 minutos
