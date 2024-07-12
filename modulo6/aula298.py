import locale 
from datetime import datetime
import json
import string
from pathlib import Path

locale.setlocale(locale.LC_ALL, '')
CAMINHO_ARQUIVO = Path(__file__).parent / 'aula298.txt'

def converter_para_brl(numero: float | int) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl

data = datetime(2022,12,28)
dados = dict(
    nome='João',
    valor=converter_para_brl(1234),
    data=data.strftime('%d/%m/%Y'),
    empresa='T-Systems',
    telefone='+55 47 999205271'
)

#print(json.dumps(dados, indent=2))

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()
    template = string.Template(texto)
    print(template.substitute(dados))

"""
texto = '''
Prezado(a) $nome,
Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data. Caso deseje cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone.
Atenciosamente,
${empresa} 
'''

template = string.Template(texto)
print(template.substitute(dados)) #safe_substitute(dados)
"""