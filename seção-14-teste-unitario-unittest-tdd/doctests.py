"""
Doctests são testes automatizados escritos diretamente na documentação
(docstring) de uma função ou classe em Python. Eles simulam uma sessão
interativa do terminal e verificam se o código retorna exatamente o
resultado esperado, servindo como guia de uso e teste.

Como funciona? O módulo doctest lê a docstring do seu código, busca por
linhas que começam com o prompt do Python (>>>) e executa esses comandos.
Em seguida, ele compara o resultado obtido com o que foi documentado logo
abaixo.
"""
def somar(a, b):
    """
    Soma dois números e retorna o resultado.

    Exemplos:
    >>> somar(2, 3)   aqui vai passar 
    5

    >>> somar(-1, 1)  aqui vai dar erro
    1
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
