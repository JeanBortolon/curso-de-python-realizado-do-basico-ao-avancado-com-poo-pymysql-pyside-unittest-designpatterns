"""
Bridge é um padrão de projeto estrutural que
tem a intenção de desacoplar uma abstração
da sua implementação, de modo que as duas
possam variar e evoluir independentemente.

Abstração é uma camada de alto nível para algo.
Geralmente, a abstração não faz nenhum trabalho
por conta própria, ela delega parte ou todo o
trabalho para a camada de implementação.

RELEMBRANDO: Adapter é um padrão de projeto
estrutural que tem a intenção de permitir
que duas classes que seriam incompatíveis
trabalhem em conjunto através de um "adaptador".

Diferença (GOF pag. 208) - A diferença chave
entre esses padrões está nas suas intenções...
...O padrão Adapter faz as coisas funcionarem
APÓS elas terem sido projetadas; o Bridge as
faz funcionar ANTES QUE existam...
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class IRemoteControl(ABC):
    # Esta é a interface (Abstração) para o controle remoto.
    # Ela define as operações de alto nível que um controle remoto pode realizar,
    # sem se preocupar com os detalhes da implementação do dispositivo subjacente.
    @abstractmethod
    def increase_volume(self) -> None: pass

    @abstractmethod
    def decrease_volume(self) -> None: pass

    @abstractmethod
    def power(self) -> None: pass


class RemoteControl(IRemoteControl):
    # RemoteControl é a Abstração concreta.
    # Ela contém uma referência para um objeto IDevice (Implementador)
    # e delega as operações a ele.
    def __init__(self, device: IDevice) -> None:
        self._device = device # O device é a implementação

    def increase_volume(self) -> None:
        self._device.volume += 10 # Delega para o device

    def decrease_volume(self) -> None:
        self._device.volume -= 10 # Delega para o device

    def power(self) -> None:
        self._device.power = not self._device.power # Delega para o device


class RemoteControlWithMute(RemoteControl):
    # RemoteControlWithMute é uma Abstração refinada.
    # Ela estende a funcionalidade do RemoteControl adicionando um método 'mute'.
    # A adição de novas funcionalidades na Abstração não afeta a Implementação.
    def mute(self) -> None:
        self._device.volume = 0 # Delega para o device, sem alterar o device em si.


class IDevice(ABC):
    # Esta é a interface Implementadora.
    # Ela declara a interface para os objetos de implementação.
    # Não precisa corresponder à interface da Abstração.
    # Na verdade, as duas interfaces podem ser bem diferentes.
    # Normalmente, a interface Implementadora fornece apenas operações primitivas,
    # e a Abstração define operações de nível superior com base nessas primitivas.
    @property
    @abstractmethod
    def volume(self) -> int: pass

    @volume.setter
    def volume(self, volume: int) -> None: pass

    @property
    @abstractmethod
    def power(self) -> bool: pass

    @power.setter
    def power(self, power: bool) -> None: pass


class TV(IDevice):
    # TV é uma Implementação concreta de IDevice.
    # Ela implementa a interface Implementadora e define suas próprias operações.
    def __init__(self) -> None:
        self._volume = 10
        self._power = False
        self._name = self.__class__.__name__

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int) -> None:
        if not self.power:
            print(f'Please, turn {self._name} ON')
            return

        if volume > 100:
            return

        if volume < 0:
            return

        self._volume = volume
        print(f'Volume is now {self._volume}')

    @property
    def power(self) -> bool:
        return self._power

    @power.setter
    def power(self, power: bool) -> None:
        self._power = power
        power_status = 'ON' if self._power else 'OFF'

        print(f'{self._name} is now {power_status}')


class Radio(TV):
    # Radio é outra Implementação concreta, demonstrando que novas implementações
    # podem ser adicionadas sem alterar a hierarquia de Abstração.
    ...


if __name__ == "__main__":
    # Cria instâncias de dispositivos (implementações concretas)
    tv = TV()
    radio = Radio()

    # Cria um controle remoto (abstração) e o vincula a um dispositivo (implementação).
    # O RemoteControl não precisa saber os detalhes de como a TV funciona.
    remote = RemoteControl(tv)

    # O controle remoto pode operar o dispositivo através de sua interface abstrata.
    remote.increase_volume() # Tenta aumentar volume, mas a TV está desligada.
    remote.power()           # Liga a TV
    remote.increase_volume() # Aumenta volume
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.power()           # Desliga a TV
    remote.increase_volume() # Tenta aumentar volume, mas a TV está desligada.
    remote.power()           # Liga a TV
    remote.decrease_volume() # Diminui volume
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()

    print()
    # Cria um controle remoto com mute (abstração refinada) e o vincula ao rádio.
    # O RemoteControlWithMute não precisa saber os detalhes de como o Rádio funciona.
    remote = RemoteControlWithMute(radio)

    # Demonstra as operações básicas e a funcionalidade extra de mute.
    remote.increase_volume()
    remote.power()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.increase_volume()
    remote.power()
    remote.increase_volume()
    remote.power()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    remote.decrease_volume()
    print('MUTE')
    remote.mute() # Silencia o rádio.
