# Padrão de Projeto Comportamental - State

Esta pasta contém exemplos que ilustram o padrão de projeto **State**. O objetivo deste padrão é permitir que um objeto altere seu comportamento quando seu estado interno muda, fazendo com que o objeto pareça ter mudado de classe.

Isso é alcançado criando-se classes separadas para cada estado possível de um objeto "contexto". Cada classe de estado implementa o comportamento específico para aquele estado, e o objeto de contexto simplesmente delega a execução para o objeto de estado atual.

## Vantagens do Padrão State

- **Organiza o código:** Isola a lógica de cada estado em sua própria classe, eliminando a necessidade de grandes e complexos blocos condicionais (`if/elif/else`) no objeto de contexto.
- **Facilita a manutenção e extensão:** Adicionar um novo estado se torna mais simples. Basta criar uma nova classe de estado e ajustar as transições nos estados existentes, sem precisar modificar a lógica do contexto ou de outros estados.
- **Código mais limpo e legível:** O código se torna mais claro, pois o comportamento de cada estado está encapsulado e bem definido em sua respectiva classe.

---

## Arquivos e Exemplos

### 1. `not-state.py`

Este arquivo serve como um **anti-exemplo**, ou seja, uma demonstração do problema que o padrão State se propõe a resolver.

- **`Order` (classe):** Representa um pedido que pode ter diferentes estados de pagamento (`Pending`, `Approved`, `Rejected`).
- **`change_state` (método):** Dentro desta classe, há um método que concentra toda a lógica de transição de estados usando uma longa cadeia de `if/elif/else`.

Observe como este método é complexo e difícil de gerenciar. Qualquer alteração nas regras de transição (por exemplo, "um pagamento recusado não pode ser aprovado") exige uma modificação cuidadosa neste bloco monolítico, o que aumenta a chance de introduzir bugs.

### 2. `state-1.py`

Este é o primeiro exemplo prático do padrão State. Ele refatora o problema apresentado em `not-state.py`.

- **`Order` (classe de contexto):** Agora, a classe `Order` não contém mais a lógica condicional. Ela apenas mantém uma referência ao seu estado atual (um objeto de uma subclasse de `OrderState`). Quando um método como `approve()` é chamado, ele delega a chamada para o objeto de estado atual.

- **`OrderState` (classe abstrata de estado):** Define a interface comum para todos os estados. Garante que todos os estados concretos implementem os mesmos métodos (`pending()`, `approve()`, `reject()`).

- **`PaymentPending`, `PaymentApproved`, `PaymentRejected` (classes de estado concreto):** Cada uma dessas classes implementa o comportamento específico para um estado.
    - `PaymentPending` pode transicionar para `Approved` ou `Rejected`.
    - `PaymentApproved` não pode ser aprovado novamente.
    - `PaymentRejected` bloqueia a maioria das ações.

Este exemplo mostra como a responsabilidade de gerenciar as transições de estado é distribuída entre as classes de estado, tornando o sistema mais limpo e organizado.

### 3. `state-2.py`

Este é outro exemplo prático, que simula o comportamento de um aparelho de som que pode operar em diferentes modos (Rádio ou Música).

- **`Sound` (classe de contexto):** Representa o aparelho de som. Ele possui um "modo" (`mode`), que é o seu estado atual.

- **`PlayMode` (classe abstrata de estado):** Define a interface para os modos de reprodução, com os métodos `press_next()` e `press_prev()`.

- **`RadioMode`, `MusicMode` (classes de estado concreto):**
    - Em `RadioMode`, os botões `next` e `prev` mudam a frequência em grandes saltos (ex: +1000).
    - Em `MusicMode`, os mesmos botões mudam a faixa de música de um em um (ex: +1).

Este exemplo demonstra de forma clara como o **mesmo método** (`press_next()`) produz um **comportamento completamente diferente** dependendo do estado atual do objeto `Sound`. O objeto "muda seu comportamento" ao mudar de estado.

### Arquivos de Diagrama (`.graphml` e `.png`)

- **`state-1.graphml` / `state-1.png`:** Diagrama visual do fluxo de estados implementado em `state-1.py`.
- **`state-2.graphml` / `state-2.png`:** Diagrama visual do fluxo de estados implementado em `state-2.py`.

Estes diagramas ajudam a visualizar as transições possíveis entre os diferentes estados em cada exemplo.
