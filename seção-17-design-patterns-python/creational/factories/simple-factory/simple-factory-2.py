"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID
"""
from abc import ABC, abstractmethod


# Define uma classe abstrata (Interface) 'Veiculo'.
# Todas as classes de veículos concretos devem herdar desta classe
# e implementar seus métodos abstratos.
class Veiculo(ABC):
    # Define um método abstrato que as subclasses serão obrigadas a implementar.
    # Este é o "contrato" que todos os veículos devem seguir.
    @abstractmethod
    def buscar_cliente(self) -> None: pass


# Classe concreta que representa um tipo de veículo (Produto).
class CarroLuxo(Veiculo):
    # Implementação específica do método para CarroLuxo.
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente...')


# Classe concreta que representa outro tipo de veículo.
class CarroPopular(Veiculo):
    # Implementação específica do método para CarroPopular.
    def buscar_cliente(self) -> None:
        print('Carro popular está buscando o cliente...')


# Classe concreta que representa outro tipo de veículo.
class MotoLuxo(Veiculo):
    # Implementação específica do método para MotoLuxo.
    def buscar_cliente(self) -> None:
        print('Moto está buscando o cliente...')


# Classe concreta que representa outro tipo de veículo.
class MotoPopular(Veiculo):
    # Implementação específica do método para MotoPopular.
    def buscar_cliente(self) -> None:
        print('Moto popular está buscando o cliente...')


# Esta é a classe Factory (Fábrica).
# Nesta versão, a própria fábrica é instanciada e atua como um invólucro
# para o objeto do veículo criado.
class VeiculoFactory:
    # O construtor da fábrica. Ele recebe o tipo de veículo desejado.
    def __init__(self, tipo) -> None:
        # Ao criar uma instância da fábrica, o método 'get_carro' é chamado
        # para criar e armazenar o objeto de veículo apropriado na variável 'self.carro'.
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        # Este método estático centraliza a lógica de criação de objetos.
        # Com base no parâmetro 'tipo', ele decide qual classe concreta instanciar.
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return MotoPopular()
        # Se um tipo de veículo inválido for solicitado, uma exceção AssertionError é levantada.
        assert 0, 'Veículo não existe'

    # Este método delega a chamada para o método 'buscar_cliente' do objeto de veículo
    # que foi criado e armazenado em 'self.carro'.
    def buscar_cliente(self) -> None:
        self.carro.buscar_cliente()


if __name__ == "__main__":
    from random import choice
    # Lista de tipos de veículos disponíveis que a fábrica pode criar.
    carros_disponiveis = ['luxo', 'popular', 'moto'] # 'moto_luxo' foi removido da lista de disponíveis

    # Simula a solicitação de 10 veículos de forma aleatória.
    for i in range(10):
        # O cliente (este código) cria uma instância da fábrica, passando o tipo de veículo.
        # A fábrica, por sua vez, cria o objeto de veículo internamente.
        carro = VeiculoFactory(choice(carros_disponiveis))
        # O cliente chama o método na instância da fábrica, que delega a ação para o veículo real.
        carro.buscar_cliente()
