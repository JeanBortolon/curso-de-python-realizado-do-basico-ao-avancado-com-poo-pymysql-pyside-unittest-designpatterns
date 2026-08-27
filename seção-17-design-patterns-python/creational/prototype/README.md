# Estudo sobre o Design Pattern: Prototype

Esta pasta contém um exemplo prático do padrão de projeto criacional **Prototype**. O objetivo deste padrão é especificar os tipos de objetos a serem criados usando uma instância-protótipo e criar novos objetos pela cópia desse protótipo.

A ideia principal é evitar o custo de criar um objeto de forma convencional (usando o construtor), especialmente quando a criação é complexa ou ineficiente. Em vez disso, cria-se um objeto base (o protótipo) e, para gerar novos objetos, simplesmente clona-se o protótipo.

## Arquivos no Diretório

- ### `prototype-1.py`
  Este script é a implementação principal do padrão Prototype. Ele define as seguintes classes:
  - `Person`: O protótipo concreto. Esta classe representa um objeto que queremos clonar. Ela contém atributos simples (nome, sobrenome) e um atributo mutável (uma lista de endereços).
  - `Address`: Uma classe simples para representar os endereços associados a uma pessoa.
  - `StringReprMixin`: Uma classe mixin para fornecer uma representação de string legível para os objetos, facilitando a depuração.

  O coração do padrão está no método `clone(self)` da classe `Person`, que utiliza `copy.deepcopy()` para criar uma cópia profunda e independente do objeto. O bloco `if __name__ == "__main__":` demonstra o padrão em ação:
  1. Cria um objeto `Person` original.
  2. Clona este objeto para criar um novo.
  3. Modifica o clone.
  4. Imprime ambos os objetos para provar que são instâncias independentes e que a alteração no clone não afetou o original.

- ### `mutáveis-e-imutáveis.txt`
  Este arquivo de texto contextualiza um conceito fundamental para o padrão Prototype em Python: a diferença entre tipos de dados mutáveis e imutáveis.
  - **Mutáveis** (como `list`, `dict`, `set`) são passados por referência. Se uma cópia superficial (shallow copy) for feita, a cópia e o original compartilharão a mesma referência ao objeto mutável.
  - **Imutáveis** (como `str`, `int`, `tuple`) são passados por valor (copiados).

  Entender isso é crucial para perceber por que `deepcopy()` é usado no script: ele garante que até os objetos mutáveis aninhados (como a lista de endereços) sejam clonados, evitando efeitos colaterais.

- ### `prototype.png` e `prototype.graphml`
  Estes são arquivos de diagrama que representam visualmente a estrutura e o funcionamento do padrão Prototype, servindo como um auxílio visual para o estudo.

## Como Executar o Exemplo

Para ver o padrão em funcionamento, basta executar o script principal no seu terminal:
```bash
python prototype-1.py
```

## Conceitos-Chave

- **Clonagem vs. Criação**: O padrão favorece a clonagem de um objeto existente em vez de criar um novo do zero.
- **Deep Copy vs. Shallow Copy**: Para que um clone seja verdadeiramente independente do original, é essencial usar uma cópia profunda (`deepcopy`), especialmente quando o objeto contém outros objetos mutáveis. Uma cópia superficial faria com que ambos os objetos (original e clone) compartilhassem as mesmas referências para os objetos internos.
