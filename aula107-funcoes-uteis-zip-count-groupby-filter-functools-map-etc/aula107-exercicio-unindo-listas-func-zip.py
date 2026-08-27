
# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

'''
# Função que retorna qual o menor tamanho entre duas listas.
def zipper(lista1,lista2):
    return min(len(lista1),len(lista2))
    
# Atribuição das listas.
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1,l2))
'''

def zipper(lista1,lista2):
    intervalo_maximo = min(len(lista1),len(lista2))
    return [ 
        (lista1[i], lista2[i]) for i in range(intervalo_maximo)
        # Parenteses para transformar em tupla
        # indice 3 obtido do tamanho minimo entre as 2 listas
        # as listas navegam indice a indice do range 3 e ret suas posições
        # posição 1 da lista 1 com a 1 da lista 2

    ]
    
# Atribuição das listas.
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1,l2))
print()

'''# O PYTHON TEM UMA FUNÇÃO QUE CHAMA ZIP QUE FAZ A MESMA COISA
QUE FIZEMOS ACIMA, PORÉM RETORNA O ITERATOR, ENTÃO CONVERTO PARA LISTA
'''

print(list(zip(l1,l2)))
print()

"""
# O PYTHON TEM O MÓDULO ITERTOOLS ONDE POSSO CHAMAR O
ZIP LONGEST QUE FAZ O ZIP PEGANDO A LISTA MAIS LONGA
TAMBÉM POSSO PREENCHER ESPAÇOS VÁZIOS COM FILL VALUE

"""

from itertools import zip_longest

print(list(zip_longest(l1,l2, fillvalue=('SEM CIDADE'))))