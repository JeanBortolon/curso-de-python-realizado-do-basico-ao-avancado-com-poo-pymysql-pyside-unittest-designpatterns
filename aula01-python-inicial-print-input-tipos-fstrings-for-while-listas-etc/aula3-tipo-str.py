"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""
print(1234)
#control x control v recorta e cola em outra parte

# Strings podem ser passadas no argumento como Aspas Simples
print('Jean Bortolon')

# Strings podem ser passadas no argumento como Aspas Duplas
print("Jean Bortolon")

#Posso utilizar caracter de escape \ para pular algo exemplo:
print("Jean \"Bortolon") #quando ver a barra ignora o proximo carac.
# a outra aspa que quebraria a string será apenas concatenada
# é o mesmo conceito da barra dupla do HIscada.

''' r pode ser utilizado para expressões regulares e mostrar o
caracter de escape'''  
print(r"Jean \"Bortolon\"")

'''Não é necessário muitas vezes utilizar o r pois é possível
inserir aspas duplas dentro de aspas simples combinando na sua
string e com isso consegue inserir os caracteres necessários sem
quebrar a sintaxe, veja abaixo:'''
print('Jean "Bortolon"')
print(1,'Jean "Bortolon"') #mesmo exemplo com multiplos argumentos