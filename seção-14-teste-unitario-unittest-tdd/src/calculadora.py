# Define a função soma que realiza a soma de dois números
def soma(x, y):
    '''Soma x e y
    >>> soma(10,20)  # Exemplo de uso da função com resultado esperado
    30
    '''
    # Verifica se x é do tipo int ou float, caso contrário lança um erro
    assert isinstance(x, (int, float)), 'x precisa ser int ou float '
    # Verifica se y é do tipo int ou float, caso contrário lança um erro
    assert isinstance(y, (int, float)), 'y precisa ser int ou float '
    # Retorna a soma de x e y
    return x + y

# Define a função subtrai que realiza a subtração de dois números
def subtrai(x, y):
    '''Subtrai x e y

    >>> subtrai(10, 5)  # Exemplo de uso da função com resultado esperado
    5
    >>> subtrai('10', 5)  # Este exemplo não é válido devido à validação
    5
    '''
    # Verifica se x é do tipo int ou float, caso contrário lança um erro
    assert isinstance(x, (int, float)), 'x precisa ser int ou float '
    # Verifica se y é do tipo int ou float, caso contrário lança um erro
    assert isinstance(y, (int, float)), 'y precisa ser int ou float '
    # Retorna a subtração de x e y
    return x - y

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Importa o módulo doctest para executar testes embutidos na documentação
    import doctest
    # Executa os testes definidos na documentação das funções com saída detalhada
    doctest.testmod(verbose=True)