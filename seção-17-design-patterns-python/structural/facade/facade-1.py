"""
Façade (Fachada) é um padrão de projeto estrutural
que tem a intenção de fornecer uma interface
unificada para um conjunto de interfaces em um
subsistema. Façade define uma interface de nível
mais alto que torna o subsistema mais fácil de ser
usado.

Neste exemplo, a `WeatherStationFacade` atua como uma fachada
para o subsistema de monitoramento de clima, que inclui
a estação meteorológica (`WeatherStation`) e os dispositivos
que observam seus dados (`Smartphone`, `Notebook`).
A fachada simplifica a interação com a complexidade
de adicionar/remover observadores e atualizar o estado da estação.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObservable(ABC):
    """
    Interface para o objeto Observável (Subject).
    Define os métodos para adicionar, remover e notificar observadores.
    """

    @property
    @abstractmethod
    def state(self):
        """ Retorna o estado atual do Observável. """
        pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None:
        """ Adiciona um observador à lista. """
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None:
        """ Remove um observador da lista. """
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        """ Notifica todos os observadores sobre uma mudança de estado. """
        pass


class WeatherStation(IObservable):
    """
    Observável concreto (Estação Meteorológica).
    Armazena o estado do clima e notifica os observadores quando ele muda.
    """

    def __init__(self) -> None:
        # Lista de observadores que estão interessados nas atualizações do clima.
        self._observers: List[IObserver] = []
        # O estado atual da estação meteorológica (ex: temperatura, umidade).
        self._state: Dict = {}

    @property
    def state(self) -> Dict:
        """ Getter para o estado da estação meteorológica. """
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        """
        Setter para o estado da estação meteorológica.
        Quando o estado é atualizado, notifica os observadores se houver mudança real.
        """
        # Cria um novo estado mesclando o estado atual com as atualizações recebidas.
        new_state: Dict = {**self._state, **state_update}

        # Verifica se o novo estado é diferente do estado anterior.
        if new_state != self._state:
            self._state = new_state  # Atualiza o estado interno.
            self.notify_observers()  # Notifica os observadores.

    def reset_state(self) -> None:
        """ Reseta o estado da estação meteorológica e notifica os observadores. """
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        """ Adiciona um observador à lista de observadores. """
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        """ Remove um observador da lista, se ele estiver presente. """
        if observer not in self._observers:
            return
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        """
        Itera sobre todos os observadores e chama o método update() de cada um,
        informando-os sobre a mudança no estado.
        """
        for observer in self._observers:
            observer.update()
        print()  # Adiciona uma linha em branco para melhor visualização.


class IObserver(ABC):
    """
    Interface para o objeto Observador.
    Define o método `update` que será chamado quando o Observável mudar de estado.
    """
    @abstractmethod
    def update(self) -> None:
        """
        Método a ser implementado pelos observadores para reagir às mudanças
        no Observável.
        """
        pass


class Smartphone(IObserver):
    """
    Observador concreto: Um smartphone que exibe as atualizações da estação meteorológica.
    """

    def __init__(self, name: str, observable: IObservable) -> None:
        self.name = name  # Nome do smartphone (ex: iPhone).
        self.observable = observable  # A estação meteorológica que ele está observando.

    def update(self) -> None:
        """
        Implementa o método update: quando notificado, o smartphone imprime
        o novo estado da estação meteorológica.
        """
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} '
              f'acabou de ser atualizado => {self.observable.state}')


class Notebook(IObserver):
    """
    Observador concreto: Um notebook que pode processar as atualizações
    da estação meteorológica de uma maneira diferente.
    """

    def __init__(self, observable: IObservable) -> None:
        self.observable = observable  # A estação meteorológica que ele está observando.

    def show(self) -> None:
        """ Um método específico do notebook para manipular os dados. """
        state = self.observable.state
        print('Sou o note e vou fazer outra coisa com esses dados', state)

    def update(self) -> None:
        """
        Implementa o método update: quando notificado, o notebook chama seu
        método `show` para processar os dados.
        """
        self.show()


class WeatherStationFacade:
    """
    Aqui está nossa fachada.
    Ela fornece uma interface simplificada para o subsistema da estação meteorológica,
    escondendo a complexidade da interação direta com a `WeatherStation` e seus observadores.
    """

    def __init__(self) -> None:
        # A fachada inicializa o Observável principal.
        self.weather_station = WeatherStation()

        # A fachada também pode inicializar e gerenciar os Observadores.
        self.smartphone = Smartphone('iPhone', self.weather_station)
        self.outro_smartphone = Smartphone(
            'Outro Smartphone', self.weather_station)
        self.notebook = Notebook(self.weather_station)

        # Adiciona os observadores à estação meteorológica através da fachada.
        self.weather_station.add_observer(self.smartphone)
        self.weather_station.add_observer(self.outro_smartphone)
        self.weather_station.add_observer(self.notebook)

    def add_observer(self, observer: IObserver) -> None:
        """
        Método simplificado da fachada para adicionar um observador.
        Delega a chamada para o objeto `weather_station` interno.
        """
        self.weather_station.add_observer(observer)

    def remove_observer(self, observer: IObserver) -> None:
        """
        Método simplificado da fachada para remover um observador.
        Delega a chamada para o objeto `weather_station` interno.
        """
        self.weather_station.remove_observer(observer)

    def change_state(self, state: Dict) -> None:
        """
        Método simplificado da fachada para mudar o estado da estação.
        Delega a chamada para o setter `state` da `weather_station`,
        que por sua vez notificará os observadores.
        """
        self.weather_station.state = state

    def remove_smartphone(self) -> None:
        """
        Exemplo de método específico da fachada para remover um observador
        pré-definido (o smartphone 'iPhone').
        """
        self.weather_station.remove_observer(self.smartphone)

    def reset_state(self) -> None:
        """
        Método simplificado da fachada para resetar o estado da estação.
        Delega a chamada para o objeto `weather_station` interno.
        """
        self.weather_station.reset_state()


if __name__ == "__main__":
    # --- Demonstração do uso da Facade ---

    # Instancia a fachada, que por sua vez inicializa a estação e os observadores.
    print('Criando a fachada e inicializando observadores...')
    weather_station_facade = WeatherStationFacade()
    print('-' * 30)

    # Usa a fachada para mudar o estado, sem precisar interagir diretamente
    # com os detalhes da `WeatherStation` ou dos Observadores.
    print('Alterando o estado da estação via fachada (temperatura: 30)...')
    weather_station_facade.change_state({'temperature': '30'})
    print('Alterando o estado da estação via fachada (temperatura: 32)...')
    weather_station_facade.change_state({'temperature': '32'})
    print('Alterando o estado da estação via fachada (umidade: 90)...')
    weather_station_facade.change_state({'humidity': '90'})
    print('-' * 30)

    # Demonstra a remoção de um observador através da fachada.
    print('Removendo o smartphone "iPhone" via fachada...')
    weather_station_facade.remove_smartphone()
    print('-' * 30)

    # Demonstra o reset do estado da estação através da fachada.
    print('Resetando o estado da estação via fachada...')
    weather_station_facade.reset_state()
    print('-' * 30)

    # Novas mudanças de estado após a remoção de um observador e reset.
    # O smartphone 'iPhone' não será mais notificado.
    print('Novamente alterando o estado da estação via fachada (temperatura: 30)...')
    weather_station_facade.change_state({'temperature': '30'})
    print('Novamente alterando o estado da estação via fachada (temperatura: 32)...')
    weather_station_facade.change_state({'temperature': '32'})
    print('Novamente alterando o estado da estação via fachada (umidade: 90)...')
    weather_station_facade.change_state({'humidity': '90'})
    print('-' * 30)
