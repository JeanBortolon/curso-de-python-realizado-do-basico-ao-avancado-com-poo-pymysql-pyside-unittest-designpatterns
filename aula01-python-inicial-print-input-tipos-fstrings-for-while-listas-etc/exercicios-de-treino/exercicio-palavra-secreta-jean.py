"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

tentativas = 1
secret_word = 'jean'


while tentativas <= 10: 
        chute = input("Digite uma letra da palavra secreta: ")
        if len(chute) > 1:
             print('Tamanho invalido, digite apenas uma letra')
             continue
        if chute in secret_word:
            print(f'A letra "{chute}" ESTÁ na palavra, \
                você usou {tentativas} de 10 tentivas ')
            tentativas += 1
        else:
            print(f'A letra "{chute}" NÃO ESTÁ na palavra, \
                você usou {tentativas} de 10 tentivas ')
            tentativas += 1
else:
     print('Você esgotou suas tentativas')

''' 
     O FOR é utilizado para que uma variavel percorra a outra
     [FOR VAR1 IN VAR2: ou seja VAR1 vai correr por toda VAR2 e se 
     printarmos a VAR1 ela irá reproduzindo toda a VAR2 que está percorrendo],0
     O print indica cada posição percorrida e quando as letras
     forem compativeis ele printara, quando não forem compativeis
     ele irá printar um asterico no local.
'''