
msg = 'camila'

def imprime_msg():
    msg = 1
    # print('carlos ponce')
    print(msg)

# imprime_msg()
print(msg)

def imprime_soma(x, y):
    print(x + y)

imprime_soma(2, 2)
imprime_soma('2','3')

def incremento_argumento(x):
    x = x + 1
    print(x)

a = 1
incremento_argumento(a)
print(a) 

def duplica_ultimo(lista):
    lista.append(lista[-1])
    print(lista)

# lista = numeros
numeros = [1,2,3,4]
duplica_ultimo(numeros)
print(numeros)


def mensagem():
    return "Mais uma função"

x = mensagem()
print(x, len(x))

def soma_e_subtração(x, y):
    return (x + 5, x - y)

soma, subtração = soma_e_subtração(4, 1)
print(soma, subtração)


def soma(x, y):
    z = x + y
    return z

def subtração(x, y):
    z = (x - y)
    return z
    
resposta1 = soma(2, 3)
resposta2 = subtração(2, 3)
print(resposta1, resposta2)

