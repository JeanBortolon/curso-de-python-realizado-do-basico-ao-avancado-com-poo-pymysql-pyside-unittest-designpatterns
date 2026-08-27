'''EXERCICIO: SOLICITAR DOIS VALORES E COMPARAR QUAL É MAIOR
E ENTÃO PRINTAR QUAL É O MAIOR VALOR ENTRE ELES '''

valor_1 = input('Digite o primeiro valor:')
valor_2 = input('Digite o segundo valor:')
valor_1_num = valor_1.isdigit()
valor_2_num = valor_2.isdigit()

if valor_1_num and valor_2_num:
    valor_1_float = float(valor_1)
    valor_2_float = float(valor_2)
    if valor_1_float > valor_2_float:
        print(f'O primeiro valor:{valor_1_float} é maior que o segundo valor:{valor_2_float}')
    else:
        print(f'O segundo valor:{valor_2_float} é maior que o primeiro valor:{valor_1_float}')
else:
    print('Valor digitado inválido, digite apenas números.')
    

