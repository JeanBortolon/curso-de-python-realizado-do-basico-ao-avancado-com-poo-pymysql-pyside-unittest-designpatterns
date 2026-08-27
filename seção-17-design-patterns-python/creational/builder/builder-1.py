"""
Builder é um padrão de criação que tem a intenção
de separar a construção de um objeto complexo
da sua representação, de modo que o mesmo processo
de construção possa criar diferentes representações.

Builder te da a possibilidade de criar objetos passo-a-passo
e isso já é possível no Python sem este padrão.

Geralmente o builder aceita o encadeamento de métodos
(method chaining).
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Mixin para fornecer uma representação de string formatada para objetos
class StringReprMixin:
    def __str__(self) -> str:
        # Cria uma string com os atributos e seus valores do objeto
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        # Retorna a mesma representação de __str__
        return self.__str__()


# Classe que representa o objeto complexo a ser construído
class User(StringReprMixin):
    def __init__(self) -> None:
        # Inicializa os atributos do usuário como None ou listas vazias
        self.firstname = None
        self.lastname = None
        self.age = None
        self.phone_numbers: List = []
        self.addresses: List = []


# Interface Abstrata para o Builder de Usuário
class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self) -> User:
        # Propriedade abstrata que deve retornar o objeto User construído
        pass

    @abstractmethod
    def add_firstname(self, firstname) -> 'UserBuilder':
        # Método abstrato para adicionar o primeiro nome
        pass

    @abstractmethod
    def add_lastname(self, lastname) -> 'UserBuilder':
        # Método abstrato para adicionar o sobrenome
        pass

    @abstractmethod
    def add_age(self, age) -> 'UserBuilder':
        # Método abstrato para adicionar a idade
        pass

    @abstractmethod
    def add_phone(self, phone) -> 'UserBuilder':
        # Método abstrato para adicionar um número de telefone
        pass

    @abstractmethod
    def add_address(self, address) -> 'UserBuilder':
        # Método abstrato para adicionar um endereço
        pass


# Construtor Concreto que implementa a interface IUserBuilder
class UserBuilder(IUserBuilder):
    def __init__(self) -> None:
        # Inicializa o builder e reseta o objeto User
        self.reset()

    def reset(self) -> None:
        # Cria uma nova instância de User para começar uma nova construção
        self._result = User()

    @property
    def result(self) -> User:
        # Retorna o objeto User construído e reseta o builder para futuras construções
        return_data = self._result
        self.reset()
        return return_data

    def add_firstname(self, firstname) -> 'UserBuilder':
        # Adiciona o primeiro nome ao objeto User e retorna a própria instância do builder para encadeamento
        self._result.firstname = firstname
        return self

    def add_lastname(self, lastname) -> 'UserBuilder':
        # Adiciona o sobrenome ao objeto User e retorna a própria instância do builder para encadeamento
        self._result.lastname = lastname
        return self

    def add_age(self, age) -> 'UserBuilder':
        # Adiciona a idade ao objeto User e retorna a própria instância do builder para encadeamento
        self._result.age = age
        return self

    def add_phone(self, phone) -> 'UserBuilder':
        # Adiciona um número de telefone à lista de telefones do objeto User e retorna a própria instância do builder para encadeamento
        self._result.phone_numbers.append(phone)
        return self

    def add_address(self, address) -> 'UserBuilder':
        # Adiciona um endereço à lista de endereços do objeto User e retorna a própria instância do builder para encadeamento
        self._result.addresses.append(address)
        return self


# Diretor que orquestra a construção do objeto usando o Builder
class UserDirector:
    def __init__(self, builder: UserBuilder) -> None:
        # O diretor trabalha com uma instância específica de UserBuilder
        self._builder = builder

    def with_age(self, firstname, lastname, age) -> User:
        # Método para construir um usuário com nome, sobrenome e idade
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_age(age)
        return self._builder.result

    def with_address(self, firstname, lastname, address) -> User:
        # Método para construir um usuário com nome, sobrenome e endereço
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_address(address)
        return self._builder.result


# Exemplo de uso
if __name__ == "__main__":
    # Instancia o UserBuilder
    user_builder = UserBuilder()
    # Instancia o UserDirector, passando o builder
    user_director = UserDirector(user_builder)

    # Constrói o user1 usando o diretor para configurar nome, sobrenome e idade
    user1 = user_director.with_age('Jean', 'Lucas', 30)
    # Constrói o user2 usando o diretor para configurar nome, sobrenome e endereço
    user2 = user_director.with_address('Maria', 'Bortolon', 'Av Brasil')

    # Imprime os objetos User construídos
    print(user1)
    print(user2)
