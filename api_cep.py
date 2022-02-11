import requests
print('###########################')
print("-------CONSULTA CEP--------")
print('###########################')

cep_input = input('Digite o CEP para consulta: ')

if len(cep_input) != 8:
    print('CEP, inválido, deve conter 8 digitos!')
    exit()
request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

dados = request.json()

if 'erro' not in dados:
    print('===>CEP encontrado<====')
    print(dados['cep'])
    print(dados['logradouro'])
    print(dados['complemento'])
    print(dados['bairro'])
    print(dados['localidade'])
    print(dados['uf'])
else:
    print('CEP inválido')


