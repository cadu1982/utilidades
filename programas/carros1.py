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

modelos = [vm["modelo"] for vm in data]
valores = [vl["preco"] for vl in data]
lista = {}
lista = dict(zip(modelos, valores))
print(lista)
for menor in sorted(lista, key = lista.get):
    print(menor)



# for k, v in lista.items():
#     if v == "gasolina":
#         print(k,v)
# caro = max(lista, key = lista.get)
# print(caro)


# for i,j in zip(modelos, valores):
#     lista[i] = j
#     print(lista)
#     caro = max(lista, key = lista.get)
#     print(caro)


# for infos in data:
    # gravar = []
    # gravar.append((infos['modelo'], infos['preco']))
    # lista = dict(gravar)
    # print(lista)

# print(valores)
# print(valor)
    # print(valores, valor)
    # max_valor = max(maior)
    # print(maior)
    # if max_maior =



        # for i in range (len(lista)):
        #     atual = v[i]
        #     j = i - 1;
        # while (j >=0) and (atual < v[j]):
        #     v[j +1] = v[j]
        #     j = j -1
        #     v[j + 1] = atual
        #     i = 1
        # print(modelo, valor)







# gravar = dict(data[0]), (data[1])
# print(gravar)
# print(data)

# for carro in gravar:
#     modelo, combustivel = gravar.values()
#     print(modelo, combustivel)
# for carro in data:
#     modelo, combustivel = data.values_of_key()
#     print(modelo, combustivel)

# for infos in data:
#     gravar = []
#     gravar.append((infos['modelo'], infos['preco']))
#     lista = dict(gravar)
#     # print(lista)
#     lista = d.items()
#     for v in lista.items():
#         print(v[0])









#
# 2. Veículo Mais Caro

# def veiculo_caro(carro):
#     valores = list([vl[valor])
#     maior = valores
#     for vl in carro:
#         max_valor = max(maior)
#     return max_valor




# print(veiculo_caro(data))
#
# # 3. Veículo Mais barato
#
# def veiculo_barato(carro):
#     valor = "preco"
#     valores = [vl[valor] for vl in carro]
#     maior = valores
#     print(maior)
#     max_valor = max(maior)
#     return max_valor
#
# print(veiculo_barato(data))
