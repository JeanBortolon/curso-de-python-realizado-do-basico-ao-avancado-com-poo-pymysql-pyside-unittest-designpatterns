"""
Abstract Factory é um padrão de criação que fornece uma interface para criar
famílias de objetos relacionados ou dependentes sem especificar suas classes
concretas. Geralmente Abstract Factory conta com um ou mais Factory Methods
para criar seus objetos.

Uma diferença importante entre Factory Method e Abstract Factory é que o
Factory Method usa herança, enquanto Abstract Factory usa a composição.

Princípio: programe para interfaces, não para implementações
"""
from abc import ABC, abstractmethod

# PRODUTOS ABSTRATOS
# Estas são as interfaces para as famílias de objetos que queremos criar.
# No nosso caso, temos duas famílias: Veículos de Luxo e Veículos Populares.
# Elas definem o que um objeto "produto" deve ser capaz de fazer, sem se
# preocupar com a implementação.
class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


# PRODUTOS CONCRETOS (FAMÍLIA ZONA NORTE)
# Estas são as implementações reais dos produtos abstratos para uma variante
# específica, neste caso, para a "Zona Norte". Cada classe aqui é um objeto
# real que pode ser criado.
class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZN está buscando o cliente...')


class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZN está buscando o cliente...')


class MotoLuxoZN(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZN está buscando o cliente...')


class MotoPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZN está buscando o cliente...')


# PRODUTOS CONCRETOS (FAMÍLIA ZONA SUL)
# Aqui temos a outra variante dos nossos produtos, para a "Zona Sul".
# Note que as classes seguem as mesmas interfaces (VeiculoLuxo, VeiculoPopular),
# mas a implementação é diferente, refletindo a sua variante.
class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo ZS está buscando o cliente...')


class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular ZS está buscando o cliente...')


class MotoLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo ZS está buscando o cliente...')


class MotoPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Moto popular ZS está buscando o cliente...')


# FÁBRICA ABSTRATA (ABSTRACT FACTORY)
# Esta é a interface da nossa fábrica. Ela declara um conjunto de métodos
# para criar cada um dos produtos abstratos (VeiculoLuxo, VeiculoPopular, etc.).
# O código cliente irá interagir com esta interface, e não com as fábricas
# concretas diretamente.
class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo: pass

    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular: pass

    @staticmethod
    @abstractmethod
    def get_moto_luxo() -> VeiculoLuxo: pass

    @staticmethod
    @abstractmethod
    def get_moto_popular() -> VeiculoPopular: pass


# FÁBRICA CONCRETA 1 (ZONA NORTE)
# Esta é uma implementação da fábrica abstrata. Sua responsabilidade é
# instanciar a família de produtos da "Zona Norte". Cada método aqui retorna
# um veículo concreto específico da ZN.
class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZN()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZN()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZN()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZN()


# FÁBRICA CONCRETA 2 (ZONA SUL)
# Esta é a outra implementação da fábrica, responsável por criar a família
# de produtos da "Zona Sul". Note como ela retorna objetos diferentes da
# fábrica da Zona Norte, mas que seguem as mesmas interfaces.
class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo:
        return CarroLuxoZS()

    @staticmethod
    def get_carro_popular() -> VeiculoPopular:
        return CarroPopularZS()

    @staticmethod
    def get_moto_luxo() -> VeiculoLuxo:
        return MotoLuxoZS()

    @staticmethod
    def get_moto_popular() -> VeiculoPopular:
        return MotoPopularZS()


# CÓDIGO CLIENTE
# O cliente utiliza a fábrica para obter os veículos de que precisa.
# O ponto principal é que o cliente não sabe (e não precisa saber) qual
# fábrica concreta está usando (ZN ou ZS) nem quais classes de veículos
# concretos estão sendo instanciadas. Ele apenas "pede" um tipo de veículo
# (ex: carro popular) e a fábrica se encarrega de entregar o objeto correto
# para aquela família.
class Cliente:
    def buscar_clientes(self) -> None:
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            print(f'--- Usando a fábrica: {factory.__class__.__name__} ---')
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()


# PONTO DE ENTRADA DA APLICAÇÃO
if __name__ == "__main__":
    # O código cliente é instanciado e seu método é chamado para demonstrar
    # o funcionamento do padrão.
    cliente = Cliente()
    cliente.buscar_clientes()
