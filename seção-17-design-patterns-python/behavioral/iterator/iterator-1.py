"""
Iterator é um padrão comportamental que tem a
intenção de fornecer um meio de acessar,
sequencialmente, os elementos de um objeto
agregado sem expor sua representação subjacente.

- Uma coleção deve fornecer um meio de acessar
    seus elementos sem expor sua estrutura interna
- Uma coleção pode ter maneiras e percursos diferentes
    para expor seus elementos
- Você deve separar a complexidade dos algoritmos
    de iteração da coleção em si

A ideia principal do padrão é retirar a responsabilidade
de acesso e percurso de uma coleção, delegando tais
tarefas para um objeto iterador.
"""
from collections.abc import Iterator, Iterable
from typing import List, Any


class MyIterator(Iterator):
    # O construtor recebe a coleção (lista) sobre a qual irá iterar.
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection  # Armazena a coleção.
        self._index = 0  # Inicializa o índice para começar do primeiro elemento.

    # Método 'next' para compatibilidade com versões mais antigas do Python (Python 2)
    # ou para ser explicitamente chamado quando se quer controlar a iteração manualmente.
    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            return None

    # Implementa o protocolo do iterador, retornando o próximo item da coleção.
    def __next__(self):
        try:
            item = self._collection[self._index]  # Obtém o item atual.
            self._index += 1  # Move para o próximo índice.
            return item  # Retorna o item.
        except IndexError:
            # Se o índice estiver fora dos limites, significa que a iteração terminou.
            raise StopIteration  # Levanta StopIteration para sinalizar o fim da iteração.


class ReverseIterator(Iterator):
    # O construtor recebe a coleção (lista) sobre a qual irá iterar.
    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection  # Armazena a coleção.
        self._index = -1  # Inicializa o índice para começar do último elemento.

    # Método 'next' para compatibilidade ou chamada manual.
    def next(self):
        try:
            return self.__next__()
        except StopIteration:
            return None

    # Implementa o protocolo do iterador para iteração reversa.
    def __next__(self):
        try:
            item = self._collection[self._index]  # Obtém o item atual (do fim para o começo).
            # Verifica se o índice ainda está dentro dos limites da lista.
            # Se _index for menor que -len(self._collection), significa que todos
            # os elementos foram iterados.
            if self._index < -len(self._collection):
                raise StopIteration
            self._index -= 1  # Move para o índice anterior.
            return item  # Retorna o item.
        except IndexError:
            # Se o índice estiver fora dos limites (o que pode acontecer se a lista estiver vazia),
            # ou se já iteramos por todos os elementos, a iteração terminou.
            raise StopIteration


class MyList(Iterable):
    # O construtor inicializa a lista interna de itens e um iterador padrão para ela.
    def __init__(self) -> None:
        self._items: List[Any] = []  # A coleção interna de elementos.
        # Cria uma instância de MyIterator para ser o iterador padrão desta lista.
        # Isso permite que a lista seja iterada diretamente em um loop `for`.
        self._my_iterator = MyIterator(self._items)

    # Método para adicionar um valor à coleção.
    def add(self, value: Any) -> None:
        self._items.append(value)

    # Este método é o que torna a classe 'Iterable'.
    # Quando um loop 'for' é usado na instância de MyList, ele chama este método
    # para obter um objeto iterador.
    def __iter__(self) -> Iterator:
        # Retorna uma nova instância do iterador padrão (MyIterator)
        # para garantir que cada nova iteração comece do início.
        # Ou, pode-se retornar self._my_iterator se a intenção é ter um único
        # iterador compartilhado (mas isso pode levar a comportamentos inesperados
        # se múltiplas iterações simultâneas forem tentadas).
        return MyIterator(self._items) # Retorna um novo iterador para garantir iterações independentes.

    # Método que fornece um iterador para percorrer a lista em ordem inversa.
    def reverse_iterator(self) -> Iterator:
        return ReverseIterator(self._items)

    # Representação em string do objeto MyList.
    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self._items})'


if __name__ == "__main__":
    # Cria uma instância da nossa coleção personalizada.
    mylist = MyList()
    # Adiciona elementos à coleção.
    mylist.add('Luiz')
    mylist.add('Maria')
    mylist.add('João')

    # Exemplo de como um loop 'for' usa o método __iter__ de MyList
    # para obter um iterador (MyIterator) e percorrer os elementos.
    print("Iteração normal:")
    for value in mylist:
        print(value)

    print("\nIteração reversa:")
    # Demonstra o uso de um iterador diferente (ReverseIterator)
    # para percorrer a coleção em ordem inversa.
    for value in mylist.reverse_iterator():
        print(value)
