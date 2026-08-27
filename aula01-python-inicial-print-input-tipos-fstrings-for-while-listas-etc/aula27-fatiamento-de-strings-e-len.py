"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
i: -> inicio
f: -> fim
p: -> passo
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:]) #Printa a partir do indice 4
print(variavel[4:8]) #Printa a partir do indice 4
# e para antes do indice 8, ou seja, até 7.
print(len(variavel)) #função len pega a quantidade
#de caracteres de uma variavel ou str literal
print(len(variavel[3:7])) #posso contar caracteres
# em quantidades especificas atraves dos indices
# contragem de chars da str começa de 1, mas indice 0
print(variavel[0:len(variavel):1])
"""começando de zero até o tamanho da string com 
passo de 1 em 1"""
print(variavel[0:len(variavel):4])
"""começando de zero até o tamanho da string com 
pulando caracteres de 4 em 4"""

print(variavel[::-1]) #passo invertido de trás pra
# frente, pois a str tem indice positivo e negativo