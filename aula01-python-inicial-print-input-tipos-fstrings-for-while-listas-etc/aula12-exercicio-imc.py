'''Cálculo do IMC = peso / (altura x altura)
onde o peso é em quilogramas e a altura 
em metros. '''

nome = 'Jean Bortolon'
altura = 1.74
peso = 80
imc = peso / (altura * altura)

print('O Paciente:', nome, 'mede:', altura, 'metros', ' e pesa:', peso, 'quilos', 'possuindo um IMC de:', imc)

imc2 = peso / altura**2
print(round(imc2,2)) #Lembrete de precedencia de exp
#função round formata casas decimais do valor

'''Em python podemos colocar var = ...
os 3 pontinhos são chamados de ellipsis
são place holders, basicamente permitem
que não seja atribuído nada porém não dá
erro na hora de compilar, servem para
"segurar o lugar do valor a ser atribuido"'''
print(...)