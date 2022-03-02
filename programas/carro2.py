carros = [
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


def filtrar_por_gasolina(carros):
    modelos_a_gasolina = []
    for carro in carros:
        if carro['combustivel'] == 'gasolina':
            modelos_a_gasolina.append(carro['modelo'])
    return modelos_a_gasolina

modelos_a_gasolina = filtrar_por_gasolina(carros)
print(modelos_a_gasolina)




# def filtrar_por_gasolina(data):
#     modelos_a_gasolina = []
#     for carro in data:
#         if carro['combustivel'] == 'gasolina':
#             modelos_a_gasolina.append(carro['modelo'])
#             return modelos_a_gasolina
#
# modelos_a_gasolina = filtrar_por_gasolina(data)
# print(modelos_a_gasolina)
#
# # for carros in data:
#     if carros["combustivel"] == 'gasolina':
#     mod_carros = carros["modelo"]
#     print(mod_carros)
#
# def gasolina(modelo):
#     comb = "gasolina"
#     for i in range(0, len(modelo)):
#         gaso = modelo[i]
#         if comb == gaso["combustivel"]:
#             modelos = gaso["modelos"]
#             print(modelos)
#
# quantidade = gasolina(data)
# print("A quantidade de itens da lista é: ", quantidade)




    # for carro in modelo:
    #     mod = carro["modelo"]
    #     comb = carro["combustivel"]
    #     print(mod, comb)





        # if carro["combustivel"] == "gasolina":
        #     modelo = carro["modelo"]
        #     print(modelo)
        # return modelo



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
