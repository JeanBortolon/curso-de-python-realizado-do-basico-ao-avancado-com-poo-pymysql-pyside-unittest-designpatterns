"""
GoF - Memento é um padrão de projeto comportamental
que tem a intenção de permitir que você salve e restaure
um estado anterior de um objeto originator sem revelar os
detalhes da sua implementação e sem violar o encapsulamento.

Originator é o objeto que deseja salvar seu estado.
Memento é usado para salvar o estado do Originator.
Caretaker é usado para armazenar mementos.
Caretaker também é usado com o Padrão Command.
"""
from __future__ import annotations
from typing import Dict, List
from copy import deepcopy


# Memento: Armazena o estado interno de um objeto Originator.
# O Memento deve ser imutável para garantir que o estado salvo não seja modificado
# após a sua criação.
class Memento:
    def __init__(self, state: Dict) -> None:
        # O estado é armazenado internamente.
        self._state: Dict
        # Utiliza super().__setattr__ para definir _state, garantindo a imutabilidade
        # uma vez que o método __setattr__ é sobrescrito para levantar um AttributeError.
        super().__setattr__('_state', state)

    def get_state(self) -> Dict:
        # Retorna o estado salvo do Originator.
        return self._state

    def __setattr__(self, name, value):
        # Impede modificações no Memento após a inicialização, tornando-o imutável.
        raise AttributeError('Sorry, I am immutable')


# Originator: É o objeto cujo estado queremos salvar e restaurar.
# Ele cria um memento contendo seu estado atual e usa um memento para restaurar
# um estado anterior.
class ImageEditor:
    def __init__(self, name: str, width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        # Salva o estado atual do ImageEditor em um novo objeto Memento.
        # deepcopy é usado para garantir que o memento contenha uma cópia independente
        # do estado, evitando que alterações futuras no ImageEditor afetem o memento salvo.
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        # Restaura o estado do ImageEditor a partir de um objeto Memento.
        # Sobrescreve o dicionário __dict__ do objeto com o estado salvo.
        self.__dict__ = memento.get_state()

    def __str__(self):
        # Representação em string do objeto ImageEditor.
        return f'{self.__class__.__name__}({self.__dict__})'


# Caretaker: É responsável por armazenar e gerenciar os Mementos.
# Ele nunca opera ou examina o conteúdo de um memento.
class Caretaker:
    def __init__(self, originator: ImageEditor):
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        # Salva o estado atual do Originator (ImageEditor) adicionando um Memento à lista.
        print(f'Caretaker: Saving Originator state...')
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        # Restaura o estado anterior do Originator a partir do último Memento salvo.
        if not self._mementos:
            print('Caretaker: No mementos to restore.')
            return

        memento = self._mementos.pop()
        print(f'Caretaker: Restoring state to: {memento.get_state()}')
        self._originator.restore(memento)


if __name__ == "__main__":
    # Exemplo de uso do padrão Memento.
    img = ImageEditor('FOTO_1.jpg', 111, 111)
    caretaker = Caretaker(img)

    # Backup inicial do estado.
    caretaker.backup()
    print(f'Estado inicial: {img}')

    # Modifica o estado e faz um backup.
    img.name = 'FOTO_2.jpg'
    img.width = 222
    img.height = 222
    caretaker.backup()
    print(f'Estado após primeira modificação: {img}')

    # Modifica o estado novamente e faz outro backup.
    img.name = 'FOTO_3.jpg'
    img.width = 333
    img.height = 333
    caretaker.backup()
    print(f'Estado após segunda modificação: {img}')

    # Modifica o estado sem fazer backup.
    img.name = 'FOTO_4.jpg'
    img.width = 444
    img.height = 444
    print(f'Estado atual (sem backup): {img}')

    # Restaura o estado para a versão 'FOTO_3.jpg'.
    caretaker.restore()
    print(f'Estado restaurado (FOTO_3.jpg): {img}')

    # Restaura o estado para a versão 'FOTO_2.jpg'.
    caretaker.restore()
    print(f'Estado restaurado (FOTO_2.jpg): {img}')

    # Restaura o estado para a versão 'FOTO_1.jpg'.
    caretaker.restore()
    print(f'Estado restaurado (FOTO_1.jpg): {img}')

    # Tenta restaurar sem mementos disponíveis.
    caretaker.restore()
    print(f'Tentativa de restaurar sem mementos: {img}')
