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

a_key = "preco"
values_of_key = [a_dict[a_key] for a_dict in data]

print(values_of_key)



caro = 0
i = 0
modelo = (data[0]["preco"])
esse = data[i]["preco"]
i = i + 1

if (modelo > caro):
    caro = modelo
    modelo = caro
    print(modelo)



carro = (data[2]["preco"])
print(modelo, carro)