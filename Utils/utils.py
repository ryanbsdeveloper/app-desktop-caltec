import webbrowser
import os
from datetime import datetime
import re

def open_link(url):
    webbrowser.open(url)

def name_locauser():
    return os.getlogin()

def validador(entrada):
    cpf = re.sub(r'[^0-9]', '', entrada)

    if not len(cpf) == 11:
        return None

    soma = 0
    for pos, c in enumerate(range(10, 1, -1)):
        soma += int(cpf[pos]) * c

    modulo1 = 11 - (soma % 11)
    novo_cpf = cpf[:-2]

    if modulo1 > 9:
        novo_cpf += '0'
    else:
        novo_cpf += f'{modulo1}'

    soma_2 = 0
    for pos, c in enumerate(range(11, 1, -1)):
        soma_2 += int(cpf[pos]) * c

    modulo2 = 11 - (soma_2 % 11)

    if modulo2 > 9:
        novo_cpf += '0'
    else:
        novo_cpf += f'{modulo2}'

    if novo_cpf == cpf:
        return True
    else:
        return False



