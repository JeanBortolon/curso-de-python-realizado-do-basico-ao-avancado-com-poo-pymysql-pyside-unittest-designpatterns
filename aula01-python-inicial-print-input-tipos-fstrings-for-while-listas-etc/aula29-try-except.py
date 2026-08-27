"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

#input recebe str se eu multiplicar por 2 vai receber 
#duas vezes o texto da string portanto:

#numero_float = float(numero_str)
#print(f'Você digitou o numero {numero_str} e o dobro é: {numero_float*2:.2f}')
#agora tratamos o numero

'''Eu poderia testar se é um numero inteiro
utilizando o método IsDigit de um numero e testa
ndo com if, porém o try e o except permite
que testamos sem causar erro no programa
ele indica qual foi o erro, chamado de fail fast'''

'''
if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'Você digitou o numero {numero_str} e o dobro é: {numero_float*2:.2f}')
else:
    print('Isso não é um numero inteiro')

'''

'''Agora com o try e except podemos testar melhor
ele vai rodar até onde rolar um erro
diferente do resto do programa que se tiver erro
nem roda, exemplo converter string A para float
daria erro fora, aqui no try ele vai tentando
até dar o erro e depois ele mostra q deu erro
ou seja, até o print do numero_str ele roda.
Posso escolher a partir de qual linha eu quero
testar se está errado, no meu caso a partir
da segunda, se eu botasse a conversão na primeira
eu já pularia para a except'''
try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'Você digitou o numero {numero_str} e o dobro é: {numero_float*2:.2f}')
except:
    print('Isso não é um numero')