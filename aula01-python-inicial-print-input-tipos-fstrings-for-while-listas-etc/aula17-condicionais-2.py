# if / elif ...../ else
# se / se não se / se não

condicao1 = False
condicao2 = False
condicao3 = False
condicao4 = True


if condicao1:
    print('código para condição 1')
elif condicao2:
    print('código para condição 2')
elif condicao3:
    print('código para condição 3')
elif condicao4:
    print('código para condição 4')
    pass  #funciona como Ellipsis (...) também para pular
else:
    print('Nenhuma condição foi executada')

#APENAS A PRIMEIRA CONDIÇÃO ATENDIDA SERÁ EXECUTADA
#SE PRECISAR TESTAR MULTIPLAS CONDIÇÕES PRECISO DE
#MULTIPLOS IFS

