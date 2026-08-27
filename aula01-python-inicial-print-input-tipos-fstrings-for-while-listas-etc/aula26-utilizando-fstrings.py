"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
Em programação, "pad" geralmente significa
 preencher uma string ou número com caracteres 
 adicionais para atingir uma largura fixa. 
 Isso é frequentemente usado para formatar a saída
de dados para que ela tenha uma aparência 
consistente, mesmo quando os valores originais
têm comprimentos diferentes."""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # faz o pad pegando o
# valor da variável e complemetando caracteres a
# esquerda dela até bater 10 com a str da var
# indo para a direita
print(f'{variavel: <10}.') # mesma coisa acima
# só que agora joga a var pra esquerda e caractere
# pra direita até bater 10
print(f'{variavel:$<10}.') #também posso preencher
# com outros caracteres.
var2 = 'abcd'
print(f'{var2:0^10}') #posso jogar a var no centro
#entre 10 caracteres
print(f'{123.45678:.3f}') #casas decimais no valor
print(f'{1234.45678:,.2f}') #posso colocar virgula
# quando o valor for acima de 1000
print(f'{1234.45678:+.2f}') #posso forçar aparecer
#simbolo de positivo na frente do numero
print(f'{1234.45678:0=+10,.2f}') #posso inserir zeros a
#esquerda
print(f'O Hexadecimal de 1500 é: {1500:04X}')
# 04X converte em para Hexa com 4 digitos e valor
# printado em maiusculo
print(f'{var2!r}')
''' !r -> o método __repr__() é usado para fornecer 
 uma representação em string de um objeto,
geralmente para fins de depuração e desenvolvimento.
Ele é chamado quando a função repr() é usada no 
objeto, ou quando o objeto é exibido no console 
interativo.'''
print(f'{var2!s}') # !s -> método __str__
print(f'{var2!a}') # !a -> método __ascii_