# AUTENTICAÇÃO SOAP - VALE PEDÁGIO (API GATEWAY)
import requests
from lxml import etree

# ====== CONFIGURAÇÕES ======
URL = 'https://apphom.viafacil.com.br/wsvp/ValePedagio'  # Homologação
# URL = 'https://app.viafacil.com.br/wsvp/ValePedagio'  # Produção

CODIGO_ACESSO = '53943098000187'  # Substitua pelo seu código de acesso
LOGIN = 'ADMINISTRADOR'           # Substitua pelo seu login
SENHA = 'grupostp'                # Substitua pela sua senha

# ====== MONTAGEM DO ENVELOPE SOAP ======
NS_SOAPENV = 'http://schemas.xmlsoap.org/soap/envelope/'
NS_CGMP = 'http://cgmp.com'
NS_XSI = 'http://www.w3.org/2001/XMLSchema-instance'
NS_XSD = 'http://www.w3.org/2001/XMLSchema'

headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': 'autenticarUsuario'
}

envelope = etree.Element(f'{{{NS_SOAPENV}}}Envelope', nsmap={
    'xsi': NS_XSI,
    'xsd': NS_XSD,
    'soapenv': NS_SOAPENV,
    'cgmp': NS_CGMP
})
body = etree.SubElement(envelope, f'{{{NS_SOAPENV}}}Body')
auth = etree.SubElement(body, f'{{{NS_CGMP}}}autenticarUsuario', attrib={
    f'{{{NS_SOAPENV}}}encodingStyle': 'http://schemas.xmlsoap.org/soap/encoding/'
})

etree.SubElement(auth, 'codigodeacesso', attrib={etree.QName(NS_XSI, 'type'): 'xsd:string'}).text = CODIGO_ACESSO
etree.SubElement(auth, 'login', attrib={etree.QName(NS_XSI, 'type'): 'xsd:string'}).text = LOGIN
etree.SubElement(auth, 'senha', attrib={etree.QName(NS_XSI, 'type'): 'xsd:string'}).text = SENHA

soap_request = etree.tostring(envelope, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# ====== ENVIO E RESPOSTA ======
try:
    response = requests.post(URL, data=soap_request, headers=headers)
    response.raise_for_status()
    print(f"Status Code: {response.status_code}")
    print("Response Content:")
    print(response.content.decode('utf-8'))

    # Parse da resposta
    response_xml = etree.fromstring(response.content)
    ns = {
        'soapenv': NS_SOAPENV,
        'ns1': NS_CGMP,
        'ns2': 'http://ws.dto.model.cgmp.com',
        'xsi': NS_XSI,
        'xsd': NS_XSD
    }
    auth_response = response_xml.find('.//ns1:autenticarUsuarioResponse', namespaces=ns)
    if auth_response is not None:
        auth_return = auth_response.find('.//{http://cgmp.com}autenticarUsuarioReturn')
        if auth_return is None:
            auth_return = auth_response.find('.//autenticarUsuarioReturn')
        if auth_return is not None:
            sessao = auth_return.find('.//{http://ws.dto.model.cgmp.com}sessao')
            if sessao is None:
                sessao = auth_return.find('.//sessao')
            status = auth_return.find('.//{http://ws.dto.model.cgmp.com}status')
            if status is None:
                status = auth_return.find('.//status')
            if sessao is not None:
                print(f"Sessão: {sessao.text}")
            else:
                print("Elemento 'sessao' não encontrado na resposta.")
            if status is not None:
                status_text = status.text
                print(f"Status: {status_text}")
                status_messages = {
                    '0': "Sucesso",
                    '1': "CNPJ, login ou senha inválidos",
                    '3': "Sessão expirada ou inválida",
                    '4': "Veículo não disponível",
                    '5': "Placa inválida",
                    '7': "Veículo com múltiplos Tags",
                    '8': "Viagem não encontrada",
                    '9': "Usuário sem permissão a este serviço"
                }
                print(f"Status: {status_text} - {status_messages.get(status_text, 'Código de status desconhecido')}")
            else:
                print("Elemento 'status' não encontrado na resposta.")
        else:
            print("Elemento 'autenticarUsuarioReturn' não encontrado na resposta.")
    else:
        print("Elemento 'autenticarUsuarioResponse' não encontrado na resposta.")
except requests.exceptions.RequestException as e:
    print(f"Erro na requisição SOAP: {e}") 