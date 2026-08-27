"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# DECLARA A VARIAVEL DO CPF EM STRING
cpf = '746824890'

# FATIA OS VALORES EM 9 DIGITOS A PARTIR DO INDICE ZERO
nove_digitos = cpf[:9] 
# PRINTA OS DIGITOS FATIADOS
print(nove_digitos)

# CRIA O CONTADOR REGISTRO PARA MULTIPLICARA  PARTIR DE 10
contador_regressivo_1 = 10

# CRIA A VARIÁVEL QUE GUARDARÁ O RESULTADO
resultado_1 = 0

# PARA CADA DIGITO QUE CORRESPONDE A POSIÇÃO NA VAR NOVE DIGITOS
for digito_1 in nove_digitos:
    # ATRIBUO A SOMA DA MULTIPLICAÇÃO DO DIGITO DO INDICE CONVERT
    resultado_1 += int(digito_1) * contador_regressivo_1
    # REDUZO O VALOR DO CONTADOR REGRESSIVO
    contador_regressivo_1 -= 1
# PRINTA O RESULTADO DA SOMA DA MULTIPLICAÇÃO * 10 MÓDULO 11
digito_1 = (resultado_1 * 10) % 11
print(digito_1)

# FAÇA A LÓGICA USANDO TERNÁRIO SE O VALOR É MAIOR QUE 9
# DIGITO VAI SER DIGITO SE DIGITO FOR <= 9 SE NÃO 0
digito_1 = digito_1 if digito_1 <= 9 else 0

