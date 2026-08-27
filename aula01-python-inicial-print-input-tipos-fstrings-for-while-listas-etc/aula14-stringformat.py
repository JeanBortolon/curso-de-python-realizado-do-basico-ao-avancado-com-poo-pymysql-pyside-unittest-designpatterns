# A Função Format fica dentro do objeto string
# Quando uma função fica dentro do objeto é chamada
# de método.
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)

'''É possível formatar strings utilizando a format
basta colocar .format na frente da string
que deseja trabalhar e passar os argumentos
que a format está pedindo, posso referenciar
na ordem, esses argumentos em outra string
utilizando a chamada por chaves, deixando
as chaves vazias eu pego na ordem, colocando
parametros nomeados no format eu consigo chamar pelo
nome do parametro entre chaves ou seja, um parametro
que referencia o valor de outra variável.
Se eu colocar chaves além da quantidade de
argumentos, por exemplo neste, 4 chaves
apresentaria o erro replacement index out of
range, ou seja, estou tentando referenciar
uma quantidade de itens além dos parametros.'''