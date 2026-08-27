# Padrão de Projeto Memento

O padrão de projeto Memento é um padrão comportamental que permite salvar e restaurar o estado anterior de um objeto sem violar o encapsulamento.

## Explicação dos Arquivos

### `memento-1.py`

Este arquivo contém a implementação do padrão Memento em Python. Ele é dividido em três classes principais:

*   **`ImageEditor` (Originator):** É o objeto cujo estado queremos salvar. No exemplo, é um editor de imagens que possui atributos como nome, largura e altura.
*   **`Memento`:** É um objeto que armazena o estado do `ImageEditor`. Ele é imutável, ou seja, uma vez criado, seu estado não pode ser alterado.
*   **`Caretaker`:** É o objeto que armazena os `Mementos`. Ele é responsável por salvar e restaurar o estado do `ImageEditor` quando solicitado.

### `memento.graphml` e `memento.png`

Esses arquivos são representações visuais do padrão Memento, provavelmente um diagrama de classes que ilustra a relação entre as classes `ImageEditor`, `Memento` e `Caretaker`. A imagem `memento.png` é uma visualização do arquivo `memento.graphml`.

## Como o Código Funciona

1.  O `ImageEditor` (Originator) cria um `Memento` contendo um snapshot de seu estado atual.
2.  O `Caretaker` armazena esse `Memento` em uma lista.
3.  Quando precisamos restaurar o estado anterior, o `Caretaker` pega o `Memento` mais recente da lista e o entrega ao `ImageEditor`.
4.  O `ImageEditor` então usa o estado do `Memento` para restaurar seu próprio estado.

Isso é útil para implementar funcionalidades como "desfazer" (undo), onde o usuário pode reverter uma ação e voltar ao estado anterior do objeto.
