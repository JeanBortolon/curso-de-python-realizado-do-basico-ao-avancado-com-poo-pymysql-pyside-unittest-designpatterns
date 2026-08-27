"""
Padrão de Projeto Criacional - Prototype

Especificar os tipos de objetos a serem criados
usando uma instância-protótipo e criar novos objetos
pela cópia desse protótipo

O objetivo principal é evitar o custo de criar um objeto
de forma convencional (ex: usando o construtor) quando
isso é ineficiente. Em vez disso, você cria um objeto
base (protótipo) e, para criar novos objetos, simplesmente
clona o protótipo.
"""

from __future__ import annotations
from typing import List
from copy import deepcopy

# Mixin para fornecer uma representação de string legível para os objetos.
# Isso ajuda na depuração, mostrando o nome da classe e seus atributos.
class StringReprMixin:
    def __str__(self):
        # Formata os atributos do objeto como 'chave=valor'.
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        # __repr__ é usado para representações "oficiais",
        # aqui, reutilizamos a mesma formatação do __str__.
        return self.__str__()


# A classe Person é o nosso "Protótipo Concreto".
# É o objeto que queremos clonar.
class Person(StringReprMixin):
    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        # Este atributo é uma lista, um objeto mutável.
        # Isso é importante para entender a necessidade do deepcopy.
        self.addresses: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    # O método clone é o coração do padrão Prototype.
    def clone(self) -> Person:
        # deepcopy cria uma cópia profunda (recursiva) do objeto.
        # Isso significa que tanto o objeto Person quanto os objetos
        # mutáveis dentro dele (como a lista de 'addresses') são
        # duplicados. Se usássemos uma cópia rasa (shallow copy),
        # o novo objeto Person compartilharia a mesma lista de endereços
        # com o original, o que causaria efeitos colaterais indesejados.
        return deepcopy(self)


# Uma classe simples para representar um endereço.
class Address(StringReprMixin):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


# Código cliente que demonstra o uso do padrão.
if __name__ == "__main__":

    # 1. Cria o objeto original (protótipo).
    Jean = Person('Jean', 'Bortolon')
    endereco_Jean = Address('Av. Brasil', '250A')
    Jean.add_address(endereco_Jean)

    # 2. Clona o objeto original para criar um novo.
    # Em vez de criar um novo objeto Person do zero,
    # nós simplesmente copiamos o objeto 'Jean'.
    esposa_Jean = Jean.clone()
    esposa_Jean.firstname = 'Letícia'

    # 3. Imprime os objetos para mostrar o resultado.
    # Observe que 'Jean' e 'esposa_Jean' são objetos diferentes.
    # A alteração do nome em 'esposa_Jean' não afeta 'Jean'.
    # Mais importante, ambos têm o mesmo endereço, mas como usamos
    # deepcopy, a lista de endereços de cada um é independente.
    print(Jean)
    print(esposa_Jean)
