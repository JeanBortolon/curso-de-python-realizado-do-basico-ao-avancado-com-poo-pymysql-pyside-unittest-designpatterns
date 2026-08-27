"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
nome = input("Digite seu nome:")
idade = input("Digite sua idade:")

if (nome == '') or (idade == ''):
    print('Desculpe, você deixou campos vazios.')
else:
    nome_invertido = nome[::-1]
    nome_space = ' ' in nome
    tamanho_nome = len(nome)
    primeira_letra = nome[0]
    ultima_letra = nome[-1]
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome_invertido}')
    if nome_space:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não tem contém espaços.')
    print(f'Seu nome tem {tamanho_nome} letras')
    print(f'A primeira letra do seu nome é {primeira_letra}')
    print(f'A última letra do seu nome é {ultima_letra}')