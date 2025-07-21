from soap_client import autenticar_usuario, comprar_viagem, imprimir_recibo
from datetime import datetime, timedelta

print('--- Testando autenticação (dados fixos) ---')
sessao = autenticar_usuario()
if not sessao:
    print('Falha na autenticação. Encerrando teste.')
    exit(1)

print(f'Sessão obtida: {sessao}')

# Dados de entrada mínimos
base_rota = input('Base da rota (ex: FAZ AMERICANA): ').strip()
placa = input('Placa: ').strip().upper()
n_eixos_ida = int(input('Número de eixos na IDA: '))
n_eixos_volta = 9  # Volta sempre 9 eixos

# Datas automáticas
hoje = datetime.today()
inicio_vigencia = hoje.strftime('%Y-%m-%d')
fim_vigencia = (hoje + timedelta(days=5)).strftime('%Y-%m-%d')

# Rotas ida e volta
rota_ida = f'{base_rota} - IDA'
rota_volta = f'{base_rota} - VOLTA'

# Parâmetros comuns
itemFin1 = ''
itemFin2 = ''
itemFin3 = ''

print(f'Comprando viagem de IDA: {rota_ida}')
numero_viagem_ida = comprar_viagem(rota_ida, placa, n_eixos_ida, inicio_vigencia, fim_vigencia, itemFin1, itemFin2, itemFin3, sessao.strip())
if numero_viagem_ida:
    print(f'Número da viagem de ida: {numero_viagem_ida}')
    imprimir_obs = input('Imprimir observações na IDA? (s/n): ').strip().lower() == 's'
    imprimir_recibo(sessao.strip(), numero_viagem_ida, imprimir_obs)
else:
    print('Falha na compra da viagem de ida.')

print(f'\nComprando viagem de VOLTA: {rota_volta} (9 eixos)')
numero_viagem_volta = comprar_viagem(rota_volta, placa, n_eixos_volta, inicio_vigencia, fim_vigencia, itemFin1, itemFin2, itemFin3, sessao.strip())
if numero_viagem_volta:
    print(f'Número da viagem de volta: {numero_viagem_volta}')
    imprimir_obs = input('Imprimir observações na VOLTA? (s/n): ').strip().lower() == 's'
    imprimir_recibo(sessao.strip(), numero_viagem_volta, imprimir_obs)
else:
    print('Falha na compra da viagem de volta.') 