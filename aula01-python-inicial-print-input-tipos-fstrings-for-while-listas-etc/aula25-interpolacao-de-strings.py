'''Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)'''

nome = 'Luiz'
preco = 1000.95897643
variavel = 'O senhor %s comprou um jogo que custa %.2f reais' % (nome,preco)

print(variavel)

'''Interpolação é  basicamente como trabalha-
vamos em lua ou C para printar uma frase
onde temos que colocar no lugar da variável
o %TipoDaVarial e depois de forma ordenada
dentro de um parenteses vamos passando os
argumentos, em python escrevemos a frase
com o tipo e a formatação desejada e fechamos
a string, depois de fechar a string inserimos
o símbolo % e abrimos e fechamos parenteses
com os argumentos na ordem.'''

valor = 10
print('O hexadecimal do numero %d é: %x' % (valor,10))
# nos argumentos eu posso passar o valor em var
# também posso passar o valor literal
# na frase o hexa do numero 10 é 10 em hexa %x [A]
# hexadecimal é estranho com apenas 1 digito
# normalmente são 16 ou 32 bits então podemos
# complementar com zeros na frente com a sintaxe
# %04x -> 4 vezes o 0 na frente do hexa X
print('%04x' % (valor))
print('%04X' % (valor)) # X Maiusculo printa maiusc