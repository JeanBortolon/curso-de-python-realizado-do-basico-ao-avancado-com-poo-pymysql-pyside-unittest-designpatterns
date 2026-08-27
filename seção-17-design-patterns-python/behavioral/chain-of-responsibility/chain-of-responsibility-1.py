# Implementação do padrão Chain of Responsibility (Cadeia de Responsabilidade) usando funções.
#
# O padrão Chain of Responsibility permite que você passe requisições ao longo de uma cadeia de handlers.
# Cada handler decide se processa a requisição ou a passa para o próximo handler na cadeia.
#
# Neste exemplo, temos uma cadeia de funções onde cada função tenta "tratar" uma letra.
# Se uma função não conseguir tratar a letra, ela passa a responsabilidade para a próxima.


def handler_ABC(letter: str) -> str:
    # Este handler é responsável por tratar as letras 'A', 'B', 'C'.
    letters = ['A', 'B', 'C']

    if letter in letters:
        # Se a letra estiver na lista de responsabilidade deste handler, ele a trata.
        return f'handler_ABC: conseguiu tratar o valor {letter}'
    # Se não puder tratar, ele passa a requisição para o próximo handler na cadeia.
    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
    # Este handler é responsável por tratar as letras 'D', 'E', 'F'.
    letters = ['D', 'E', 'F']

    if letter in letters:
        # Se a letra estiver na lista de responsabilidade deste handler, ele a trata.
        return f'handler_DEF: conseguiu tratar o valor {letter}'
    # Se não puder tratar, ele passa a requisição para o próximo handler na cadeia.
    return handler_unsolved(letter)


def handler_unsolved(letter: str) -> str:
    # Este é o handler final na cadeia. Se a requisição chegar aqui, significa que
    # nenhum dos handlers anteriores foi capaz de tratá-la.
    return f'handler_unsolved: não sei tratar {letter}'


if __name__ == "__main__":
    # Demonstração da cadeia de responsabilidade
    print('--- Testando handler_ABC com diferentes entradas ---')
    # 'A' é tratado por handler_ABC
    print(handler_ABC('A'))
    # 'B' é tratado por handler_ABC
    print(handler_ABC('B'))
    # 'C' é tratado por handler_ABC
    print(handler_ABC('C'))
    # 'D' não é tratado por handler_ABC, passado para handler_DEF
    print(handler_ABC('D'))
    # 'E' não é tratado por handler_ABC, passado para handler_DEF
    print(handler_ABC('E'))
    # 'F' não é tratado por handler_ABC, passado para handler_DEF
    print(handler_ABC('F'))
    # 'G' não é tratado por handler_ABC, nem por handler_DEF, passado para handler_unsolved
    print(handler_ABC('G'))
    # 'H' não é tratado por handler_ABC, nem por handler_DEF, passado para handler_unsolved
    print(handler_ABC('H'))
    # 'I' não é tratado por handler_ABC, nem por handler_DEF, passado para handler_unsolved
    print(handler_ABC('I'))
