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


# print(data)
# for infos in data:
#     gravar = []
#     gravar.append((infos['modelo'], infos['combustivel']))
#     lista = dict(gravar)
#     x = "gasolina"
#     for k,v in lista.items():
#         if v == x:
#             print(f'{k}')

# for infos in data:
#     gravar = []
#     gravar.append((infos['modelo'], infos['combustivel']))
#     lista = dict(gravar)
#     for k,v in lista.items():
#         if k, v == "gasolina"
#         print(f' {k}:{v}')
    # return max_valor

# for carro in data:
#     if carro['combustivel'] in 'gasolina':
#         resp = (f'{carro["modelo"]} ')
#         print(resp)



#
# 2. Veículo Mais Caro

# def veiculo_caro(carro):
#     valor = "preco"
#     valores = list([vl[valor] for vl in carro])
#     maior = valores
#     max_valor = max(maior)
#     return max_valor
#
# print(veiculo_caro(data))
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
    g = "gasolina"
    for infos in gasolina:
        gravar = []
        gravar.append((infos['modelo'], infos['combustivel']))
        lista = dict(gravar)
        for k,v in lista.items():
            if v == g:
                lista_gasolina = k

print(veiculos_gasolina(data))

# 4. Todos os veículos movidos a alcool

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

print(veiculos_alcool(data))

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


print(veiculos_flex(data))


#____name____ == "____main____"
