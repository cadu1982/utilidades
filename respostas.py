import requests

print('--ESCOLHA ENTRE PIADA OU IMAGEM--')
print('Digite sua escolha: ')
escolha = str(input())


def pega_piada():
    request = requests.get('https://api.chucknorris.io/jokes/random')
    piada = request.json()
    return piada['value']


def pega_imagem():
    request = requests.get('https://api.chucknorris.io/jokes/random')
    caminho = request.json()
    return caminho['icon_url']


if escolha == 'piada':
    print(pega_piada())
elif escolha == 'imagem':
    print(pega_imagem())
else:
    print('Voce nao fez a escolha corrta')
