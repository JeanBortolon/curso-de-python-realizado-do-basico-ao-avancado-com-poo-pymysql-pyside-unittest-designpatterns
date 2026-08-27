''' FAÇA UM PROGRAMA QUE PERGUNTE A HORA AO USUÁRIO E, BASEANDO-SE 
NO HORÁRIO DESCRITA, EXIBA A SAUDAÇÃO APROPRIADA. EX:
BOM DIA 0-11, BOA TARDE 12-17 E BOA NOITE 18-23'''

hora = input('Digite apenas a HORA do dia:')

if hora.isdigit():
    hora_num = int(hora)
    if (hora_num >= 0) and (hora_num <= 23):
        if (hora_num >= 0) and (hora_num <= 11):
            print('BOM DIA!')
        elif (hora_num >= 12) and (hora_num <= 17):
            print('BOA TARDE!')
        else:
            print('BOA NOITE!')
    else:
        print('Você digitou uma hora inválida, digite um valor de 0 a 23.')
else:
    print('Você digitou um valor inválido, digite apenas a HORA do dia.')