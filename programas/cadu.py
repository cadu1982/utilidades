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
        }
    ]

mod = "modelo"
comb = "combustivel"
tipo = [vl[mod] for vl in data]
tipo1 = [vl[comb] for vl in data]
for q, a in zip(tipo, tipo1):
    # print(q,a)
    if a == "gasolina":
        print(q, a)
# resul = tipo(zip)
# quantos = tipo.count("gasolina")
# print(maior)
# print(tipo, tipo1)




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
