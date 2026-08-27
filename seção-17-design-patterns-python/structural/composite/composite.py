"""
Composite é um padrão de projeto estrutural que permite que
você utilize a composição para criar objetos em estruturas
de árvores. O padrão permite aos clientes tratarem de maneira
uniforme objetos individuais (Leaf) e composições de
objetos (Composite).

IMPORTANTE: só aplique este padrão em uma estrutura que possa
ser representada em formato hierárquico (árvore).

No padrão composite, temos dois tipos de objetos:
Composite (que representa nós internos da árvore) e Leaf
(que representa nós externos da árvore).

Objetos Composite são objetos mais complexos e com filhos.
Geralmente, eles delegam trabalho para os filhos usando
um método em comum.
Objetos Leaf são objetos simples, da ponta e sem filhos.
Geralmente, são esses objetos que realizam o trabalho
real da aplicação.
"""
from __future__ import annotations # Permite o uso de anotações de tipo de avanço (ex: referenciar a própria classe em um tipo)
from abc import ABC, abstractmethod  # Importa a Base Class Abstrata (ABC) e o decorador abstractmethod para definir interfaces
from typing import List            # Importa List para anotações de tipo, indicando que uma variável é uma lista

# A classe abstrata Componente declara a interface para os objetos na composição.
# Para o padrão Composite, essa interface precisa declarar métodos para gerenciar
# os filhos, além de métodos para as operações comuns.
class BoxStructure(ABC):
    """
    Componente Abstrato: Define a interface para todos os objetos na composição,
    tanto para os objetos complexos (Composite) quanto para os simples (Leaf).
    Declara métodos para operações comuns e, opcionalmente, para gerenciar filhos.
    """
    @abstractmethod
    def print_content(self) -> None:
        """
        Método abstrato para imprimir o conteúdo do componente.
        Será implementado por classes concretas (Leaf e Composite).
        """
        pass

    @abstractmethod
    def get_price(self) -> float:
        """
        Método abstrato para obter o preço do componente.
        Será implementado por classes concretas (Leaf e Composite).
        """
        pass

    # Métodos para gerenciar os filhos (componentes).
    # São métodos opcionais no Componente, mas obrigatórios para o Composite.
    # No padrão Composite, geralmente esses métodos são vazios ou levantam um erro
    # nas folhas, pois as folhas não possuem filhos para gerenciar.
    def add(self, child: BoxStructure) -> None:
        """
        Adiciona um componente filho à estrutura.
        Este método é tipicamente implementado em objetos Composite.
        """
        pass

    def remove(self, child: BoxStructure) -> None:
        """
        Remove um componente filho da estrutura.
        Este método é tipicamente implementado em objetos Composite.
        """
        pass


# A classe Composite representa os nós internos da estrutura de árvore.
# Ela contém outros componentes (Composite ou Leaf) e implementa os métodos
# do Componente para delegar a operação aos seus filhos.
class Box(BoxStructure):
    """
    Composite: Representa nós que contêm outros componentes (filhos).
    Delegam o trabalho para seus filhos e podem ter comportamentos adicionais
    antes e/ou depois de delegar.
    """

    def __init__(self, name: str) -> None:
        """
        Inicializa uma caixa (Composite) com um nome e uma lista vazia de filhos.
        """
        self.name = name
        self._children: List[BoxStructure] = [] # Lista para armazenar os componentes filhos

    def print_content(self) -> None:
        """
        Imprime o nome da caixa e, em seguida, itera sobre seus filhos
        chamando o método print_content de cada um, demonstrando a delegação.
        """
        print(f'\n{self.name}:')
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        """
        Calcula o preço total da caixa somando os preços de todos os seus filhos.
        """
        # Utiliza uma compreensão de lista para somar os preços de todos os filhos.
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        """
        Adiciona um componente (Box ou Product) à lista de filhos desta caixa.
        """
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        """
        Remove um componente da lista de filhos desta caixa, se ele estiver presente.
        """
        if child in self._children:
            self._children.remove(child)


# A classe Leaf representa os nós externos da estrutura de árvore (os objetos individuais).
# Ela não tem filhos e implementa as operações do Componente diretamente.
class Product(BoxStructure):
    """
    Leaf (Folha): Representa os objetos "folha" ou "simples" na estrutura.
    Não pode ter filhos e implementa o comportamento das operações diretamente.
    """

    def __init__(self, name: str, price: float) -> None:
        """
        Inicializa um produto (Leaf) com um nome e um preço.
        """
        self.name = name
        self.price = price

    def print_content(self) -> None:
        """
        Imprime o nome e o preço do produto.
        """
        print(self.name, self.price)

    def get_price(self) -> float:
        """
        Retorna o preço do produto.
        """
        return self.price


# Exemplo de uso do padrão Composite
if __name__ == "__main__":
    # Criação de objetos Leaf (produtos individuais)
    camiseta1 = Product('camiseta1', 10)
    camiseta2 = Product('camiseta2', 10)
    camiseta3 = Product('camiseta3', 10)

    # Criação de um objeto Composite (caixa de camisetas)
    caixa_camisetas = Box('Caixa de camiseta')
    caixa_camisetas.add(camiseta1) # Adiciona produtos à caixa de camisetas
    caixa_camisetas.add(camiseta2)
    caixa_camisetas.add(camiseta3)

    # Criação de mais objetos Leaf (smartphones individuais)
    smartphone1 = Product('smartphone1', 10000)
    smartphone2 = Product('smartphone2', 10000)

    # Criação de outro objeto Composite (caixa de smartphones)
    caixa_smartphones = Box('Caixa de Smartphones')
    caixa_smartphones.add(smartphone1) # Adiciona smartphones à caixa
    caixa_smartphones.add(smartphone2)

    # Criação de um Composite aninhado (caixa grande contendo outras caixas)
    caixa_grande = Box('Caixa grande')
    caixa_grande.add(caixa_camisetas)  # Adiciona a caixa de camisetas à caixa grande
    caixa_grande.add(caixa_smartphones) # Adiciona a caixa de smartphones à caixa grande

    # Demonstração das operações:
    # print_content() é chamado na caixa_grande, que delega para suas sub-caixas e produtos.
    caixa_grande.print_content()
    # get_price() é chamado na caixa_grande, que recursivamente soma os preços de todos os itens.
    print(caixa_grande.get_price()) # Imprime o preço total de todos os itens na caixa grande
