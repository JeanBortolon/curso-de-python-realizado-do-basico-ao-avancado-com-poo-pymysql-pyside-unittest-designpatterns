"""
Exemplo de implementação do padrão de projeto State (Estado).

O padrão State permite que um objeto altere seu comportamento
quando seu estado interno muda. O objeto parecerá mudar sua classe.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


# O Contexto define a interface de interesse para os clientes. Ele também
# mantém uma referência para uma instância de uma subclasse State, que
# representa o estado atual do Contexto.
class Sound:
    """
    Contexto: A classe Sound é o contexto que mantém uma referência
    ao objeto de estado atual e delega a ele as requisições específicas do estado.
    """
    def __init__(self) -> None:
        """
        Inicializa o Sound com um estado inicial (RadioMode) e um valor de reprodução.
        """
        # O estado inicial do Contexto é definido aqui.
        self.mode: PlayMode = RadioMode(self)
        self.playing = 0

    def change_mode(self, mode: PlayMode) -> None:
        """
        Permite que o Contexto mude seu objeto de estado.
        Isso é o que permite ao objeto Sound mudar seu comportamento.
        """
        print(f'Mudando para mode: {mode.__class__.__name__}')
        self.playing = 0  # Reseta o valor ao mudar o modo, para demonstração.
        self.mode = mode

    def press_next(self) -> None:
        """
        Delega a funcionalidade de "próximo" para o objeto de estado atual.
        O comportamento real é determinado pela classe de estado específica.
        """
        self.mode.press_next()
        print(self)

    def press_prev(self) -> None:
        """
        Delega a funcionalidade de "anterior" para o objeto de estado atual.
        O comportamento real é determinado pela classe de estado específica.
        """
        self.mode.press_prev()
        print(self)

    def __str__(self) -> str:
        """
        Retorna a representação em string do valor 'playing'.
        """
        return str(self.playing)


# A interface State declara métodos específicos do estado. Esses métodos
# devem ser implementados por todas as Concrete State.
class PlayMode(ABC):
    """
    State (Estado): A interface PlayMode declara os métodos que todos os
    Estados Concretos devem implementar. Ela também fornece uma referência de
    volta para o objeto Contexto, caso os Estados precisem interagir com ele.
    """
    def __init__(self, sound: Sound) -> None:
        """
        O Estado recebe o objeto Contexto através do seu construtor.
        """
        self.sound = sound

    @abstractmethod
    def press_next(self) -> None:
        """
        Método abstrato para avançar a reprodução.
        """
        pass

    @abstractmethod
    def press_prev(self) -> None:
        """
        Método abstrato para retroceder a reprodução.
        """
        pass


# Concrete States implementam vários comportamentos específicos de estado.
class RadioMode(PlayMode):
    """
    Concrete State (Estado Concreto): Implementa o comportamento para o
    estado "Rádio". Neste estado, 'next' e 'prev' ajustam o valor em 1000.
    """
    def press_next(self) -> None:
        """
        No modo Rádio, "próximo" incrementa o valor 'playing' em 1000.
        """
        self.sound.playing += 1000

    def press_prev(self) -> None:
        """
        No modo Rádio, "anterior" decrementa o valor 'playing' em 1000,
        mas não permite que seja menor que zero.
        """
        self.sound.playing -= 1000 if self.sound.playing > 0 else 0


class MusicMode(PlayMode):
    """
    Concrete State (Estado Concreto): Implementa o comportamento para o
    estado "Música". Neste estado, 'next' e 'prev' ajustam o valor em 1.
    """
    def press_next(self) -> None:
        """
        No modo Música, "próximo" incrementa o valor 'playing' em 1.
        """
        self.sound.playing += 1

    def press_prev(self) -> None:
        """
        No modo Música, "anterior" decrementa o valor 'playing' em 1,
        mas não permite que seja menor que zero.
        """
        self.sound.playing -= 1 if self.sound.playing > 0 else 0


if __name__ == "__main__":
    # O código do cliente funciona com o Contexto (Sound) em vez de
    # lidar diretamente com os objetos State. Isso permite que o Contexto
    # decida qual Estado é apropriado com base em seu estado interno.
    sound = Sound()

    print("--- Modo Rádio ---")
    sound.press_next()  # Deveria ser 1000
    sound.press_next()  # Deveria ser 2000
    sound.press_next()  # Deveria ser 3000
    sound.press_next()  # Deveria ser 4000
    sound.press_prev()  # Deveria ser 3000
    sound.press_prev()  # Deveria ser 2000
    sound.press_prev()  # Deveria ser 1000
    sound.press_prev()  # Deveria ser 0
    sound.press_prev()  # Deveria ser 0 (não vai abaixo de zero)
    sound.press_prev()  # Deveria ser 0
    sound.press_prev()  # Deveria ser 0

    print("\n--- Mudando para Modo Música ---")
    # O Contexto muda seu estado, o que altera o comportamento subsequente.
    sound.change_mode(MusicMode(sound))
    sound.press_next()  # Deveria ser 1
    sound.press_next()  # Deveria ser 2
    sound.press_next()  # Deveria ser 3
    sound.press_next()  # Deveria ser 4
    sound.press_prev()  # Deveria ser 3
    sound.press_prev()  # Deveria ser 2
    sound.press_prev()  # Deveria ser 1
    sound.press_prev()  # Deveria ser 0
    sound.press_prev()  # Deveria ser 0 (não vai abaixo de zero)
    sound.press_prev()  # Deveria ser 0
    sound.press_prev()  # Deveria ser 0
    sound.press_prev()  # Deveria ser 0
