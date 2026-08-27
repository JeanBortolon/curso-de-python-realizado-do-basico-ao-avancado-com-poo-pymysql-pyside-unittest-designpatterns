# o que vai dentro dos parenteses da função é chamado argumento
# posso passar 1 ou vários colocando virgula (12,'abc',45)
print(12, 34) # control c control v duplica a linha
print(56, 78,32) # espaço e quebra de linha são colocados automatico
#esse tipo de argumento é chamado argumento não nomeado.
print(12, 34, sep="  ") #posso colocar outro separador sem ser 1 espaço
print(12, 34, sep='  ') #posso colocar outro separador sem ser 1 espaço
#inserindo um argumento nomeado como sep, posso controlar o separador
print(12, 34, sep='-') #posso colocar outro separador sem ser espaço
# \r\n -> CRLF -> Carriage Return, Line Feed
# combinação de dois caracteres de controle que quebram a linha e
# retornam para o começo para escrever novamente
print(12, 34, sep=" ", end='\r\n')
print(12, 34, sep=" ", end='##') 
print('não quebrou a linha com cerquilha apenas indicou o fim')
print('posso usar argumento nomeados para controlar separador e fim')
print('python é case sensitive, não usar maiuscula e minuscula')