"""
Adapter é um padrão de projeto estrutural que
tem a intenção de permitir que duas classes
que seriam incompatíveis trabalhem em conjunto
através de um "adaptador".
"""
from abc import ABC, abstractmethod


class IControl(ABC):
    """
    Interface Alvo (Target Interface): Define a interface que o cliente espera usar.
    As classes adaptadoras devem implementar esta interface.
    """
    @abstractmethod
    def top(self) -> None: pass

    @abstractmethod
    def right(self) -> None: pass

    @abstractmethod
    def down(self) -> None: pass

    @abstractmethod
    def left(self) -> None: pass


class Control(IControl):
    """
    Implementação Concreta do Alvo: Uma classe que implementa a Interface Alvo.
    É o que o cliente já sabe usar.
    """
    def top(self) -> None:
        print('Movendo para cima...')

    def right(self) -> None:
        print('Movendo para direita...')

    def down(self) -> None:
        print('Movendo para baixo...')

    def left(self) -> None:
        print('Movendo para esquerda...')


class NewControl:
    """
    Adaptado (Adaptee): Uma classe existente com uma interface incompatível
    que precisa ser adaptada para trabalhar com a Interface Alvo.
    """
    def move_top(self) -> None: # Método equivalente ao 'top' da interface IControl
        print('NewControl: Movendo para cima...')

    def move_right(self) -> None: # Método equivalente ao 'right' da interface IControl
        print('NewControl: Movendo para direita...')

    def move_down(self) -> None: # Método equivalente ao 'down' da interface IControl
        print('NewControl: Movendo para baixo...')

    def move_left(self) -> None: # Método equivalente ao 'left' da interface IControl
        print('NewControl: Movendo para esquerda...')


class ControlAdapter(IControl): # O Adaptador (ControlAdapter) implementa a interface do Alvo (IControl)
    """
    Adaptador (Object Adapter): Adapta a interface do Adaptado (NewControl) para a interface do Alvo (IControl).
    Este é um "Adapter de Objeto", pois o adaptador COMPÕE o objeto adaptado.
    """

    def __init__(self, new_control: NewControl) -> None:
        # O adaptador mantém uma referência ao objeto Adaptado.
        self.new_control = new_control

    def top(self) -> None: # Implementa o método 'top' da IControl
        self.new_control.move_top() # Delega a chamada ao método 'move_top' do Adaptado

    def right(self) -> None: # Implementa o método 'right' da IControl
        self.new_control.move_right() # Delega a chamada ao método 'move_right' do Adaptado

    def down(self) -> None: # Implementa o método 'down' da IControl
        self.new_control.move_down() # Delega a chamada ao método 'move_down' do Adaptado

    def left(self) -> None: # Implementa o método 'left' da IControl
        self.new_control.move_left() # Delega a chamada ao método 'move_left' do Adaptado


class ControlAdapter2(Control, NewControl): # O Adaptador (ControlAdapter2) herda da interface do Alvo (Control) e do Adaptado (NewControl)
    """
    Adaptador (Class Adapter): Adapta a interface do Adaptado (NewControl) para a interface do Alvo (Control).
    Este é um "Adapter de Classe", pois o adaptador herda tanto do alvo quanto do adaptado.
    Note que, em Python, a herança múltipla permite isso de forma mais direta, mas exige cuidado.
    """

    def top(self) -> None: # Implementa o método 'top' da Control (que herda de IControl)
        self.move_top() # Chama o método 'move_top' do NewControl (também herdado)

    def right(self) -> None: # Implementa o método 'right'
        self.move_right() # Chama o método 'move_right' do NewControl

    def down(self) -> None: # Implementa o método 'down'
        self.move_down() # Chama o método 'move_down' do NewControl

    def left(self) -> None: # Implementa o método 'left'
        self.move_left() # Chama o método 'move_left' do NewControl


if __name__ == "__main__":
    # Control - Adapter Object
    new_control = NewControl()
    control_object = ControlAdapter(new_control)

    control_object.top()
    control_object.down()
    control_object.left()
    control_object.right()

    print()
    # Control - Adapter class
    control_class = ControlAdapter2()

    control_class.top()
    control_class.down()
    control_class.left()
    control_class.right()
