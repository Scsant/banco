"""
Módulo para centralizar chamadas SOAP ao serviço de vale-pedágio.
"""

import requests
from lxml import etree

def autenticar_usuario(*args, **kwargs):
    """Autentica o usuário no serviço SOAP usando valores fixos de cnpj, login e senha."""
    cnpj = '53943098000187'
    login = 'ADMINISTRADOR'
    senha = 'grupostp'
    url = 'https://apphom.viafacil.com.br/wsvp/ValePedagio'
    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': ''
    }
    envelope = etree.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope',
                             nsmap={
                                 'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
                                 'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                                 'xsd': 'http://www.w3.org/2001/XMLSchema',
                                 'cgmp': 'http://cgmp.com'
                             })
    header = etree.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Header')
    body = etree.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
    autenticar_usuario = etree.SubElement(
        body,
        '{http://cgmp.com}autenticarUsuario',
        attrib={
            '{http://schemas.xmlsoap.org/soap/envelope/}encodingStyle': 'http://schemas.xmlsoap.org/soap/encoding/'
        }
    )
    etree.SubElement(autenticar_usuario, 'cnpj', attrib={etree.QName('http://www.w3.org/2001/XMLSchema-instance', 'type'): 'xsd:string'}).text = cnpj
    etree.SubElement(autenticar_usuario, 'login', attrib={etree.QName('http://www.w3.org/2001/XMLSchema-instance', 'type'): 'xsd:string'}).text = login
    etree.SubElement(autenticar_usuario, 'senha', attrib={etree.QName('http://www.w3.org/2001/XMLSchema-instance', 'type'): 'xsd:string'}).text = senha
    soap_request = etree.tostring(envelope, pretty_print=True, xml_declaration=True, encoding='UTF-8')
    print('--- SOAP Request XML (autenticar_usuario) ---')
    print(soap_request.decode())
    print('---------------------------------------------')
    try:
        response = requests.post(url, data=soap_request, headers=headers)
        print(f"Status Code: {response.status_code}")
        response.raise_for_status()
        response_content = etree.fromstring(response.content)
        ns = {
            'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
            'ns1': 'http://cgmp.com',
            'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
            'xsd': 'http://www.w3.org/2001/XMLSchema'
        }
        autenticar_usuario_response = response_content.find('.//ns1:autenticarUsuarioResponse', namespaces=ns)
        if autenticar_usuario_response is not None:
            autenticar_usuario_return = autenticar_usuario_response.find('.//autenticarUsuarioReturn')
            if autenticar_usuario_return is not None:
                sessao = autenticar_usuario_return.find('.//sessao')
                status = autenticar_usuario_return.find('.//status')
                if sessao is not None:
                    print(f"Sessao: {sessao.text}")
                    return sessao.text
                else:
                    print("Elemento 'sessao' não encontrado na resposta.")
            else:
                print("Elemento 'autenticarUsuarioReturn' não encontrado na resposta.")
        else:
            print("Elemento 'autenticarUsuarioResponse' não encontrado na resposta.")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição SOAP: {e}")
    return None

def comprar_viagem(rota, placa, n_eixos, inicio_vigencia, fim_vigencia, itemFin1, itemFin2, itemFin3, sessao):
    """Realiza a compra do vale-pedágio via SOAP, conforme o WSDL (ordem e campos corretos)."""
    url = 'https://apphom.viafacil.com.br/wsvp/ValePedagio'
    headers = {
        'Content-Type': 'text/xml; charset=utf-8',
        'SOAPAction': ''
    }
    envelope = etree.Element('{http://schemas.xmlsoap.org/soap/envelope/}Envelope',
                             nsmap={
                                 'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
                                 'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                                 'xsd': 'http://www.w3.org/2001/XMLSchema',
                                 'cgmp': 'http://cgmp.com'
                             })
    header = etree.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Header')
    body = etree.SubElement(envelope, '{http://schemas.xmlsoap.org/soap/envelope/}Body')
    comprar_viagem = etree.SubElement(
        body,
        '{http://cgmp.com}comprarViagem',
        attrib={
            '{http://schemas.xmlsoap.org/soap/envelope/}encodingStyle': 'http://schemas.xmlsoap.org/soap/encoding/'
        }
    )
    etree.SubElement(comprar_viagem, 'rota', attrib={etree.QName('http://www.w3.org/2001/XMLSchema-instance', 'type'): 'xsd:string'}).text = rota
    etree.SubElement(comprar_viagem, 'placa', attrib={etree.QName('http://www.w3.org/2001/XMLSchema-instance', 'type'): 'xsd:string'}).text = placa
    etree.SubElement(comprar_viagem, 'nEixos', attrib={etree.QName('http://www.w3.org/2001/XMLSchema-instance', 'type'): 'xsd:int'}).text = str(n_eixos)
    etree.SubElement(comprar_viagem, 'inicioVigencia', attrib={etree.QName('http://www.w3.org/2001/XMLSchema-instance', 'type'): 'xsd:date'}).text = inicio_vigencia
    etree.SubElement(comprar_viagem, 'fimVigencia', attrib={etree.QName('http://www.w3.org/2001/XMLSchema-instance', 'type'): 'xsd:date'}).text = fim_vigencia
    etree.SubElement(comprar_viagem, 'itemFin1', attrib={etree.QName('http://www.w3.org/2001/XMLSchema-instance', 'type'): 'xsd:string'}).text = itemFin1 or ''
    etree.SubElement(comprar_viagem, 'itemFin2', attrib={etree.QName('http://www.w3.org/2001/XMLSchema-instance', 'type'): 'xsd:string'}).text = itemFin2 or ''
    etree.SubElement(comprar_viagem, 'itemFin3', attrib={etree.QName('http://www.w3.org/2001/XMLSchema-instance', 'type'): 'xsd:string'}).text = itemFin3 or ''
    etree.SubElement(comprar_viagem, 'sessao', attrib={etree.QName('http://www.w3.org/2001/XMLSchema-instance', 'type'): 'xsd:long'}).text = str(sessao)
    soap_request = etree.tostring(envelope, pretty_print=True, xml_declaration=True, encoding='UTF-8')
    print('--- SOAP Request XML (comprar_viagem) ---')
    print(soap_request.decode())
    print('-----------------------------------------')
    try:
        response = requests.post(url, data=soap_request, headers=headers)
        print(f"Status Code: {response.status_code}")
        response.raise_for_status()
        response_content = etree.fromstring(response.content)
        ns = {
            'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
            'ns1': 'http://cgmp.com',
            'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
            'xsd': 'http://www.w3.org/2001/XMLSchema'
        }
        comprar_viagem_response = response_content.find('.//ns1:comprarViagemResponse', namespaces=ns)
        if comprar_viagem_response is not None:
            comprar_viagem_return = comprar_viagem_response.find('.//comprarViagemReturn')
            if comprar_viagem_return is not None:
                numero = comprar_viagem_return.find('.//numero')
                status = comprar_viagem_return.find('.//status')
                if status is not None and status.text == '0':
                    print(f"Compra realizada com sucesso. Número da viagem: {numero.text if numero is not None else 'N/A'}")
                    return numero.text if numero is not None else None
                else:
                    print(f"Erro na compra. Código de status: {status.text if status is not None else 'N/A'}")
            else:
                print("Elemento 'comprarViagemReturn' não encontrado na resposta.")
        else:
            print("Elemento 'comprarViagemResponse' não encontrado na resposta.")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição SOAP de compra: {e}")
    return None

def imprimir_recibo(sessao, numero_viagem, imprimir_observacoes):
    """Solicita a impressão do recibo da viagem via HTTP POST para o endpoint correto."""
    url_impressao = 'https://app.viafacil.com.br/vpnew/imprimirValePedagioSTP.do'
    payload = {
        'sessao': sessao,
        'viagem': numero_viagem,
        'imprimirObservacoes': 'true' if imprimir_observacoes else 'false'
    }
    print(f"Solicitando impressão do recibo para a viagem {numero_viagem}...")
    print(f"POST {url_impressao} | payload: {payload}")
    try:
        response = requests.post(url_impressao, data=payload)
        print(f"Status Code: {response.status_code}")
        response.raise_for_status()
        print(f"Recibo da viagem {numero_viagem} foi impresso com sucesso.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Erro ao imprimir o recibo para a viagem {numero_viagem}: {e}")
        return False 