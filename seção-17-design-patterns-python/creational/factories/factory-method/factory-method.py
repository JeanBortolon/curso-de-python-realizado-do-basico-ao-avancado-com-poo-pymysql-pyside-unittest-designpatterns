"""
Factory method é um padrão de criação que permite definir uma interface para
criar objetos, mas deixa as subclasses decidirem quais objetos criar. O
Factory method permite adiar a instanciação para as subclasses, garantindo o
baixo acoplamento entre classes.
"""
from abc import ABC, abstractmethod

# PASSO 1: Definir a Interface do Produto (Veiculo)
# Esta é uma classe abstrata que define o "contrato" que todos os
# objetos (produtos) criados pela fábrica devem seguir.
class Veiculo(ABC):
    # O método abstrato que as subclasses (produtos concretos) devem implementar.
    @abstractmethod
    def buscar_cliente(self) -> None: pass


# PASSO 2: Criar os Produtos Concretos (CarroLuxo, CarroPopular, etc.)
# Estas são as classes que realmente implementam a interface do produto.
# Cada uma representa uma variação do objeto que a fábrica pode criar.
class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente...')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular está buscando o cliente...')


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo está buscando o cliente...')


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto popular está buscando o cliente...')


# PASSO 3: Definir a Fábrica Abstrata (Creator)
# Esta classe define a interface para as fábricas. Contém o "Factory Method",
# que é um método abstrato para criar objetos (produtos).
class VeiculoFactory(ABC):
    # O construtor recebe o tipo de veículo e chama o factory method
    # para criar e armazenar o objeto do veículo.
    def __init__(self, tipo) -> None:
        self.carro = self.get_carro(tipo)

    # Este é o "Factory Method". É estático e abstrato.
    # As subclasses (fábricas concretas) são obrigadas a implementar este método,
    # decidindo COMO criar o objeto.
    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo: pass

    # Este método delega a chamada para o objeto de veículo que foi criado.
    # O cliente interage com a fábrica, que por sua vez usa o produto.
    def buscar_cliente(self) -> None:
        self.carro.buscar_cliente()


# PASSO 4: Criar as Fábricas Concretas (Concrete Creators)
# Cada fábrica concreta herda da fábrica abstrata e implementa o factory method
# para criar um conjunto específico de produtos.
# Esta fábrica atende a "Zona Norte" e pode criar todos os tipos de veículos.
class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        # A lógica para decidir qual objeto instanciar.
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return MotoPopular()
        if tipo == 'moto_luxo':
            return MotoLuxo()
        # Lança um erro se o tipo não for reconhecido.
        assert 0, 'Veículo não existe'


# Esta é outra fábrica concreta. Ela atende a "Zona Sul" e tem uma
# oferta limitada de veículos (apenas carros populares).
class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        # A lógica de criação aqui é diferente da Zona Norte.
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veículo não existe'


if __name__ == "__main__":
    # PASSO 5: Código Cliente
    # O cliente usa as fábricas para obter veículos, sem precisar saber
    # as classes concretas dos veículos (CarroLuxo, etc.).
    # O código cliente depende das abstrações (VeiculoFactory, Veiculo),
    # não das implementações concretas.
    from random import choice
    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto', 'moto_luxo']
    veiculos_disponiveis_zona_sul = ['popular']

    print('ZONA NORTE')
    for i in range(10):
        # Usa a fábrica da Zona Norte para criar um veículo aleatório.
        carro = ZonaNorteVeiculoFactory(
            choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

    print()

    print('ZONA SUL')
    for i in range(10):
        # Usa a fábrica da Zona Sul. Note que o cliente não se importa
        # com as regras internas da fábrica, apenas pede um veículo.
        carro2 = ZonaSulVeiculoFactory(
            choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()
