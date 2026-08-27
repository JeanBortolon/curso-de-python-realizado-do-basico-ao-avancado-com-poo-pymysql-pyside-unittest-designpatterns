"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue

    print(contador)

    if contador == 40:
        break


print('Acabou')

'''Da mesma forma que o break termina o laço
o continue permite pular uma ação e voltar para
o teste while na posição que estava, exemplo
se eu colocar um continue antes de printar
o valor do contador == 6, ele vai voltar no while
ignorar essa condição e pular para o valor 7'''