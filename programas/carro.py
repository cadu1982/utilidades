
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


print(data)
for infos in data:
    gravar = []
    gravar.extend((infos['modelo'], infos['preco']))
    # lista = dict(zip(gravar))
    print(gravar)
    # max_key = max(lista, key=lista.get)
    # print(max_key)



    # valor = "preco"
    # valores = list([vl[valor] for vl in carro])
    # maior = valores
    # max_valor = max(maior)
    # return max_valor

for carro in data:
    if carro['combustivel'] in 'gasolina':
        resp = (f'{carro["modelo"]} ')
        print(resp)



# 1. Quantidade de Itens

def count_keys(itens):
    quantidade = 0
    for item in enumerate(itens):
        quantidade += 1
    return quantidade

print(count_keys(data))

def quantidade_itens(itens):
    quantidade = len(itens)
    return quantidade

print(quantidade_itens(data))

def quant_itens(itens):
    quantidade = 0
    for item in itens:
        quantidade += 1
    return quantidade

print(quant_itens(data))
#
# 2. Veículo Mais Caro

def veiculo_caro(carro):
    valor = "preco"
    valores = list([vl[valor] for vl in carro])
    maior = valores
    max_valor = max(maior)
    return max_valor

print(veiculo_caro(data))
#
# # 3. Veículo Mais barato
#
# # def veiculo_barato(carro):
# #     valor = "preco"
# #     valores = [vl[valor] for vl in carro]
# #     maior = valores
# #     max_valor = max(maior)
# #     return max_valor
# #
# # print(veiculo_caro(data))
#
# 4. Todos os veículos movidos a gasolina

def veiculos_gasolina(gasolina):
    for carro in gasolina:
        if carro['combustivel'] in 'gasolina':
            resp = (f'{carro["modelo"]} ')
            return resp

print(veiculos_gasolina(data))

# # 4. Todos os veículos movidos a alcool

def veiculos_alcool(alcool):
    for carro in alcool:
        if carro['combustivel'] in 'alcool':
            resp = (f'{carro["modelo"]} ')
            return resp

print(veiculos_alcool(data))

# 6. Todos os veículos movidos a flex

def veiculos_flex(flex):
    for carro in flex:
        if carro['combustivel'] in 'flex':
            resp = (f'{carro["modelo"]} ')
            return resp

print(veiculos_flex(data))
