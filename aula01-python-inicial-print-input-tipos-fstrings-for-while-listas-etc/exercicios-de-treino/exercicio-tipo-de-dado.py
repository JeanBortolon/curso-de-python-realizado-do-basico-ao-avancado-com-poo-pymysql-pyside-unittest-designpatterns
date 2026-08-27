'''EXERCICIO: INSERIR DADOS DE TODOS OS TIPOS E PRINTAR'''

nome = 'Jean'
sobrenome = 'Bortolon'
idade = 30
ano_nascimento = 1994
maior_de_idade = idade >= 18
altura_metros = 1.74

print('Nome:',nome)
print('Sobrenome:',sobrenome)
print('Idade:',idade)
print('Ano de nascimento:',ano_nascimento)
if maior_de_idade:
    print('É maior de idade !')
else:
    print('É menor de idade !')
print('Altura em metros:',altura_metros)
