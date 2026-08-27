# Padrão de Projeto: Chain of Responsibility (Cadeia de Responsabilidade)

O padrão de projeto **Chain of Responsibility** é um padrão comportamental que permite que uma solicitação seja passada ao longo de uma cadeia de objetos (handlers) até que um deles a processe. Isso desacopla o remetente da solicitação de seus possíveis receptores, pois o remetente não precisa saber qual objeto em específico tratará a solicitação.

## Como funciona?

1.  **Remetente da solicitação**: Cria uma solicitação e a envia para o primeiro objeto da cadeia.
2.  **Handlers**: Cada objeto na cadeia (handler) decide se pode processar a solicitação ou se deve passá-la para o próximo handler na cadeia.
3.  **Encadeamento**: Se um handler não puder processar a solicitação, ele a encaminha para o próximo handler pré-definido na sequência.
4.  **Fim da cadeia**: A solicitação viaja pela cadeia até que um handler a processe ou até o final da cadeia ser atingido (geralmente com um handler "padrão" que lida com todas as solicitações não tratadas).

## Benefícios

*   **Acoplamento reduzido**: O remetente da solicitação não está diretamente acoplado a nenhum handler específico.
*   **Flexibilidade**: A ordem dos handlers pode ser alterada e novos handlers podem ser adicionados à cadeia sem modificar o código existente do cliente.
*   **Responsabilidade única**: Cada handler tem uma única responsabilidade: decidir se trata a solicitação ou a passa adiante.

## Arquivos neste diretório

### `chain-of-responsibility-1.py`

Este arquivo demonstra uma implementação simplificada do padrão Chain of Responsibility utilizando **funções**.

*   Cada função (`handler_ABC`, `handler_DEF`, `handler_unsolved`) atua como um "handler".
*   As funções `handler_ABC` e `handler_DEF` verificam se conseguem processar uma determinada letra.
*   Se uma função não puder tratar a letra, ela invoca a próxima função na cadeia.
*   A função `handler_unsolved` é o handler final, que informa que a letra não pôde ser tratada por nenhum handler anterior.

Este exemplo é útil para entender o conceito básico da cadeia de responsabilidade de forma procedural.

### `chain-of-responsibility-2.py`

Este arquivo apresenta uma implementação mais clássica e orientada a objetos do padrão Chain of Responsibility, utilizando **classes**.

*   **`Handler` (Classe Abstrata)**: Define a interface comum para todos os handlers e geralmente contém a lógica para passar a solicitação ao próximo handler na cadeia.
*   **`HandlerABC` e `HandlerDEF` (Classes Concretas)**: Implementam a lógica de tratamento específica. Cada um deles decide se processa a solicitação ou a encaminha para seu `sucessor`.
*   **`HandlerUnsolved` (Classe Concreta)**: É o último handler da cadeia. Ele trata qualquer solicitação que chegue a ele, geralmente indicando que a solicitação não foi processada por nenhum dos handlers anteriores.
*   A cadeia é construída explicitamente, onde cada handler conhece apenas o seu sucessor direto.

Esta implementação é mais robusta e escalável para cenários complexos.

### `chain-of-responsibility.graphml` e `chain-of-responsibility.png`

Estes arquivos provavelmente contêm diagramas visuais que representam a estrutura do padrão Chain of Responsibility, facilitando a compreensão de como os handlers estão encadeados e como a solicitação flui através deles. O `.png` é uma imagem do diagrama, e o `.graphml` é o arquivo fonte do diagrama (possivelmente criado com o software yEd Graph Editor ou similar).
