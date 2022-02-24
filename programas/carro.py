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

print(data[0], data[1])
datq = data.update()



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

# 2. Veículo Mais Caro

def veiculo_caro(carro):
    valor = "preco"
    valores = [vl[valor] for vl in carro]
    maior = valores
    max_valor = max(maior)
    return max_valor

print(veiculo_caro(data))

# 3. Veículo Mais barato

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
    mod = "modelo"
    comb = "combustivel"
    tipo = [vl[mod] for vl in gasolina]
    tipo1 = [vl[comb] for vl in gasolina]
    for q, a in zip(tipo, tipo1):
        print(q,a)
        if a == "gasolina":
            gasolina = q, a
            return gasolina

print(veiculos_gasolina(data))

#     res = "combustivel"
#     tipo = [vl[res] for vl in gasolina]
#     maior = tipo
#     mod_gasolina = maior.count("gasolina")
#     return mod_gasolina
#
# print(veiculos_gasolina(data))
