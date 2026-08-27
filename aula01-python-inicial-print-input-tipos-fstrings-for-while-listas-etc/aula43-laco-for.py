'''

# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')
texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
'''
''' Exemplo Jean Printando letra a letra de uma palavra 
texto = 'python'

indice = 0

while indice < len(texto):
    letra = texto[indice]
    print(f'Printando cada letra de uma vez {letra}')
    indice += 1
'''

texto = 'python'

novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'  #asterisco concatenando letra +=
    print(letra)
print(novo_texto + '*') #print do texto final concatenado fora do FOR