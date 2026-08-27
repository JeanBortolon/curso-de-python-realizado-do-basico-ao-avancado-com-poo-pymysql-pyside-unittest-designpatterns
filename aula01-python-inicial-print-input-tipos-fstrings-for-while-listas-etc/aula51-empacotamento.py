"""
Introdução ao empacotamento e desempacotamento + Tuples [ tuplas ]
"""

'''
nomes = ['Maria', 'Helena', 'Luiz']
nome1,nome2,nome3 = nomes
print(nome2)
'''
'''Sempre que for pegar valores pra colocar em variaveis
preciso garantir que tenha quantidade para receber ou seja
nome1,nome2 = ['Maria' , 'Helena']
Se eu tiver mais valor que variavel preciso criar algo
para receber o resto colocando asterisco e nome da var, exemplo:
nomes = ['Maria', 'Helena', 'Luiz']

nome1, *resto = ['Maria', 'Helena', 'Luiz']

print(nome1)


'''

''' EM PYTHON EXISTE A CONVENÇÃO DE DEIXAR UM UNDERLINE PARA VARIAVEL
QUE NÃO VOU UTILIZAR, QUE SERIA PARA O RESTO.
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)
'''