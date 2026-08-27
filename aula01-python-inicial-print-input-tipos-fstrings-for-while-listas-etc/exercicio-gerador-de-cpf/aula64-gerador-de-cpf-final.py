# MÓDULO PYTHON PARA GERAR NUMERO ALEATORIO
import random

nove_digitos = ''
# GERA UM NUMERO ALEATÓRIO DE 0 A 9 PARA O CPF random.randint(0,9)
# range(9) gera um range iterável de 0 a 9
for i in range(9):
    # string nove digitos recebe a conversão para str 
    # de 9 valores randomicos de inteiros
    nove_digitos += str(random.randint(0,9))

contador_regressivo_1 = 10
resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'
print(cpf_gerado_pelo_calculo)