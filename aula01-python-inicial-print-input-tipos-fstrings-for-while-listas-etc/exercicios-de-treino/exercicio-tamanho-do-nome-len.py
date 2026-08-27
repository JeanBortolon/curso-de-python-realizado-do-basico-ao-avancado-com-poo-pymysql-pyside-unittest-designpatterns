'''FAÇA UM PROGRAMA QUE PEÇA O PRIMEIRO NOME DO USUÁRIO. SE O NOME
TIVER 4 LETRAS OU MENOS ESCREVA [SEU NOME É CURTO], SE TIVER ENTRE 5
E 6 LETRAS, ESCREVA [ SEU NOME É NORMAL ] SE TIVER MAIS QUE 6 LETRAS
ESCREVA [ SEU NOME É MUITO GRANDE ]. '''

nome = input('Digite apenas o seu PRIMEIRO nome:')

if (' ' in nome) or (nome.isdigit()):
    print('Nome digitado inválido, digite apenas o PRIMEIRO nome.')
else:
    if len(nome) <= 4:
        print('SEU NOME É CURTO.')
    elif (len(nome) == 5) or (len(nome) == 6):
        print('SEU NOME É NORMAL.')
    else:
        print('SEU NOME É MUITO GRANDE.')
