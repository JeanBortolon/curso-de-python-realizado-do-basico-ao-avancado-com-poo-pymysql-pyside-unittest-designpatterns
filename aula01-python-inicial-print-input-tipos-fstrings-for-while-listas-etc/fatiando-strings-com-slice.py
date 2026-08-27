# Lista de Strings
nomes = ['jean', 'maria', 'joão', 'ana', 'carlos']

'''
Cria "função" que fatia do zero até o terceiro elemento
com passo de 1 em 1 pois marquei None
'''
obtem_elementos = slice(0,3,None)

'''
Cria "função" que inverte os elementos
'''
inverte = slice(None,None,-1)

# Printa a lista aplicando o fatiamento
print(nomes[obtem_elementos])
# Printa a lista aplicando o fatiamento
print(nomes[inverte])