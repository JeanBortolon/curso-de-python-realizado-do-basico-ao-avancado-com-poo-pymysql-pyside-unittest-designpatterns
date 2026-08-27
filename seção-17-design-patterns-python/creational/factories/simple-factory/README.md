# Padrão de Projeto: Simple Factory (Fábrica Simples)

Esta pasta contém exemplos que demonstram o padrão de projeto **Simple Factory**. O objetivo de uma fábrica é centralizar a criação de objetos, desacoplando o código cliente das classes concretas que ele precisa instanciar.

## O que é uma "Factory" (Fábrica)?

Em programação orientada a objetos, uma "fábrica" é uma classe ou um método cuja principal responsabilidade é criar outros objetos. Em vez de o código cliente criar um objeto diretamente (ex: `carro = CarroLuxo()`), ele pede à fábrica para criar o objeto para ele (ex: `carro = Fabrica.criar_veiculo('luxo')`).

### Vantagens

*   **Baixo Acoplamento**: O código cliente não precisa saber qual classe concreta está sendo usada. Ele só conhece a fábrica e a interface (classe abstrata) do objeto que recebe.
*   **Flexibilidade**: Para adicionar um novo tipo de produto (ex: `Caminhao`), você só precisa criá-lo e modificar a fábrica. O código cliente não precisa ser alterado.
*   **Centralização**: A lógica de qual objeto criar fica em um único lugar, facilitando a manutenção.

---

## Arquivos na Pasta

Temos dois arquivos que, apesar de muito parecidos, mostram duas abordagens diferentes para implementar uma Simple Factory.

### 1. `simple-factory-1.py`

Esta é a implementação mais comum e direta de uma Simple Factory.

#### Como Funciona?

1.  **Interface `Veiculo`**: Uma classe abstrata que define o que todos os veículos devem fazer (o método `buscar_cliente()`).
2.  **Classes Concretas**: `CarroLuxo`, `CarroPopular`, `MotoLuxo`, etc. são as implementações reais dos veículos.
3.  **`VeiculoFactory`**:
   *   Possui um **método estático** `get_carro(tipo)`. Um método estático pertence à classe, não a uma instância dela.
   *   O cliente chama `VeiculoFactory.get_carro('popular')` para obter um veículo.
   *   O método usa uma série de `if`s para decidir qual objeto criar com base na string `tipo`.
   *   Ele retorna a **instância do veículo criado** diretamente para o cliente.

#### Exemplo de Uso no Código:

```python
# O cliente pede um carro para a CLASSE da fábrica
carro = VeiculoFactory.get_carro('luxo')

# O cliente usa o objeto recebido
carro.buscar_cliente()
```

Neste caso, a fábrica é apenas um "intermediário" que entrega o produto final. O cliente interage diretamente com o produto (`CarroLuxo`, `CarroPopular`, etc.).

---

### 2. `simple-factory-2.py`

Esta versão mostra uma abordagem um pouco diferente, onde a fábrica atua como um "embrulho" (wrapper) para o objeto criado.

#### Como Funciona?

1.  **Interface e Classes Concretas**: São as mesmas do primeiro arquivo.
2.  **`VeiculoFactory`**:
    *   O cliente agora **cria uma instância** da própria fábrica: `fabrica = VeiculoFactory('popular')`.
    *   No construtor (`__init__`), a fábrica chama seu próprio método `get_carro(tipo)` e armazena o veículo criado internamente (em `self.carro`).
    *   A fábrica possui seus próprios métodos (como `buscar_cliente()`), que simplesmente **delegam a chamada** para o objeto de veículo que ela guarda.

#### Exemplo de Uso no Código:

```python
# O cliente cria uma INSTÂNCIA da fábrica
fabrica_de_carro = VeiculoFactory('popular')

# O cliente chama o método na PRÓPRIA FÁBRICA
fabrica_de_carro.buscar_cliente()
```

Aqui, o cliente não interage com o `CarroPopular` diretamente. Ele interage com a `VeiculoFactory`, que por sua vez repassa a ação para o carro que ela criou e escondeu.

---

## Resumo das Diferenças

| Característica | `simple-factory-1.py` (Método Estático) | `simple-factory-2.py` (Instância Delegadora) |
| :--- | :--- | :--- |
| **Como o cliente usa?** | Chama um método na classe da fábrica: `VeiculoFactory.get_carro()` | Cria um objeto da fábrica: `VeiculoFactory()` |
| **O que o cliente recebe?** | O objeto final (o veículo). | O objeto da fábrica (que contém o veículo). |
| **Com quem o cliente fala?** | Com o veículo retornado pela fábrica. | Com a instância da fábrica. |
| **Analogia** | Pedir um lanche no balcão e recebê-lo para comer. | Pedir um "combo" que já vem com o lanche dentro, e você interage com a caixa do combo. |

Ambas as abordagens alcançam o objetivo de desacoplar o cliente da criação de objetos, mas a primeira (`simple-factory-1.py`) é a representação mais clássica e simples do padrão Simple Factory.

