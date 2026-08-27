''' FAÇA UM PROGRAMA QUE PEÇA AO USUÁRIO PARA DIGITAR UM NUMERO INTEIRO,
INFORME SE ESTE NUMERO É PAR OU IMPAR. CASO O USUÁRIO NÃO DIGITE UM NUMERO
INTEIRO, INFORME QUE NÃO É UM NUMERO INTEIRO. '''

num = input('Por gentileza digite um numero inteiro:')

if num.isdigit():
    num_int = int(num)
    if (num_int % 2) == 0:  # CALCULA O MODULO, SOBRA DA DIVISÃO
        print('Seu número é par')
    else:
        print('Seu número é impar')

else:
    print('Você não digitou um número inteiro')