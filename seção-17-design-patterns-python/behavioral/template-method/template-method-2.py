"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""
from abc import ABC, abstractmethod


class Pizza(ABC):
    """
    Classe abstrata que define o esqueleto do algoritmo para preparar uma pizza.
    Esta é a classe 'AbstractClass' do padrão Template Method.
    """

    def prepare(self) -> None:
        """
        Este é o Template Method. Ele define a sequência fixa de passos
        para preparar uma pizza. Alguns passos são implementados aqui,
        outros são deixados para as subclasses (métodos abstratos)
        ou podem ser estendidos opcionalmente (hooks).
        """
        self.hook_before_add_ingredients()  # Hook: Chamado antes de adicionar ingredientes, opcional para subclasses.
        self.add_ingrentients()  # Abstract: Subclasses devem implementar a adição de ingredientes.
        self.hook_after_add_ingredients()  # Hook: Chamado depois de adicionar ingredientes, opcional para subclasses.
        self.cook()  # Abstract: Subclasses devem implementar o cozimento.
        self.cut()  # Concrete: Método implementado na classe base, comum a todas as pizzas.
        self.serve()  # Concrete: Método implementado na classe base, comum a todas as pizzas.

    # Hooks: Métodos vazios que subclasses podem sobrescrever opcionalmente
    # para injetar lógica específica em pontos definidos do algoritmo.
    def hook_before_add_ingredients(self) -> None: pass
    def hook_after_add_ingredients(self) -> None: pass

    # Métodos concretos: Implementações padrão que não precisam ser alteradas
    # pelas subclasses.
    def cut(self) -> None:
        print(f'{self.__class__.__name__}: Cortando pizza.')

    def serve(self) -> None:
        print(f'{self.__class__.__name__}: Servindo pizza.')

    # Métodos abstratos: Devem ser implementados por todas as subclasses concretas.
    # Representam os passos variáveis do algoritmo.
    @abstractmethod
    def add_ingrentients(self) -> None: pass

    @abstractmethod
    def cook(self) -> None: pass


class AModa(Pizza):
    """
    Subclasse concreta que implementa os passos abstratos para uma pizza "À Moda".
    Esta é a classe 'ConcreteClass' do padrão Template Method.
    """
    def add_ingrentients(self) -> None:
        """ Implementação específica para adicionar ingredientes da pizza "À Moda". """
        print(f'AModa - adicionando ingredientes: presunto, queijo, goiabada')

    def cook(self) -> None:
        """ Implementação específica para cozinhar a pizza "À Moda". """
        print(f'AModa - cozinhado por 45min no forno a lenha')


class Veg(Pizza):
    """
    Outra subclasse concreta que implementa os passos abstratos para uma pizza vegana.
    Demonstra a capacidade de sobrescrever hooks.
    """
    def hook_before_add_ingredients(self) -> None:
        """
        Sobrescreve o hook para adicionar uma etapa extra antes de adicionar
        os ingredientes para a pizza vegana.
        """
        print('Veg - Lavando ingredientes')

    def add_ingrentients(self) -> None:
        """ Implementação específica para adicionar ingredientes da pizza vegana. """
        print(f'Veg - adicionando ingredientes: ingredientes veganos')

    def cook(self) -> None:
        """ Implementação específica para cozinhar a pizza vegana. """
        print(f'Veg - cozinhado por 5min no forno comum')


if __name__ == "__main__":
    print('--- Preparando Pizza "À Moda" ---')
    # Cria uma instância da pizza "À Moda"
    a_moda = AModa()
    # Chama o template method 'prepare()'. O algoritmo é executado,
    # usando as implementações de AModa para os passos abstratos.
    a_moda.prepare()

    print('\n--- Preparando Pizza Vegana ---')
    # Cria uma instância da pizza vegana
    veg = Veg()
    # Chama o template method 'prepare()'. O algoritmo é executado,
    # usando as implementações de Veg para os passos abstratos e o hook sobrescrito.
    veg.prepare()
