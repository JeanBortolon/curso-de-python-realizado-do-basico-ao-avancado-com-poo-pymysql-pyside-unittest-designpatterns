"""
Chain of responsibility (COR) é um padrão comportamental
que tem a intenção de evitar o acoplamento do remetente de
uma solicitação ao seu receptor, ao dar a mais de um objeto
a oportunidade de tratar a solicitação.
Encadear os objetos receptores passando a solicitação
ao longo da cadeia até que um objeto a trate.
"""

from abc import ABC, abstractmethod


# Handler Abstrato: Define a interface para os objetos que manipulam a solicitação
# e implementa o encadeamento para o próximo objeto na cadeia.
class Handler(ABC):
    def __init__(self) -> None:
        # O sucessor é o próximo manipulador na cadeia.
        # Ele será definido durante a construção da cadeia.
        self.sucessor: Handler

    @abstractmethod
    # O método handle é a interface para processar a solicitação.
    # Cada manipulador concreto irá implementar sua própria lógica de tratamento.
    def handle(self, letter: str) -> str: pass


# Manipulador Concreto: HandlerABC tenta lidar com as letras 'A', 'B', 'C'.
# Se não conseguir, ele passa a solicitação para o próximo sucessor.
class HandlerABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        # Define as letras que este manipulador pode tratar.
        self.letters = ['A', 'B', 'C']
        # Armazena o próximo manipulador na cadeia.
        self.sucessor = sucessor

    # Implementa a lógica de tratamento para HandlerABC.
    def handle(self, letter: str) -> str:
        # Se a letra está na lista de responsabilidade deste manipulador, ele a trata.
        if letter in self.letters:
            return f'HandlerABC: conseguiu tratar o valor {letter}'
        # Caso contrário, a solicitação é passada para o próximo manipulador na cadeia.
        return self.sucessor.handle(letter)


# Manipulador Concreto: HandlerDEF tenta lidar com as letras 'D', 'E', 'F'.
# Se não conseguir, ele passa a solicitação para o próximo sucessor.
class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        # Define as letras que este manipulador pode tratar.
        self.letters = ['D', 'E', 'F']
        # Armazena o próximo manipulador na cadeia.
        self.sucessor = sucessor

    # Implementa a lógica de tratamento para HandlerDEF.
    def handle(self, letter: str) -> str:
        # Se a letra está na lista de responsabilidade deste manipulador, ele a trata.
        if letter in self.letters:
            return f'HandlerDEF: conseguiu tratar o valor {letter}'
        # Caso contrário, a solicitação é passada para o próximo manipulador na cadeia.
        return self.sucessor.handle(letter)


# Manipulador Concreto: HandlerUnsolved é o último manipulador na cadeia.
# Ele é responsável por tratar as solicitações que nenhum outro manipulador conseguiu resolver.
class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        # Este manipulador simplesmente indica que a solicitação não foi tratada pelos anteriores.
        return f'HandlerUnsolved: não tratou {letter}'


# Bloco principal para testar a implementação da Cadeia de Responsabilidade.
if __name__ == "__main__":
    # 1. Cria o último manipulador na cadeia.
    # Este manipulador não tem um sucessor, pois ele encerra a cadeia.
    handler_unsolved = HandlerUnsolved()
    # 2. Cria o manipulador para 'D', 'E', 'F', passando o handler_unsolved como seu sucessor.
    handler_def = HandlerDEF(handler_unsolved)
    # 3. Cria o manipulador para 'A', 'B', 'C', passando o handler_def como seu sucessor.
    # Este é o ponto de entrada da cadeia para as solicitações.
    handler_abc = HandlerABC(handler_def)

    # Testando a cadeia a partir de handler_abc (o primeiro na cadeia)
    print("--- Testando a cadeia a partir de handler_abc ---")
    print(handler_abc.handle('A'))  # Deve ser tratado por HandlerABC
    print(handler_abc.handle('B'))  # Deve ser tratado por HandlerABC
    print(handler_abc.handle('C'))  # Deve ser tratado por HandlerABC
    print(handler_abc.handle('D'))  # Deve passar para HandlerDEF e ser tratado por ele
    print(handler_abc.handle('E'))  # Deve passar para HandlerDEF e ser tratado por ele
    print(handler_abc.handle('F'))  # Deve passar para HandlerDEF e ser tratado por ele
    print(handler_abc.handle('G'))  # Deve passar para HandlerUnsolved
    print(handler_abc.handle('H'))  # Deve passar para HandlerUnsolved
    print(handler_abc.handle('I'))  # Deve passar para HandlerUnsolved

    print("\n--- Testando a cadeia a partir de handler_def ---")
    # Testando a cadeia a partir de handler_def (ignorando HandlerABC)
    print(handler_def.handle('A'))  # Deve passar para HandlerUnsolved
    print(handler_def.handle('B'))  # Deve passar para HandlerUnsolved
    print(handler_def.handle('C'))  # Deve passar para HandlerUnsolved
    print(handler_def.handle('D'))  # Deve ser tratado por HandlerDEF
    print(handler_def.handle('E'))  # Deve ser tratado por HandlerDEF
    print(handler_def.handle('F'))  # Deve ser tratado por HandlerDEF
    print(handler_def.handle('G'))  # Deve passar para HandlerUnsolved
    print(handler_def.handle('H'))  # Deve passar para HandlerUnsolved
    print(handler_def.handle('I'))  # Deve passar para HandlerUnsolved

    print("\n--- Testando a cadeia a partir de handler_unsolved ---")
    # Testando a cadeia a partir de handler_unsolved (o último manipulador)
    print(handler_unsolved.handle('A')) # Deve ser tratado por HandlerUnsolved imediatamente
    print(handler_unsolved.handle('B')) # Deve ser tratado por HandlerUnsolved imediatamente
    print(handler_unsolved.handle('C')) # Deve ser tratado por HandlerUnsolved imediatamente
    print(handler_unsolved.handle('D')) # Deve ser tratado por HandlerUnsolved imediatamente
    print(handler_unsolved.handle('E')) # Deve ser tratado por HandlerUnsolved imediatamente
    print(handler_unsolved.handle('F')) # Deve ser tratado por HandlerUnsolved imediatamente
    print(handler_unsolved.handle('G')) # Deve ser tratado por HandlerUnsolved imediatamente
    print(handler_unsolved.handle('H')) # Deve ser tratado por HandlerUnsolved imediatamente
    print(handler_unsolved.handle('I')) # Deve ser tratado por HandlerUnsolved imediatamente

