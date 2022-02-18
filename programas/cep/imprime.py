
def imprime1(dados):
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


