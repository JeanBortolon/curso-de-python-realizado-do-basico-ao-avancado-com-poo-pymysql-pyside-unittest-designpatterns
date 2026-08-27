# Padrão de Projeto Comportamental - Iterator

O padrão **Iterator** é um padrão de projeto comportamental que tem como objetivo fornecer uma maneira de acessar os elementos de uma coleção de objetos sequencialmente, sem a necessidade de expor a sua representação interna.

## O que foi estudado?

Nesta seção, foi estudado o padrão de projeto Iterator. O objetivo principal do padrão é retirar a responsabilidade de acesso e percurso de uma coleção, delegando tais tarefas para um objeto iterador.

### Vantagens de utilizar o padrão Iterator:

- **Abstração da complexidade:** Permite que a complexidade dos algoritmos de iteração seja separada da coleção em si.
- **Flexibilidade:** Uma coleção pode ter diferentes maneiras e percursos para expor seus elementos.
- **Segurança:** A estrutura interna da coleção não é exposta, protegendo os dados de acessos indevidos.

## Arquivos

- **`iterator-1.py`**: Este arquivo contém a implementação do padrão Iterator em Python. Ele demonstra como criar uma coleção personalizada (`MyList`) que utiliza iteradores para percorrer seus elementos de diferentes maneiras (normal e reversa).
- **`iterator.graphml`** e **`iterator.png`**: Estes arquivos são representações visuais do padrão de projeto Iterator. O arquivo `.png` é a imagem do diagrama, enquanto o `.graphml` é o arquivo fonte do diagrama, que pode ser editado em ferramentas como o yEd.

## Como o código funciona?

O arquivo `iterator-1.py` implementa o padrão da seguinte forma:

1.  **`MyIterator` e `ReverseIterator`:** São as classes que implementam a interface `Iterator`. Elas são responsáveis por percorrer a coleção de elementos em uma ordem específica (normal e reversa, respectivamente). Elas mantêm o estado da iteração (o índice atual) e fornecem um método `__next__` para obter o próximo elemento.

2.  **`MyList`:** É a classe que representa a coleção de objetos. Ela implementa a interface `Iterable`, o que significa que ela pode ser usada em um loop `for`. Ela possui o método `__iter__` que retorna uma nova instância de um iterador (neste caso, `MyIterator`). Além disso, ela fornece um método `reverse_iterator` que retorna um iterador para percorrer a lista em ordem inversa.

3.  **Exemplo de uso:** No final do arquivo, há um exemplo de como usar a `MyList` e seus iteradores. Ele demonstra como percorrer a lista em ordem normal e em ordem reversa.

Este exemplo ilustra como o padrão Iterator pode ser usado para fornecer uma maneira flexível e segura de acessar os elementos de uma coleção.
