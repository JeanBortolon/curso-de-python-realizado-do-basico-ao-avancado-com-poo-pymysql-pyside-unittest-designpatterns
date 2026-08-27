# Padrão de Projeto Estrutural: Composite (Composto)

Este diretório contém uma implementação do padrão de projeto estrutural **Composite** em Python.

## O que é o Padrão Composite?

O padrão Composite permite que você trate objetos individuais (folhas) e coleções de objetos (compostos) de maneira uniforme. Isso significa que você pode operar em uma estrutura de objetos em formato de árvore como se fossem todos o mesmo tipo de objeto, sem se preocupar se você está lidando com um objeto único ou com um grupo de objetos.

A ideia principal é organizar objetos em estruturas de árvore para representar hierarquias de "parte-todo".

**Quando usar?**
Use o padrão Composite quando você precisa construir objetos complexos a partir de objetos mais simples, e quando quer que o cliente possa tratar objetos simples e objetos complexos de forma idêntica. É ideal para estruturas hierárquicas, como menus, sistemas de arquivos, ou como neste exemplo, caixas com produtos.

## Componentes do Padrão Composite

No padrão Composite, geralmente temos os seguintes papéis:

1.  **Componente (Component):**
    *   Declara a interface comum para todos os objetos na composição (tanto folhas quanto compostos).
    *   Pode fornecer uma implementação padrão para operações comuns.
    *   Pode declarar uma interface para acessar e gerenciar seus filhos.
    *   No nosso exemplo, esta é a classe abstrata `BoxStructure`.

2.  **Folha (Leaf):**
    *   Representa os objetos "folha" da composição, que não podem ter filhos.
    *   Implementa as operações do Componente diretamente.
    *   No nosso exemplo, esta é a classe `Product`.

3.  **Composto (Composite):**
    *   Representa os objetos que podem conter outros Componentes (tanto folhas quanto outros compostos).
    *   Armazena os filhos e implementa as operações do Componente delegando-as aos seus filhos.
    *   Implementa os métodos para adicionar e remover filhos.
    *   No nosso exemplo, esta é a classe `Box`.

## `composite.py` - Exemplo Prático

O arquivo `composite.py` demonstra o padrão Composite através de um sistema de "caixas" e "produtos":

*   **`BoxStructure` (Componente):** Uma classe abstrata que define os métodos `print_content()` para exibir o conteúdo e `get_price()` para retornar o preço. Também define métodos `add()` e `remove()` que são úteis para os compostos.
*   **`Product` (Folha):** Representa um produto individual com um `nome` e um `preço`. Ele implementa `print_content()` para mostrar seus próprios detalhes e `get_price()` para retornar seu preço. Não pode ter filhos.
*   **`Box` (Composto):** Representa uma caixa que pode conter outros `Product`s ou outras `Box`es. Ele implementa `print_content()` iterando sobre seus itens internos e chamando `print_content()` para cada um. O `get_price()` soma os preços de todos os itens (produtos e sub-caixas) que ele contém, mostrando a capacidade de operar recursivamente na estrutura. Possui os métodos `add()` e `remove()` para gerenciar seus itens.

O bloco `if __name__ == "__main__":` no final do arquivo mostra um exemplo de uso, onde caixas (composites) e produtos (folhas) são combinados em uma estrutura hierárquica, e operações como `print_content()` e `get_price()` são aplicadas à estrutura inteira, de forma transparente.

## Arquivos Visuais

Os arquivos `.graphml` e `.png` presentes neste diretório são representações visuais (diagramas) da estrutura do padrão Composite, provavelmente gerados por alguma ferramenta de modelagem. Eles ajudam a entender graficamente as relações entre os componentes, folhas e compostos.

*   `composite.graphml` e `composite.png`: Provavelmente um diagrama UML ou similar ilustrando a estrutura do padrão Composite.
*   `bst.graphml` e `bst.png`: Podem representar outro exemplo de estrutura em árvore ou alguma variação do uso do padrão.

Este padrão é muito útil para gerenciar hierarquias de objetos, permitindo que você adicione novas classes de folhas ou compostos sem alterar o código cliente que usa a estrutura.
