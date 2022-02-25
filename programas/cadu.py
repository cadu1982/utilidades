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
for infos in data:
    gravar = []
    gravar.append((infos['modelo'], infos['preco']))
    lista = dict(gravar)
    # print(lista)
    for k,v in lista.items():
        print(k,v)
    #     if c == 0
    #         maior = menor = c
    #     else:
    #         if c
    #     v > x:
    #         x = v
    #     if  v < x




# for carro in data:
#     modelo, combustivel = data.values()
#     print(modelo, combustivel)


# mod = "modelo"
# comb = "combustivel"
# tipo = [vl[mod] for vl in data]
# tipo1 = [vl[comb] for vl in data]
# for q, a in zip(tipo, tipo1):
#     # print(q,a)
#     if a == "gasolina":
#         print(q, a)
# # resul = tipo(zip)
# # quantos = tipo.count("gasolina")
# # print(maior)
# # print(tipo, tipo1)




# valor = "preco"
# valores = [vl[valor] for vl in data]
# cadu = valores
# max_value = max(cadu)
# # max_index = cadu.index(max_value)
# print(max_value)

# print(type(valores))
# resultado = valores.split(",")
# maximo = (max(int(maior) for maior in resultado))
#
#
# max_value = max(data)
# max_index = number_list.index(max_value)
# print(max_index)







# a_key = "preco"
# values_of_key = [a_dict[a_key] for a_dict in data]
#
# print(values_of_key)



# caro = 0
# i = 0
# modelo = (data[0]["preco"])
# esse = data[i]["preco"]
# i = i + 1
#
# if (modelo > caro):
#     caro = modelo
#     modelo = caro
#     print(modelo)
#
#
# carro = (data[2]["preco"])
# print(modelo, carro)

# mod = "modelo"
# comb = "combustivel"
# tipo = [vl[mod] for vl in gasolina]
# tipo1 = [vl[comb] for vl in gasolina]
# for q, a in zip(tipo, tipo1):
#     print(q,a)
#     if a == "gasolina":
#         gasolina = q, a
#         return gasolina

# print(data[0], data[1])

# cadu = list(filter(lambda person: person['combustivel'] == 'gasolina', data))
# respo = cadu
# cadu = (respo[0]["modelo"], respo[1]["modelo"],respo[2]["modelo"],respo[3]["modelo"])
# print(cadu)
