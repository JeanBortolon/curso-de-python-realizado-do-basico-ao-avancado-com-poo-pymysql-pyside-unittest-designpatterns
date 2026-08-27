
"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
#Em Python vars tem ID na memoria, pode ser
#que sejam iguais, o python tenta otimizar
#se mudar o valor muda o id, é a identidade do
#objeto, como o python busca o elemento na memoria
v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

'''Se eu quiser testar se uma lógica passou
em um IF eu preciso setar a variavel fora do if
pq se eu colocar apenas dentro, ela seria criada
se passasse no if e daria erro no else ou outra
condição, portanto posso criar e atribuir None
'''
2
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
