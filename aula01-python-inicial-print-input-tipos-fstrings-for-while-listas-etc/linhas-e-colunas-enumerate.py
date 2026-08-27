
# Tabela com informações de alunos
students = [
    # nome      idade nota
    ['João',    14,   5.5],
    ['Maria',   13,   9.7],
    ['Luiz',    15,   8.8],
    ['Alberto', 16,   10],
]

'''
Para cada linha começando em 2 pois a 1 é cabeçalho
e não tem zero em tabela eu vou pegar a lista
de estudantes contidos na lista maior e seu indice [i]
que será utilizado para alimentar a planilha depois.
'''
for i, student_row in enumerate(students, start=2):
    '''para cada coluna começando em 1 pois não tem zero
    em tabela eu vou pegar os valores individuais de cada
    linha de estudante e seu indice [j] que será utilizado
    para alimentar a planilha depois.''' 
    for j, student_column in enumerate(student_row, start=1):
       # Forma linha e coluna com os valores para cada uma
       print(i, j, student_column) 