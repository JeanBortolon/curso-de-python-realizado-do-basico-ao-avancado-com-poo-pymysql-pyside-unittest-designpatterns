"""
Command tem intenção de encapsular uma solicitação como
um objeto, desta forma permitindo parametrizar clientes com diferentes
solicitações, enfileirar ou fazer registro (log) de solicitações e suportar
operações que podem ser desfeitas.

É formado por um cliente (quem orquestra tudo), um invoker (que invoca as
solicitações), um ou vários objetos de comando (que fazem a ligação entre o
receiver e a ação a ser executada) e um receiver (o objeto que vai executar a
ação no final).

Neste exemplo:
- Receiver: Light (luz), GarageDoor (porta da garagem) - os objetos que realizam as ações.
- Command Interface: ICommand - define a interface para todos os comandos.
- Concrete Commands: LightOnCommand, LightChangeColor - implementam a interface Command e encapsulam uma ação específica para um Receiver.
- Invoker: RemoteController - solicita que o comando seja executado, sem saber quem é o Receiver ou qual ação será executada.
- Client: O bloco `if __name__ == "__main__":` - cria os objetos Receiver, Concrete Commands e o Invoker, e os configura.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


class Light:
    """ 
    Receiver - Luz Inteligente
    Esta classe representa o objeto que executa as operações reais.
    Ela não sabe nada sobre os comandos que a invocam.
    """

    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        """ Liga a luz. """
        print(f'{self.name} no {self.room_name} está ON')

    def off(self) -> None:
        """ Desliga a luz. """
        print(f'{self.name} no {self.room_name} está OFF')

    def change_color(self, color: str) -> None:
        """ Altera a cor da luz. """
        self.color = color
        print(f'{self.name} no {self.room_name} está {self.color}')


class ICommand(ABC):
    """ 
    Interface de comando abstrata.
    Define a interface para todos os objetos de comando.
    Todos os comandos concretos devem implementar os métodos execute e undo.
    """

    @abstractmethod
    def execute(self) -> None:
        """ Executa a ação do comando. """
        pass

    @abstractmethod
    def undo(self) -> None:
        """ Desfaz a última ação do comando. """
        pass


class LightOnCommand(ICommand):
    """ 
    Comando concreto para ligar a luz.
    Encapsula a solicitação para ligar um objeto Light.
    """

    def __init__(self, light: Light) -> None:
        self.light = light  # Referência ao objeto Receiver (Light)

    def execute(self) -> None:
        """ Chama o método 'on' do Receiver. """
        self.light.on()

    def undo(self) -> None:
        """ Desfaz a ação, chamando o método 'off' do Receiver. """
        self.light.off()


class LightChangeColor(ICommand):
    """ 
    Comando concreto para mudar a cor da luz.
    Encapsula a solicitação para mudar a cor de um objeto Light.
    """

    def __init__(self, light: Light, color: str) -> None:
        self.light = light  # Referência ao objeto Receiver (Light)
        self.color = color  # Nova cor a ser aplicada
        self._old_color = self.light.color  # Guarda a cor antiga para o undo

    def execute(self) -> None:
        """ 
        Chama o método 'change_color' do Receiver com a nova cor.
        Armazena a cor atual antes de mudar para permitir o undo.
        """
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        """ Desfaz a ação, chamando o método 'change_color' do Receiver com a cor antiga. """
        self.light.change_color(self._old_color)


class RemoteController:
    """ 
    Invoker - Controle Remoto.
    Esta classe é responsável por invocar os comandos.
    Ela armazena objetos de comando e os executa quando solicitado.
    Não sabe nada sobre as operações que os comandos realizam.
    """

    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}  # Mapeia nomes de botões para objetos de comando
        self._undos: List[Tuple[str, str]] = []  # Pilha para rastrear ações para desfazer (botão, ação)

    def button_add_command(self, name: str, command: ICommand) -> None:
        """ Adiciona um comando a um botão específico no controle remoto. """
        self._buttons[name] = command

    def button_pressed(self, name: str) -> None:
        """ 
        Simula o pressionar de um botão, executando o comando associado.
        Registra a ação para possível undo.
        """
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.append((name, 'execute'))  # Registra que o comando foi executado

    def button_undo(self, name: str) -> None:
        """ 
        Simula o pressionar do botão de desfazer para um comando específico.
        Registra a ação de desfazer para possível re-fazer (não implementado totalmente aqui).
        """
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name, 'undo'))  # Registra que o comando foi desfeito

    def global_undo(self) -> None:
        """ 
        Desfaz a última operação globalmente (a última que foi executada ou desfeita).
        Recupera a última ação da pilha _undos e invoca o método oposto no comando.
        """
        if not self._undos:
            print('Nothing to undo')
            return None

        button_name, action = self._undos[-1]  # Pega a última ação

        if action == 'execute':
            # Se a última ação foi 'execute', desfazemos
            self._buttons[button_name].undo()
        else:
            # Se a última ação foi 'undo', re-executamos (refazemos)
            self._buttons[button_name].execute()

        self._undos.pop()  # Remove a ação da pilha após desfazer/refazer


if __name__ == "__main__":
    # Cliente: Cria os objetos Receiver, Command e Invoker, e os configura.

    # Receivers: Dispositivos que recebem e executam as ações
    bedroom_light = Light('Luz do quarto', 'Quarto')
    bathroom_light = Light('Luz do banheiro', 'Banheiro')

    # Concrete Commands: Encapsulam as ações para os Receivers
    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light, 'Blue')
    bedroom_light_red = LightChangeColor(bedroom_light, 'Red')

    # Invoker: O controle remoto que irá disparar os comandos
    remote = RemoteController()

    # Cliente: Configura o Invoker com os comandos
    remote.button_add_command('first_button', bedroom_light_on)
    remote.button_add_command('second_button', bathroom_light_on)
    remote.button_add_command('third_button', bedroom_light_blue)
    remote.button_add_command('fourth_button', bedroom_light_red)

    # Cliente: Invoca as ações através do controle remoto
    print('--- Executando Comandos ---')
    remote.button_pressed('first_button')  # Liga a luz do quarto
    remote.button_undo('first_button')    # Desliga a luz do quarto (desfaz o 'first_button' que ligou)

    remote.button_pressed('second_button')  # Liga a luz do banheiro
    remote.button_undo('second_button')   # Desliga a luz do banheiro

    remote.button_pressed('third_button')   # Muda a cor da luz do quarto para azul
    # remote.button_undo('third_button')    # Se descomentado, mudaria para a cor anterior (Default color)

    remote.button_pressed('fourth_button')  # Muda a cor da luz do quarto para vermelho
    remote.button_undo('fourth_button')   # Volta a cor da luz do quarto para azul (cor anterior)

    print('--- Desfazendo Globalmente ---')
    # Demonstração do undo global, desfazendo as últimas ações na ordem inversa.
    remote.global_undo()  # Desfaz o último 'undo' (o 'fourth_button' que voltou para azul, então refaz a mudança para vermelho)
    remote.global_undo()  # Desfaz o último 'execute' (o 'fourth_button' que mudou para vermelho, então volta para azul)
    remote.global_undo()  # Desfaz o último 'execute' (o 'third_button' que mudou para azul, então volta para a cor padrão)
    remote.global_undo()  # Desfaz o último 'undo' (o 'second_button' que desligou, então liga a luz do banheiro)
    remote.global_undo()  # Desfaz o último 'execute' (o 'second_button' que ligou, então desliga a luz do banheiro)
    remote.global_undo()  # Desfaz o último 'undo' (o 'first_button' que desligou, então liga a luz do quarto)
    remote.global_undo()  # Desfaz o último 'execute' (o 'first_button' que ligou, então desliga a luz do quarto)
    remote.global_undo()  # Nada para desfazer
