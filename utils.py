"""
Módulo de funções utilitárias para manipulação de JSON, cookies, tipos de veículo e namespaces.
"""

import json
import os
from lxml import etree

def carregar_grupos_placas(arquivo='grupos_placas.json'):
    """Carrega o JSON de grupos de placas."""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    return {}

def carregar_compras_realizadas(arquivo='compras_realizadas.json'):
    """Carrega o JSON de compras realizadas."""
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as f:
            return json.load(f)
    return {}

def salvar_compras_realizadas(compras, arquivo='compras_realizadas.json'):
    """Salva o JSON de compras realizadas."""
    with open(arquivo, 'w') as f:
        json.dump(compras, f, indent=4)

def viagem_ja_comprada(documento, arquivo='compras_realizadas.json'):
    """Verifica se a viagem já foi comprada."""
    compras_realizadas = carregar_compras_realizadas(arquivo)
    return documento in compras_realizadas

def registrar_compra_realizada(documento, arquivo='compras_realizadas.json'):
    """Registra uma compra realizada."""
    compras_realizadas = carregar_compras_realizadas(arquivo)
    compras_realizadas[documento] = True
    salvar_compras_realizadas(compras_realizadas, arquivo)

def determinar_tipo_veiculo(placa, arquivo='grupos_placas.json'):
    """Determina o tipo de veículo e eixos a partir da placa."""
    grupos_placas = carregar_grupos_placas(arquivo)
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

def remove_namespaces(tree):
    """Remove namespaces de um XML ElementTree."""
    for elem in tree.getiterator():
        elem.tag = elem.tag.split('}')[-1]
    etree.cleanup_namespaces(tree)
    return tree

def parse_cookies(cookies_str):
    """Converte string de cookies em dicionário."""
    cookies = {}
    for cookie in cookies_str.split(';'):
        if '=' in cookie:
            name, value = cookie.strip().split('=', 1)
            cookies[name] = value
    return cookies 