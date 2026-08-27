"""
TDD significa Desenvolvimento Orientado por Testes (Test Driven 
Development), uma prática de desenvolvimento de software onde a 
codificação começa pela escrita de testes unitários. Criada por Kent 
Beck, é um dos pilares do XP (Extreme Programming).

O TDD segue um ciclo chamado Red, Green, Refactor, que funciona assim:

1. Escrevemos um teste para a funcionalidade desejada. Ao executar, o 
   teste deve falhar, pois a implementação ainda não existe (step red).

2. Implementamos a funcionalidade e executamos o teste novamente. Desta 
   vez, o teste deve passar com sucesso (step green).

3. Com os testes funcionando, passamos ao step refactor. Nesse momento, 
   refatoramos o código, melhorando-o e aplicando boas práticas de 
   programação.
"""

'''
Algoritmo proposto:
1 - Receber um número inteiro
2 - Saber se o número é múltiplo de 3 e 5:
    Se for múltiplo retorna bacon com ovos
3 - Saber se o número é múltiplo somente de 3:
    Se for retorna Bacon
4 - Saber se o número é múltiplo somente de 5:
    Se for retorna Ovos
5 - Saber se o número NÃO é múltiplo de 3 e 5:
    Se for retorna Passa fome
'''

# Define a função bacon_com_ovos que avalia múltiplos de 3 e 5
def bacon_com_ovos(n):
    # Verifica se o argumento n é um número inteiro, caso contrário lança um erro
    assert isinstance(n, int), 'n deve ser int'
    # Verifica se n é múltiplo de 3 e 5
    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'  # Retorna "Bacon com ovos" se for múltiplo de 3 e 5
    # Verifica se n é múltiplo somente de 3
    if n % 3 == 0:
        return 'Bacon'  # Retorna "Bacon" se for múltiplo de 3
    # Verifica se n é múltiplo somente de 5
    if n % 5 == 0:
        return 'Ovos'  # Retorna "Ovos" se for múltiplo de 5
    # Caso n não seja múltiplo de 3 nem de 5
    return 'Passar fome'  # Retorna "Passar fome" se não for múltiplo de 3 nem de 5
