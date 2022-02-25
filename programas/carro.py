
data = [
        {
            'marca': 'fiat',
            'modelo': 'uno',
            'preco': 10000,
            'combustivel': 'gasolina'
        },
        {
            'marca': 'fiat',
            'modelo': 'palio',
            'preco': 12000,
            'combustivel': 'alcool'
        },
        {
            'marca': 'fiat',
            'modelo': 'punto',
            'preco': 15000,
            'combustivel': 'flex'
        },
        {
            'marca': 'vw',
            'modelo': 'fusca',
            'preco': 11000,
            'combustivel': 'gasolina'
        },
        {
            'marca': 'vw',
            'modelo': 'gol',
            'preco': 13000,
            'combustivel': 'alcool'
        },
        {
            'marca': 'vw',
            'modelo': 'jetta',
            'preco': 25000,
            'combustivel': 'flex'
        },
        {
            'marca': 'gm',
            'modelo': 'celta',
            'preco': 8000,
            'combustivel': 'gasolina'
        },
        {
            'marca': 'gm',
            'modelo': 'astra',
            'preco': 17000,
            'combustivel': 'alcool'
        },
        {
            'marca': 'gm',
            'modelo': 'vectra',
            'preco': 22000,
            'combustivel': 'gasolina'
        },
        {
            'marca': 'ford',
            'modelo': 'fusion',
            'preco': 29000,
            'combustivel': 'flex'
        }
    ]


# 1. Quantidade de Itens
#OPÇÃO 01

def count_keys(itens):
    quantidade = 0
    for item in enumerate(itens):
        quantidade += 1
    return quantidade

# OPÇÃO 02
def quantidade_itens(itens):
    quantidade = len(itens)
    return quantidade

#OPÇÃO 03
def quant_itens(itens):
    quantidade = 0
    for item in itens:
        quantidade += 1
    return quantidade

# #2. Veículo Mais Caro
#
def veiculo_caro(carro):
    modelos = [vm["modelo"] for vm in carro]
    valores = [vl["preco"] for vl in carro]
    lista = {}
    lista = dict(zip(modelos, valores))
    caro = max(lista, key = lista.get)
    return caro

# #3. Veículo Mais barato
#
# def veiculo_barato(carro):
#     valor = "preco"
#     valores = [vl[valor] for vl in carro]
#     maior = valores
#     max_valor = max(maior)
#     return max_valor
#
# print(veiculo_caro(data))

# 4. Todos os veículos movidos a gasolina

def veiculos_gasolina(gasolina):
    g = "gasolina"
    for infos in gasolina:
        gravar = []
        gravar.append((infos['modelo'], infos['combustivel']))
        lista = dict(gravar)
        for k,v in lista.items():
            if v == g:
                lista_gasolina = k
                return lista_gasolina


# 5. Todos os veículos movidos a alcool

def veiculos_alcool(alcool):
    a = "alcool"
    for infos in alcool:
        gravar = []
        gravar.append((infos['modelo'], infos['combustivel']))
        lista = dict(gravar)
        for k,v in lista.items():
            if v == a:
                lista_alcool = k
                return lista_alcool

# 6. Todos os veículos movidos a flex

def veiculos_flex(flex):
        f = "flex"
        for infos in flex:
            gravar = []
            gravar.append((infos['modelo'], infos['combustivel']))
            lista = dict(gravar)
            for k,v in lista.items():
                if v == f:
                    lista_flex = k
                    return lista_flex

if __name__ == "__main__":
    quantidade = quantidade_itens(data)
    print(quantidade)
    veiculo_caro = veiculo_caro(data)
    print(veiculo_caro)
    # veiculo_barato = veiculo_barato(data)
    # print(veiculo_barato)
    veiculos_gasolina = veiculos_gasolina(data)
    print(veiculos_gasolina)
    veiculos_alcool = veiculos_alcool(data)
    print(veiculos_alcool)
    veiculos_flex = veiculos_flex(data)
    print(veiculos_flex)
