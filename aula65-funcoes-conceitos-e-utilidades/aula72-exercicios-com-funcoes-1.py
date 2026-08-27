# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

'''
def mult(*args):
    total = 1 # Inicia o valor com 1 para não multiplicar por zero
    for valor in args:
        total *= valor # Itera os valores dos argumentos multiplicando
    return total

myvar = mult(2,2,2)
print(myvar)
'''

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
# MINHA RESOLUÇÃO
''''
def imp_par(x):
    valor = x % 2
    if valor == 0:
        print(f'O {x} é par')
    else:
        print(f'O {x} é impar')

myvar = input('Digite um valor inteiro:')
valor = int(myvar)
imp_par(valor)
'''

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
# RESOLUÇÃO DO PROF

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)

