"""
Strategy é um padrão de projeto comportamental que tem
a intenção de definir uma família de algoritmos,
encapsular cada uma delas e torná-las intercambiáveis.
Strategy permite que o algorítmo varie independentemente
dos clientes que o utilizam.

Princípio do aberto/fechado (Open/closed principle)
Entidades devem ser abertas para extensão, mas fechadas para modificação
"""
from __future__ import annotations
from abc import ABC, abstractmethod


# Contexto: A classe Order (Pedido) usa uma estratégia de desconto.
# Ela não sabe os detalhes da implementação do desconto, apenas que existe um método 'calculate'.
class Order:
    # O construtor da Order recebe o total do pedido e uma instância da estratégia de desconto.
    def __init__(self, total: float, discount: DiscountStrategy):
        self._total = total
        self._discount = discount

    @property
    def total(self):
        # Retorna o valor total original do pedido.
        return self._total

    @property
    def total_with_discount(self):
        # Delega o cálculo do desconto para o objeto de estratégia de desconto.
        # A classe Order não precisa saber como o desconto é calculado.
        return self._discount.calculate(self.total)


# Interface da Estratégia: Define a interface comum para todos os algoritmos.
# Todas as classes de estratégia de desconto devem implementar este método.
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float:
        # Método abstrato que deve ser implementado pelas estratégias concretas.
        # Recebe o valor original e retorna o valor com desconto.
        pass


# Estratégias Concretas: Implementam a interface da estratégia.
# Cada classe representa um algoritmo de desconto específico.

class TwentyPercent(DiscountStrategy):
    # Estratégia para aplicar um desconto de 20%.
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FiftyPercent(DiscountStrategy):
    # Estratégia para aplicar um desconto de 50%.
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class NoDiscount(DiscountStrategy):
    # Estratégia para não aplicar nenhum desconto.
    def calculate(self, value: float) -> float:
        return value


class CustomDiscount(DiscountStrategy):
    # Estratégia para aplicar um desconto personalizado.
    def __init__(self, discount_percentage: float) -> None:
        # O desconto é armazenado como uma fração (ex: 5% -> 0.05).
        self.discount = discount_percentage / 100

    def calculate(self, value: float) -> float:
        # Calcula o valor com o desconto percentual personalizado.
        return value - (value * self.discount)


if __name__ == "__main__":
    # Cria instâncias de diferentes estratégias de desconto.
    twenty_percent = TwentyPercent()
    fifty_percent = FiftyPercent()
    no_discount = NoDiscount()
    five_percent = CustomDiscount(5)  # Desconto personalizado de 5%

    # Cria um pedido e aplica a estratégia de 20% de desconto.
    order = Order(1000, twenty_percent)
    print(f"Pedido com 20% de desconto: Total original={order.total}, Com desconto={order.total_with_discount}")

    # Altera a estratégia para 50% de desconto para o próximo pedido.
    order = Order(1000, fifty_percent)
    print(f"Pedido com 50% de desconto: Total original={order.total}, Com desconto={order.total_with_discount}")

    # Altera a estratégia para nenhum desconto.
    order = Order(1000, no_discount)
    print(f"Pedido sem desconto: Total original={order.total}, Com desconto={order.total_with_discount}")

    # Altera a estratégia para 5% de desconto personalizado.
    order = Order(1000, five_percent)
    print(f"Pedido com 5% de desconto: Total original={order.total}, Com desconto={order.total_with_discount}")

    # Cria um novo pedido com uma estratégia de desconto personalizado de 13% no momento da criação.
    order = Order(1000, CustomDiscount(13))
    print(f"Pedido com 13% de desconto personalizado: Total original={order.total}, Com desconto={order.total_with_discount}")
