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

def gasolina(modelo):
    for carros in modelo:
        if carros["combustivel"] == 'gasolina':
            camila = carros["modelo"]
            print(camila)
        return camila

quantidade = gasolina(data)
print("A quantidade de itens da lista é: ", quantidade)

# modelos = [vm["modelo"] for vm in informacao]
# valores = [vl["combustivel"] for vl in informacao]
# lista = {}
# lista = dict(zip(modelos, valores))
# for mod, comb in lista.items():
#     if comb == "gasolina":
#         sao = mod
#         print(mod)
#
#
#
# def veiculos_gasolina(gasolina):
#     modelos = [vm["modelo"] for vm in gasolina]
#     valores = [vl["combustivel"] for vl in gasolina]
#     lista = {}
#     lista = dict(zip(modelos, valores))
#     for mod, comb in lista.items():
#         if comb == "gasolina":
#             sao = list(mod)
#             return mod
#
#
# if __name__ == "__main__":
#
#     modelos_a_gasolina = veiculos_gasolina(informacao)
#     print("Os modelos a gasolina são: ", modelos_a_gasolina)
