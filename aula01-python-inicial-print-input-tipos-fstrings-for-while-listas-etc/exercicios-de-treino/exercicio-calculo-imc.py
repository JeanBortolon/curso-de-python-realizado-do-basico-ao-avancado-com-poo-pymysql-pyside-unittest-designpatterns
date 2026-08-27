'''EXERCICIO INSERIR DADOS DO PACIENTE E CALCULAR IMC, APÓS ISSO PRINTAR
AS INFORMAÇÕES E O RESULTADO DO IMC'''
nome = 'Jean'
idade = 30
peso = 80.00
altura = 1.74
imc = peso/(altura * altura)

print('O paciente:%s tem:%d anos, pesa:%.1f quilos com altura de:%.2f metros e possui um IMC de:%.2f' % (nome,idade,peso,altura,imc))