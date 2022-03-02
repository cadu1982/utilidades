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
    modelos_c = [vm["modelo"] for vm in carro]
    valores_c = [vl["preco"] for vl in carro]
    lista = {}
    lista = dict(zip(modelos_c, valores_c))
    caro = max(lista, key = lista.get)
    return caro

# #3. Veículo Mais barato

def veiculo_barato(carro):
    modelos = [vm["modelo"] for vm in carro]
    valores = [vl["preco"] for vl in carro]
    lista = {}
    lista = dict(zip(modelos, valores))
    for menor in sorted(lista, key = lista.get):
        carro = menor
        return carro

# 4. Todos os veículos movidos a gasolina

def filtrar_por_gasolina(carros):
    modelos_a_gasolina = []
    for carro in carros:
        if carro['combustivel'] == 'gasolina':
            modelos_a_gasolina.append(carro['modelo'])
    return modelos_a_gasolina

# 5. Todos os veículos movidos a alcool

def filtrar_por_alcool(carros):
    modelos_a_alcool = []
    for carro in carros:
        if carro['combustivel'] == 'alcool':
            modelos_a_alcool.append(carro['modelo'])
    return modelos_a_alcool


# 6. Todos os veículos movidos a flex

def filtrar_por_flex(carros):
    modelos_flex = []
    for carro in carros:
        if carro['combustivel'] == 'flex':
            modelos_flex.append(carro['modelo'])
    return modelos_flex

if __name__ == "__main__":
    quantidade = quantidade_itens(data)
    print("A quantidade de itens da lista é: ", quantidade)
    veiculo_caro = veiculo_caro(data)
    print("O veiculo de maior valor é o: ", veiculo_caro)
    veiculo_barato = veiculo_barato(data)
    print("O veiculo de menor valor é o: ", veiculo_barato)
    veiculos_gasolina = filtrar_por_gasolina(data)
    print("Os veiculos movidos a gasolina são: ", veiculos_gasolina)
    veiculos_alcool = filtrar_por_alcool(data)
    print("Os veiculos movidos a alcool são: ", veiculos_alcool)
    veiculos_flex = filtrar_por_flex(data)
    print("Os veiculos flex são: ", veiculos_flex)
