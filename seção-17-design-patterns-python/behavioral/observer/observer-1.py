"""
O padrão Observer tem a intenção de
definir uma dependência de um-para-muitos entre
objetos, de maneira que quando um objeto muda de
estado, todo os seus dependentes são notificados
e atualizados automaticamente.

Um observer é um objeto que gostaria de ser
informado, um observable (subject) é a entidade
que gera as informações.

Neste exemplo, a WeatherStation (estação meteorológica) é o Observable (sujeito)
e os dispositivos como Smartphone e Notebook são os Observers (observadores).
Quando o estado da WeatherStation muda (ex: temperatura ou umidade),
todos os dispositivos registrados são notificados e atualizados.
"""
from __future__ import annotations # Permite o uso de anotações de tipo de classe futura
from abc import ABC, abstractmethod # Módulos para definir classes abstratas e métodos abstratos
from typing import List, Dict # Tipos para listas e dicionários

# Interface (ABC) para o Objeto Observável (Subject)
class IObservable(ABC):
    """
    Interface abstrata para o Objeto Observável (Subject).
    Define os métodos que um sujeito deve implementar para permitir que observadores
    se registrem, desregistrem e sejam notificados sobre mudanças de estado.
    """

    @property # Decorador para definir um método como propriedade (getter)
    @abstractmethod # Marca o método como abstrato, exigindo implementação em subclasses concretas
    def state(self):
        """
        Propriedade abstrata que representa o estado atual do Observável.
        Deve ser implementada para retornar o estado.
        """
        pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None:
        """
        Método abstrato para adicionar um observador à lista de dependentes.
        :param observer: O objeto observador a ser adicionado.
        """
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None:
        """
        Método abstrato para remover um observador da lista de dependentes.
        :param observer: O objeto observador a ser removido.
        """
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        """
        Método abstrato para notificar todos os observadores registrados
        sobre uma mudança de estado.
        """
        pass

# Implementação Concreta do Observável (Subject)
class WeatherStation(IObservable):
    """
    Estação Meteorológica Concreta, atua como o Observável (Subject).
    Mantém uma lista de observadores e os notifica quando seu estado (dados meteorológicos) muda.
    """

    def __init__(self) -> None:
        """
        Inicializa a WeatherStation.
        Cria uma lista vazia para armazenar os observadores e um dicionário
        para o estado atual (ex: temperatura, umidade).
        """
        self._observers: List[IObserver] = [] # Lista para armazenar os observadores
        self._state: Dict = {} # Dicionário para o estado atual da estação

    @property
    def state(self) -> Dict:
        """
        Getter para a propriedade 'state'. Retorna o estado atual da estação.
        """
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        """
        Setter para a propriedade 'state'.
        Atualiza o estado da estação e notifica os observadores se o estado realmente mudou.
        :param state_update: Um dicionário contendo as atualizações para o estado.
        """
        # Combina o estado existente com as novas atualizações
        new_state: Dict = {**self._state, **state_update}

        # Verifica se o novo estado é diferente do estado anterior
        if new_state != self._state:
            self._state = new_state # Atualiza o estado interno
            self.notify_observers() # Notifica todos os observadores

    def reset_state(self) -> None:
        """
        Redefine o estado da estação para um dicionário vazio e notifica os observadores.
        """
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        """
        Adiciona um observador à lista de observadores.
        :param observer: O objeto observador a ser adicionado.
        """
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        """
        Remove um observador da lista de observadores.
        :param observer: O objeto observador a ser removido.
        """
        # Verifica se o observador está na lista antes de tentar removê-lo
        if observer not in self._observers:
            return

        self._observers.remove(observer)

    def notify_observers(self) -> None:
        """
        Percorre todos os observadores registrados e chama o método 'update' de cada um.
        """
        for observer in self._observers:
            observer.update()
        print() # Apenas para formatação da saída

# Interface (ABC) para o Objeto Observador (Observer)
class IObserver(ABC):
    """
    Interface abstrata para o Objeto Observador (Observer).
    Define o método 'update' que os observadores devem implementar
    para reagir às notificações do sujeito.
    """
    @abstractmethod
    def update(self) -> None:
        """
        Método abstrato chamado pelo Observável para notificar o observador
        sobre uma mudança de estado.
        """
        pass

# Implementação Concreta do Observador
class Smartphone(IObserver):
    """
    Um dispositivo Smartphone, atua como um Observador Concreto.
    Ele é atualizado quando o estado do Observável (WeatherStation) muda.
    """
    def __init__(self, name: str, observable: IObservable) -> None:
        """
        Inicializa o Smartphone.
        :param name: O nome do smartphone (ex: 'iPhone').
        :param observable: A instância do Observável que este smartphone observará.
        """
        self.name = name
        self.observable = observable # Mantém uma referência ao observável

    def update(self) -> None:
        """
        Implementação do método 'update' da interface IObserver.
        É chamado quando o estado do Observável muda.
        Neste caso, imprime o nome do smartphone, o nome do observável
        e o estado atual do observável.
        """
        observable_name = self.observable.__class__.__name__ # Obtém o nome da classe do observável
        print(f'{self.name} o objeto {observable_name} '
              f'acabou de ser atualizado => {self.observable.state}')

# Outra Implementação Concreta do Observador
class Notebook(IObserver):
    """
    Um dispositivo Notebook, atua como outro Observador Concreto.
    Demonstra que observadores podem ter lógicas de atualização diferentes.
    """
    def __init__(self, observable: IObservable) -> None:
        """
        Inicializa o Notebook.
        :param observable: A instância do Observável que este notebook observará.
        """
        self.observable = observable # Mantém uma referência ao observável

    def show(self) -> None:
        """
        Método específico do Notebook para processar e exibir os dados do estado.
        """
        state = self.observable.state # Pega o estado atual do observável
        print('Sou o note e vou fazer outra coisa com esses dados', state)

    def update(self) -> None:
        """
        Implementação do método 'update' da interface IObserver para o Notebook.
        Chama o método 'show' para processar a atualização.
        """
        self.show()

# Bloco principal de execução para demonstrar o padrão Observer
if __name__ == "__main__":
    # 1. Cria o Observável (Subject)
    weather_station = WeatherStation()

    # 2. Cria os Observadores (Observers)
    smartphone = Smartphone('iPhone', weather_station)
    outro_smartphone = Smartphone('Outro Smartphone', weather_station)
    notebook = Notebook(weather_station)

    # 3. Registra os Observadores no Observável
    print('Registrando observadores...')
    weather_station.add_observer(smartphone)
    weather_station.add_observer(outro_smartphone)
    weather_station.add_observer(notebook)
    print('Observadores registrados.\n')

    # 4. Altera o estado do Observável, o que dispara as notificações
    print('Alterando estado: temperatura para 30')
    weather_station.state = {'temperature': '30'} # Notifica todos os observadores
    print('Alterando estado: temperatura para 32')
    weather_station.state = {'temperature': '32'} # Notifica novamente
    print('Alterando estado: umidade para 90')
    weather_station.state = {'humidity': '90'} # Notifica, combinando com a temperatura existente

    # 5. Remove um observador e altera o estado novamente
    print('Removendo "Outro Smartphone" dos observadores.')
    weather_station.remove_observer(outro_smartphone)
    print('Redefinindo o estado da estação (espera-se que "Outro Smartphone" não seja notificado).')
    weather_station.reset_state() # Redefine e notifica os observadores restantes
