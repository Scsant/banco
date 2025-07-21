#CÓDIGO PARA AUTENTICAR O USUARIO

import requests
from lxml import etree

# URL do serviço SOAP de homologação para autenticação
url = 'https://app.viafacil.com.br/wsvp/ValePedagio' 

# Cabeçalhos SOAP
headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': 'autenticarUsuario'
}

# Criação do envelope SOAP
envelope = etree.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope',
                         nsmap={
                             'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                             'xsd': 'http://www.w3.org/2001/XMLSchema',
                             'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
                             'cgmp': 'http://cgmp.com'
                         })

# Criação do corpo da requisição
body = etree.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
autenticar_usuario = etree.SubElement(body, '{http://cgmp.com}autenticarUsuario', 
                                      attrib={'{http://schemas.xmlsoap.org/soap/envelope/}encodingStyle': 'http://schemas.xmlsoap.org/soap/encoding/'})

# Namespaces
namespaces = {
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    'xsd': 'http://www.w3.org/2001/XMLSchema'
}

# Adicionando os elementos de autenticação
codigodeacesso = etree.SubElement(autenticar_usuario, 'codigodeacesso', attrib={etree.QName(namespaces['xsi'], 'type'): 'xsd:string'})
codigodeacesso.text = '53943098000187'  # Substitua pelo código de acesso real

login = etree.SubElement(autenticar_usuario, 'login', attrib={etree.QName(namespaces['xsi'], 'type'): 'xsd:string'})
login.text = 'SLUIS'  # Substitua pelo login real

senha = etree.SubElement(autenticar_usuario, 'senha', attrib={etree.QName(namespaces['xsi'], 'type'): 'xsd:string'})
senha.text = 'Br@cell123'  # Substitua pela senha real

# Converte o envelope SOAP para string
soap_request = etree.tostring(envelope, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Faz a requisição SOAP
try:
    response = requests.post(url, data=soap_request, headers=headers)
    response.raise_for_status()  # Lança um erro para status de resposta HTTP ruim
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição SOAP: {e}")
else:
    # Verifica a resposta
    print(f"Status Code: {response.status_code}")
    print("Response Content:")
    response_content = etree.fromstring(response.content)
    print(etree.tostring(response_content, pretty_print=True).decode('utf-8'))
    
    # Extraindo os valores da resposta
    ns = {
        'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
        'ns1': 'http://cgmp.com',
        'ns2': 'http://ws.dto.model.cgmp.com',
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'xsd': 'http://www.w3.org/2001/XMLSchema'
    }

    autenticar_usuario_response = response_content.find('.//ns1:autenticarUsuarioResponse', namespaces=ns)
    if autenticar_usuario_response is not None:
        # Ajuste para encontrar sem namespace para o return
        autenticar_usuario_return = autenticar_usuario_response.find('.//autenticarUsuarioReturn')
        if autenticar_usuario_return is not None:
            sessao = autenticar_usuario_return.find('.//sessao')
            status = autenticar_usuario_return.find('.//status')

            if sessao is not None:
                sessao_text = sessao.text
                print(f"Sessao: {sessao_text}")
                # Guardar a sessão para uso futuro
                # Aqui você pode salvar a sessão em uma variável global, arquivo, banco de dados, etc.
                # Exemplo:
                # with open('sessao.txt', 'w') as f:
                #     f.write(sessao_text)
            else:
                print("Elemento 'sessao' não encontrado na resposta.")
            
            if status is not None:
                status_text = status.text
                print(f"Status: {status_text}")
            else:
                print("Elemento 'status' não encontrado na resposta.")
        else:
            print("Elemento 'autenticarUsuarioReturn' não encontrado na resposta.")
    else:
        print("Elemento 'autenticarUsuarioResponse' não encontrado na resposta.")
