"""
Mediator é um padrão de projeto comportamental
que tem a intenção de definir um objeto que
encapsula a forma como um conjunto de objetos
interage. O Mediator promove o baixo acoplamento
ao evitar que os objetos se refiram uns aos
outros explicitamente e permite variar suas
interações independentemente.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Colleague (Colega)
# A classe abstrata Colleague define a interface para os objetos que se comunicarão
# através do Mediator. Cada colega possui um nome e métodos para enviar
# e receber mensagens.
class Colleague(ABC):
    def __init__(self):
        # Inicializa o nome do colega, que será definido nas classes concretas.
        self.name: str

    @abstractmethod
    def broadcast(self, msg: str) -> None:
        """
        Método abstrato para enviar uma mensagem para todos os outros colegas
        através do Mediator.
        """
        pass

    @abstractmethod
    def direct(self, msg: str) -> None:
        """
        Método abstrato para receber uma mensagem direta.
        """
        pass


# Concrete Colleague (Colega Concreto)
# A classe Person é uma implementação concreta de Colleague. Ela mantém uma referência
# ao Mediator (Chatroom) e usa-o para se comunicar com outros colegas.
class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        # Chama o construtor da classe base (Colleague)
        super().__init__()
        # Define o nome da pessoa.
        self.name = name
        # Armazena a referência ao objeto Mediator.
        self.mediator = mediator

    def broadcast(self, msg: str) -> None:
        """
        Envia uma mensagem de broadcast para todos os colegas através do Mediator.
        A própria Person não sabe quem são os outros colegas, apenas delega
        a tarefa ao Mediator.
        """
        self.mediator.broadcast(self, msg)

    def send_direct(self, receiver: str, msg: str) -> None:
        """
        Envia uma mensagem direta para um colega específico através do Mediator.
        A Person não sabe como encontrar o destinatário, apenas o Mediator sabe.
        """
        self.mediator.direct(self, receiver, msg)

    def direct(self, msg: str) -> None:
        """
        Recebe e exibe uma mensagem direta.
        """
        print(f'{self.name} recebeu: {msg}')


# Mediator (Mediador)
# A classe abstrata Mediator define a interface para o Mediator. Ela declara
# métodos para os colegas se comunicarem.
class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str) -> None:
        """
        Método abstrato para um colega enviar uma mensagem de broadcast.
        """
        pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        """
        Método abstrato para um colega enviar uma mensagem direta a outro.
        """
        pass


# Concrete Mediator (Mediador Concreto)
# A classe Chatroom é uma implementação concreta de Mediator. Ela gerencia
# a lista de colegas (Person) e orquestra a comunicação entre eles.
# Ela é responsável por encaminhar as mensagens de broadcast e diretas.
class Chatroom(Mediator):
    def __init__(self) -> None:
        # Lista de colegas (pessoas) na sala de chat.
        self.colleagues: List[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        """
        Verifica se um colega já está na sala de chat.
        """
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        """
        Adiciona um colega à sala de chat, se ainda não estiver presente.
        """
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        """
        Remove um colega da sala de chat, se estiver presente.
        """
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, msg: str) -> None:
        """
        Recebe uma mensagem de broadcast de um colega e a encaminha
        para todos os outros colegas na sala de chat.
        """
        if not self.is_colleague(colleague):
            # Se o colega não está na sala, não pode enviar broadcast.
            print(f'{colleague.name} não está na sala de chat.')
            return

        # Itera sobre todos os colegas na sala.
        for c in self.colleagues:
            # Envia a mensagem para todos, exceto para o remetente.
            if c != colleague:
                c.direct(f'{colleague.name} para todos: {msg}')

    def direct(self, sender: Colleague, receiver_name: str, msg: str) -> None:
        """
        Recebe uma mensagem direta de um remetente e a encaminha para
        o colega destinatário específico.
        """
        if not self.is_colleague(sender):
            # Se o remetente não está na sala, não pode enviar mensagem direta.
            print(f'{sender.name} não está na sala de chat.')
            return

        # Encontra o objeto do colega destinatário pelo nome.
        receiver_obj: List[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.name == receiver_name
        ]

        if not receiver_obj:
            # Se o destinatário não for encontrado, não pode enviar a mensagem.
            print(f'Destinatário "{receiver_name}" não encontrado na sala de chat.')
            return

        # Envia a mensagem para o destinatário encontrado.
        receiver_obj[0].direct(
            f'{sender.name} para {receiver_obj[0].name}: {msg}'
        )


if __name__ == "__main__":
    # Exemplo de uso do padrão Mediator (Chatroom)

    # Cria uma instância do Mediator concreto (Chatroom).
    chat = Chatroom()

    # Cria instâncias de colegas concretos (Person).
    joao = Person('João', chat)
    maria = Person('Maria', chat)
    elis = Person('Elis', chat)
    jose = Person('José', chat)

    # Adiciona os colegas à sala de chat. O Mediator agora os gerencia.
    chat.add(joao)
    chat.add(maria)
    chat.add(elis)
    chat.add(jose)

    print('--- Broadcast Messages ---')
    # João envia um broadcast. Ele não sabe quem são os outros,
    # apenas o Mediator (chat) lida com isso.
    joao.broadcast('Olá pessoal!')
    # Maria envia um broadcast.
    maria.broadcast('E aí, tudo bem?')
    # José tenta enviar um broadcast, mas ele não foi adicionado corretamente
    # ao chat no exemplo original. No entanto, com a correção do broadcast,
    # ele enviaria para todos (exceto ele mesmo) se estivesse adicionado.
    # Vamos demonstrar o caso de um colega não adicionado.
    person_not_in_chat = Person('Carlos', chat)
    person_not_in_chat.broadcast('Eu não estou no chat, posso enviar?')
    print()

    print('--- Direct Messages ---')
    # João envia uma mensagem direta para Maria. Ele não interage
    # diretamente com Maria, o Mediator faz o roteamento.
    joao.send_direct('Maria', 'Oi Maria, tudo bem?')
    # Maria responde diretamente a João.
    maria.send_direct('João', 'Bem e você?')
    # Elis tenta enviar para alguém que não existe na sala.
    elis.send_direct('Pedro', 'Olá Pedro!')
    print()

    # Demonstração de remover um colega e tentar enviar uma mensagem
    print('--- Removing Colleague ---')
    chat.remove(jose)
    jose.broadcast('Vou sair do chat!') # Esta mensagem não deve ser processada como broadcast
    joao.send_direct('José', 'José, você saiu?') # Esta mensagem não deve ser entregue
    print()

    # Adiciona José de volta para novas interações
    chat.add(jose)
    print('--- José de volta ---')
    jose.broadcast('Voltei!')

