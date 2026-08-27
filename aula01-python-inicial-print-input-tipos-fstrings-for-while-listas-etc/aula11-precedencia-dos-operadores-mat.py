'''Precedência dos operadores aritméticos
Inserir parenteses e outros recursos
matemáticos para prioridade de cálculo.'''
# 1. (n + n) -> Parentese executa primeiro
# 2. ** -> Segunda prioridade é exponencial
# 3. * / // % -> mult, div, div int, modulo
# 4. + - -> Ultima prioridade é adição e sub.
'''Se os operadores possuem a mesma
prioridade serão executados da esquerda
para a direita.'''

conta_1 = 1 + 1 ** 5 + 5
'''A Idéia da conta acima é ser 2 elevado a 10
que vai dar 1024. Porém vai dar 7 pela regra
de prioridade da precedencia aritmética
será 1 elevado a 5 = 1 + 1 + 5 = 7'''
print(conta_1)

conta_2 = (1 + 1) ** (5 + 5)
print(conta_2)
'''Corrigindo as precedencias na conta 2
obtivemos sucesso.
*** LEMBRETE: Parenteses são executados
de dentro pra fora, os internos primeiro
e depois vai saindo.'''