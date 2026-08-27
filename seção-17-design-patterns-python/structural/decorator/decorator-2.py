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
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import List
from copy import deepcopy


# INGREDIENTS
# Classe base para ingredientes
@dataclass
class Ingredient:
    price: float


# Ingredientes concretos, cada um com seu preço padrão
@dataclass
class Bread(Ingredient):
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    price: float = 6.35


@dataclass
class MashedPotatoes(Ingredient):
    price: float = 2.25


@dataclass
class PotatoSticks(Ingredient):
    price: float = 0.99

# Hotdogs
# Componente (Hotdog) - Define a interface para os objetos que podem ser decorados.
# Tanto o componente base quanto os decoradores devem implementar esta interface.
class Hotdog:
    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        # Calcula o preço total somando os preços de todos os ingredientes
        return round(sum([
            ingredient.price for ingredient in self._ingredients
        ]), 2)

    @property
    def name(self) -> str:
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        return self._ingredients

    def __repr__(self) -> str:
        # Representação em string do hotdog
        return f'{self.name}({self.price}) -> {self.ingredients})'


# Componente Concreto - Implementa a interface Hotdog com uma configuração básica.
class SimpleHotdog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'SimpleHotdog'
        # Define os ingredientes padrão de um hotdog simples
        self._ingredients: List[Ingredient] = [
            Bread(),
            Sausage(),
            PotatoSticks()
        ]


# Componente Concreto - Implementa a interface Hotdog com uma configuração especial.
class SpecialHotdog(Hotdog):
    def __init__(self) -> None:
        self._name: str = 'SpecialHotdog'
        # Define os ingredientes padrão de um hotdog especial
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
# Decorador Abstrato / Concreto
# HotdogDecorator atua como um decorador concreto, estendendo a funcionalidade de Hotdog.
class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog, ingredient: Ingredient) -> None:
        # Armazena a instância do hotdog sendo decorado
        self.hotdog = hotdog
        # Armazena o novo ingrediente a ser adicionado
        self._ingredient = ingredient

        # Copia os ingredientes do hotdog original e adiciona o novo ingrediente
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def name(self) -> str:
        # Altera o nome para refletir o ingrediente adicionado
        return f'{self.hotdog.name} +{self._ingredient.__class__.__name__}'


if __name__ == "__main__":
    print('### Testando Hotdog Simples ###')
    # Cria um hotdog simples
    simple_hotdog = SimpleHotdog()
    print(simple_hotdog)
    print(f'Nome: {simple_hotdog.name}')
    print(f'Preço: {simple_hotdog.price}')
    print(f'Ingredientes: {simple_hotdog.ingredients}')
    print()

    print('### Testando Hotdog Especial ###')
    special_hotdog = SpecialHotdog()
    print(special_hotdog)
    print(f'Nome: {special_hotdog.name}')
    print(f'Preço: {special_hotdog.price}')
    print(f'Ingredientes: {special_hotdog.ingredients}')
    print()

    print('### Decorando Hotdog Simples ###')
    # Decora o hotdog simples com bacon
    bacon_simple_hotdog = HotdogDecorator(simple_hotdog, Bacon())
    print(bacon_simple_hotdog)
    print(f'Nome: {bacon_simple_hotdog.name}')
    print(f'Preço: {bacon_simple_hotdog.price}')
    print(f'Ingredientes: {bacon_simple_hotdog.ingredients}')
    print()

    # Decora o hotdog com bacon e ovo
    egg_bacon_simple_hotdog = HotdogDecorator(bacon_simple_hotdog, Egg())
    print(egg_bacon_simple_hotdog)
    print(f'Nome: {egg_bacon_simple_hotdog.name}')
    print(f'Preço: {egg_bacon_simple_hotdog.price}')
    print(f'Ingredientes: {egg_bacon_simple_hotdog.ingredients}')
    print()

    # Decora o hotdog com bacon, ovo e purê de batatas
    mashed_potato_egg_bacon_simple_hotdog = HotdogDecorator(
        egg_bacon_simple_hotdog,
        MashedPotatoes()
    )
    print(mashed_potato_egg_bacon_simple_hotdog)
    print(f'Nome: {mashed_potato_egg_bacon_simple_hotdog.name}')
    print(f'Preço: {mashed_potato_egg_bacon_simple_hotdog.price}')
    print(f'Ingredientes: {mashed_potato_egg_bacon_simple_hotdog.ingredients}')
    print()
