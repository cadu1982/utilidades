import requests
from imprime import imprime1

def cep_correto1(cep):
    if len(cep) != 8:
        print('CEP, inválido, deve conter 8 digitos!')
        exit()
    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    dados = request.json()
    imprime1()
    return dados

