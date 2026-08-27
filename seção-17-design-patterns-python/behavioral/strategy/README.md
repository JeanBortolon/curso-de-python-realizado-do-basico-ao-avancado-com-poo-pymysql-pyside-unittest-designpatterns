# Padrão de Projeto Strategy (Comportamental)

Este diretório contém um exemplo prático do padrão de projeto **Strategy** em Python.

## O que é o Padrão Strategy?

O padrão Strategy é um padrão de projeto comportamental que permite definir uma família de algoritmos, encapsular cada um deles e torná-los intercambiáveis. Isso significa que você pode mudar o algoritmo usado por um objeto em tempo de execução sem modificar o objeto em si.

Em termos simples, pense em como você pagaria por algo: você pode pagar em dinheiro, com cartão de crédito ou por Pix. Cada método de pagamento é uma "estratégia" diferente para realizar o pagamento. O sistema que recebe o pagamento (o "contexto") não precisa saber os detalhes de como cada método funciona; ele apenas usa a estratégia que você escolheu.

### Componentes Principais:

1.  **Contexto (Context):** É a classe que usa uma das estratégias. Ela mantém uma referência a um objeto Strategy e delega a execução do algoritmo a esse objeto. **Não conhece os detalhes da implementação da estratégia.**
2.  **Estratégia Abstrata (Abstract Strategy/Interface):** Define uma interface comum para todas as estratégias concretas. Essa interface declara o método que o Contexto usará para executar o algoritmo.
3.  **Estratégias Concretas (Concrete Strategies):** Implementam a interface da Estratégia Abstrata, fornecendo a implementação específica de um algoritmo.

## `strategy-1.py` - Exemplo de Aplicação

O arquivo `strategy-1.py` demonstra o padrão Strategy aplicando diferentes políticas de desconto a um pedido (`Order`).

### Classes no Exemplo:

*   **`Order` (Contexto):** Representa um pedido de compra. Ele armazena o valor total do pedido e tem uma referência a um objeto de `DiscountStrategy`. Quando o total com desconto é solicitado, ele delega o cálculo à estratégia de desconto atualmente configurada.
    ```python
    class Order:
        def __init__(self, total: float, discount: DiscountStrategy):
            self._total = total
            self._discount = discount

        @property
        def total_with_discount(self):
            return self._discount.calculate(self.total)
    ```
*   **`DiscountStrategy` (Estratégia Abstrata):** Uma classe abstrata que define a interface para todas as estratégias de desconto. Qualquer estratégia de desconto concreta deve implementar o método `calculate(self, value: float)`.
    ```python
    class DiscountStrategy(ABC):
        @abstractmethod
        def calculate(self, value: float) -> float:
            pass
    ```
*   **Estratégias Concretas de Desconto:**
    *   **`TwentyPercent`:** Aplica um desconto fixo de 20%.
    *   **`FiftyPercent`:** Aplica um desconto fixo de 50%.
    *   **`NoDiscount`:** Não aplica nenhum desconto, retornando o valor original.
    *   **`CustomDiscount`:** Permite especificar uma porcentagem de desconto personalizada no momento da criação da estratégia.

### Como Funciona:

O `Order` (contexto) não contém a lógica de como calcular cada tipo de desconto. Em vez disso, ele recebe um objeto `DiscountStrategy` (estratégia) em seu construtor. Quando `total_with_discount` é chamado, o `Order` simplesmente invoca o método `calculate` do objeto `DiscountStrategy` que lhe foi fornecido.

Isso significa que você pode ter um `Order` que aplica 20% de desconto, e depois criar outro `Order` (ou até mesmo alterar a estratégia de um `Order` existente, se a arquitetura permitisse) que aplica 50% de desconto ou um desconto personalizado, tudo isso sem precisar modificar a classe `Order`.

### Vantagens:

*   **Flexibilidade:** Permite trocar algoritmos em tempo de execução.
*   **Princípio Aberto/Fechado (Open/Closed Principle):** A classe `Order` (contexto) é "fechada para modificação" (não precisa ser alterada quando novas estratégias são adicionadas), mas "aberta para extensão" (você pode facilmente adicionar novas estratégias de desconto).
*   **Isolamento:** Cada estratégia é encapsulada em sua própria classe, mantendo o código organizado e fácil de entender.
*   **Reusabilidade:** As estratégias podem ser reutilizadas em diferentes contextos ou com diferentes objetos.

### Outros arquivos:

*   **`strategy.graphml` e `strategy.png`:** Provavelmente são arquivos relacionados a diagramas (como UML) que visualizam a estrutura e o fluxo do padrão Strategy, ajudando a entender a relação entre o Contexto, a Estratégia Abstrata e as Estratégias Concretas.

Este padrão é ideal quando você tem várias maneiras de realizar uma tarefa e deseja que o cliente (Contexto) possa escolher entre elas sem se preocupar com os detalhes da implementação.
