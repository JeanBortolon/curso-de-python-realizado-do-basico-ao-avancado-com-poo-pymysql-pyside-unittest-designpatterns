# Padrão de Projeto Comportamental - Mediator

O padrão **Mediator** tem como objetivo principal reduzir a complexidade e o acoplamento entre múltiplos objetos. Ele faz isso centralizando a comunicação em um único objeto, o "mediador". Em vez de os objetos se comunicarem diretamente uns com os outros, eles enviam suas mensagens ao mediador, que se encarrega de encaminhá-las aos destinatários corretos.

Isso promove um baixo acoplamento, pois os objetos (chamados de *Colleagues*) não precisam mais conhecer a existência uns dos outros. Eles dependem apenas da interface do mediador.

## Arquivos no Diretório

-   `mediator.py`: Contém a implementação em Python do padrão Mediator, com um exemplo prático de uma sala de bate-papo (`Chatroom`).
-   `mediator-1.png` e `mediator-2.png`: Diagramas visuais que ilustram a estrutura e o funcionamento do padrão Mediator.
-   `mediator-1.graphml` e `mediator-2.graphml`: Arquivos de origem dos diagramas, provavelmente criados em um editor de grafos.

## Explicação do Código (`mediator.py`)

O código simula uma sala de bate-papo, um exemplo clássico para demonstrar o padrão Mediator.

### Componentes do Padrão

1.  **Mediator (`Mediator`)**:
    -   É uma classe abstrata que define a interface de comunicação para os *Colleagues*.
    -   Declara os métodos que os *Colleagues* usarão para se comunicar, como `broadcast` (enviar para todos) e `direct` (enviar para um específico).

2.  **Concrete Mediator (`Chatroom`)**:
    -   É a implementação concreta do `Mediator`.
    -   Gerencia uma lista de *Colleagues* (no caso, `Person`).
    -   Implementa a lógica de comunicação: sabe como encaminhar uma mensagem de `broadcast` para todos os participantes (exceto o remetente) e como direcionar uma mensagem `direct` para o destinatário correto.
    -   Possui métodos para adicionar e remover participantes da sala (`add`, `remove`).

3.  **Colleague (`Colleague`)**:
    -   É uma classe abstrata que define a interface para os objetos que serão mediados.
    -   Cada *Colleague* conhece seu `Mediator`.
    -   Declara métodos para enviar mensagens (`broadcast`) e para receber mensagens (`direct`).

4.  **Concrete Colleague (`Person`)**:
    -   É a implementação concreta do `Colleague`.
    -   No construtor, recebe seu nome e uma instância do `Mediator` (`Chatroom`).
    -   Quando uma pessoa quer enviar uma mensagem, ela não a envia diretamente para outra pessoa. Em vez disso, ela chama um método do mediador (`self.mediator.broadcast(...)` ou `self.mediator.direct(...)`) e confia que o mediador fará a entrega.
    -   O método `direct` em `Person` é, na verdade, o método que o mediador chama para *entregar* uma mensagem a essa pessoa.

### Como Funciona na Prática

1.  **Configuração**:
    -   Primeiro, criamos uma instância do `Chatroom` (o mediador).
    -   Em seguida, criamos várias instâncias de `Person` (os colegas), passando o `Chatroom` para cada uma delas no construtor.
    -   Adicionamos as pessoas à sala de bate-papo usando o método `chat.add(...)`.

2.  **Comunicação**:
    -   Quando `joao.broadcast('Olá!')` é chamado, o objeto `joao` não sabe quem são `maria` ou `elis`. Ele apenas diz ao `chat`: "Ei, `Chatroom`, envie esta mensagem para todos."
    -   O `Chatroom`, que conhece todos os participantes, percorre sua lista e entrega a mensagem a cada um deles (exceto ao próprio João).
    -   O mesmo acontece com mensagens diretas: `joao.send_direct('Maria', 'Oi!')` informa ao `Chatroom` para encontrar o participante com o nome "Maria" e entregar a mensagem a ele.

### Vantagens

-   **Baixo Acoplamento**: Os objetos `Person` não estão acoplados entre si. Se uma nova pessoa entrar na sala ou sair, apenas o `Chatroom` precisa saber.
-   **Centralização do Controle**: A lógica de comunicação, que poderia estar espalhada por várias classes, fica centralizada no `Chatroom`, tornando o sistema mais fácil de entender e manter.
-   **Reutilização**: A classe `Person` pode ser reutilizada em diferentes implementações de `Chatroom` sem nenhuma modificação.

Este padrão é muito útil em sistemas onde um conjunto de objetos precisa se comunicar de maneiras complexas, pois simplifica as interações e melhora a organização do código.
