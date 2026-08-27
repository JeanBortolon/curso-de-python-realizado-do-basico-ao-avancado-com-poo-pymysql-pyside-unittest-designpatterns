"""
Decorator é um padrão de projeto estrutural que permite que você
adicione novos comportamentos em objetos ao colocá-los dentro de
um "wrapper" (decorador) de objetos.
Decoradores fornecem uma alternativa flexível ao uso de subclasses
para a extensão de funcionalidades.

Decorator (padrão de projeto) != Decorator em Python

Python decorator -> Um decorator é um callable que aceita outra
função como argumento (a função decorada). O decorator pode
realizar algum processamento com a função decorada e devolvê-la
ou substituí-la por outra função ou objeto invocável.
Do livro "Python Fluente", por Luciano Ramalho (pág. 223)

Este arquivo demonstra o padrão de projeto Decorator aplicando-o a um
sistema de criação de cachorros-quentes (hotdogs). O objetivo é permitir
a adição dinâmica de ingredientes a um hotdog existente sem modificar
sua estrutura original, utilizando classes "decoradoras" para envolver
o hotdog base e adicionar novos ingredientes/comportamentos.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List
from copy import deepcopy


# INGREDIENTS
# As classes de Ingredientes representam os componentes básicos de um hotdog.
# Cada ingrediente possui um preço.
@dataclass
class Ingredient:
    """Classe base para todos os ingredientes."""
    price: float


@dataclass
class Bread(Ingredient):
    """Ingrediente: Pão para o hotdog."""
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    """Ingrediente: Salsicha principal."""
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    """Ingrediente: Bacon."""
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    """Ingrediente: Ovo."""
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    """Ingrediente: Queijo."""
    price: float = 6.35


@dataclass
class MashedPotatoes(Ingredient):
    """Ingrediente: Purê de batata."""
    price: float = 2.25


@dataclass
class PotatoSticks(Ingredient):
    """Ingrediente: Batata palha."""
    price: float = 0.99

# Hotdogs


class Hotdog:
    """
    Classe abstrata base para todos os tipos de hotdogs.
    Define a interface comum para hotdogs e decoradores de hotdogs.
    """
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        """Calcula o preço total do hotdog somando os preços dos ingredientes."""
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        """Retorna o nome do hotdog."""
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        """Retorna a lista de ingredientes do hotdog."""
        return self._ingredients

    def __repr__(self) -> str:
        """Representação em string do objeto Hotdog."""
        return f'{self.name}({self.price}) -> {self.ingredients})'


class SimpleHotdog(Hotdog):
    """
    Implementação concreta de um hotdog simples.
    Contém um conjunto básico de ingredientes.
    """
    def __init__(self) -> None:
        self._name: str = 'SimpleHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]


class SpecialHotdog(Hotdog):
    """
    Implementação concreta de um hotdog especial.
    Contém um conjunto mais extenso de ingredientes.
    """
    def __init__(self) -> None:
        self._name: str = 'SpecialHotdog'
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            Bacon(),
            Egg(),
            Cheese(),
            MashedPotatoes(),
            PotatoSticks()
        ]


# Decorators
class HotdogDecorator(Hotdog):
    """
    Classe base para todos os decoradores de hotdogs.
    Mantém uma referência ao objeto Hotdog envolvido (componente).
    Delega todos os comportamentos (preço, nome, ingredientes) ao hotdog envolvido.
    """
    def __init__(self, hotdog: Hotdog) -> None:
        self.hotdog = hotdog

    @property
    def price(self) -> float:
        """Delega o cálculo do preço ao hotdog envolvido."""
        return self.hotdog.price

    @property
    def name(self) -> str:
        """Delega o nome ao hotdog envolvido."""
        return self.hotdog.name

    @property
    def ingredients(self) -> List[Ingredient]:
        """Delega a lista de ingredientes ao hotdog envolvido."""
        return self.hotdog.ingredients


class BaconDecorator(HotdogDecorator):
    """
    Decorador concreto que adiciona Bacon a um hotdog.
    Modifica a lista de ingredientes e o nome do hotdog decorado.
    """
    def __init__(self, hotdog: Hotdog) -> None:
        super().__init__(hotdog) # Chama o construtor da classe base (HotdogDecorator).

        self._ingredient = Bacon() # Define o ingrediente específico deste decorador.

        # Cria uma cópia profunda dos ingredientes existentes e adiciona o novo.
        # Isso garante que a lista de ingredientes do hotdog original não seja modificada.
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def price(self) -> float:
        """
        Recalcula o preço do hotdog, incluindo o ingrediente adicionado por este decorador.
        """
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        """
        Atualiza o nome do hotdog para indicar a adição do novo ingrediente (e.g., 'SimpleHotdog +Bacon').
        """
        return f'{self.hotdog.name} +{self._ingredient.__class__.__name__}'

    @property
    def ingredients(self) -> List[Ingredient]:
        """
        Retorna a lista de ingredientes atualizada, incluindo o bacon.
        """
        return self._ingredients


if __name__ == "__main__":
    # Cria uma instância de um hotdog simples.
    simple_hotdog = SimpleHotdog()
    print(f'Hotdog simples: {simple_hotdog.name}, Preço: {simple_hotdog.price}, Ingredientes: {[ing.price for ing in simple_hotdog.ingredients]}')

    # Exemplo de como um HotdogDecorator base não altera o hotdog, apenas o envolve.
    decorated_simple_hotdog = HotdogDecorator(simple_hotdog)
    print(f'Hotdog decorado (base): {decorated_simple_hotdog.name}, Preço: {decorated_simple_hotdog.price}, Ingredientes: {[ing.price for ing in decorated_simple_hotdog.ingredients]}')

    # Decora o hotdog simples com Bacon.
    bacon_simple_hotdog = BaconDecorator(simple_hotdog)
    print(f'Hotdog com Bacon: {bacon_simple_hotdog.name}, Preço: {bacon_simple_hotdog.price}, Ingredientes: {[ing.price for ing in bacon_simple_hotdog.ingredients]}')

    # Decora o hotdog com Bacon novamente, mostrando que decoradores podem ser aninhados.
    bacon_simple_hotdog = BaconDecorator(bacon_simple_hotdog)
    print(f'Hotdog com Duplo Bacon: {bacon_simple_hotdog.name}, Preço: {bacon_simple_hotdog.price}, Ingredientes: {[ing.price for ing in bacon_simple_hotdog.ingredients]}')

    # Exemplo com SpecialHotdog
    special_hotdog = SpecialHotdog()
    print(f'Hotdog especial: {special_hotdog.name}, Preço: {special_hotdog.price}, Ingredientes: {[ing.price for ing in special_hotdog.ingredients]}')

    bacon_special_hotdog = BaconDecorator(special_hotdog)
    print(f'Hotdog especial com Bacon: {bacon_special_hotdog.name}, Preço: {bacon_special_hotdog.price}, Ingredientes: {[ing.price for ing in bacon_special_hotdog.ingredients]}')
