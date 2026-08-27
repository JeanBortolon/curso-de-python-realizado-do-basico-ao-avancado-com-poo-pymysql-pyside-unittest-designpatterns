'''FAÇA UMA CALCULADORA'''



while True:
    operacao = input('Selecione a operação desejada: + ou - ou * ou / :')
    if (operacao != "+") and (operacao != "-") and (operacao != "*") and (operacao != "/") :
        print('Operação selecionada inválida.')
        continue
    else:
        num1 = input('Digite o primeiro numero: ')
        num2 = input('Digite o segundo numero: ')
        #if (num1.isdigit()) and (num2.isdigit()):
        try:
            numCalc1 = float(num1)
            numCalc2 = float(num2)
            if operacao == '+':
                resultado = numCalc1 + numCalc2
                print(f'O resultado da adição é:{resultado:.2f}')
            elif operacao == '-':
                resultado = numCalc1 - numCalc2
                print(f'O resultado da subtração é:{resultado:.2f}')
            elif operacao == '*':
                resultado = numCalc1 * numCalc2
                print(f'O resultado da multiplicação é:{resultado:.2f}')
            elif operacao == '/':
                if numCalc2 == 0:
                    print('Não é possível dividir por zero')
                    continue
                else:
                    resultado = numCalc1 / numCalc2
                    print(f'O resultado da divisão é:{resultado:.2f}')
        except:
            print('Você Digitou um valor inválido')
