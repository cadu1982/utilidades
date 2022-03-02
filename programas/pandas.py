import pandas as pd


data = [{'marca': 'fiat','modelo': 'uno','preco': 10000,'combustivel': 'gasolina'},
        {'marca': 'fiat','modelo': 'palio','preco': 12000,'combustivel': 'alcool'},
        {'marca': 'fiat','modelo': 'punto','preco': 15000,'combustivel': 'flex'},
        {'marca': 'gm','modelo': 'vectra','preco': 25000,'combustivel': 'gasolina'},
        {'marca': 'gm','modelo': 'celta','preco': 11000,'combustivel': 'alcool'},
        {'marca': 'gm','modelo': 'corsa','preco': 17000,'combustivel': 'flex'}]

# Converte para dataframe
df = pd.DataFrame(data)

#Filtra coluna combustivel pelo tipo gasolina
df_result = df[df['combustivel']=='gasolina']
print(df_result)
