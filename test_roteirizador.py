from soap_client import autenticar_usuario
import requests

CNPJ = '53943098000187'
URL_RETORNO = '/vpnew/consultaNomeRotas.do'
ROTEIRIZADOR_URL = 'https://app.viafacil.com.br/vpnew/roteirizadorSTP.do'

print('--- Testando autenticação (dados fixos) ---')
sessao = autenticar_usuario()
if not sessao:
    print('Falha na autenticação. Encerrando teste.')
    exit(1)
print(f'Sessão obtida: {sessao}')

print('\n--- Teste do Roteirizador ---')
origem = input('Cidade de origem: ').strip()
destino = input('Cidade de destino: ').strip()
origem_codigo = input('Código IBGE da cidade de origem: ').strip()
destino_codigo = input('Código IBGE da cidade de destino: ').strip()

payload = {
    'sessao': sessao.strip(),
    'cnpj': CNPJ,
    'origem': origem,
    'destino': destino,
    'origemCodigo': origem_codigo,
    'destinoCodigo': destino_codigo,
    'urlRetorno': '/vpnew/consultaNomeRotas.do'
}

print(f'\nEnviando requisição para o roteirizador...')
response = requests.post(ROTEIRIZADOR_URL, data=payload)
print(f'Status Code: {response.status_code}')
print('Conteúdo da resposta:')
print(response.text)

print('\nSe a operação for bem-sucedida, você será redirecionado para a URL de retorno após o processamento.') 