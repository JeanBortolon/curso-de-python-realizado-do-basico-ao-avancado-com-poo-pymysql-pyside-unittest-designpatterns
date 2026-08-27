# if / elif ...../ else
# se / se não se / se não

entrada = input("Você deseja entrar ou sair ? :")
print(f'O Usuário digitou:{entrada}')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não selecionou uma opção válida')

'''Posso ter vários testes de elif porém só
uma condição será executada'''

print('FORA DOS BLOCOS')