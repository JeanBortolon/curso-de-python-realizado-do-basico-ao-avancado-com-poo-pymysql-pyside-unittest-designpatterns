# Padrão de Projeto Comportamental - Command

## Visão Geral

O padrão de projeto **Command** tem como principal objetivo encapsular uma solicitação (um "comando") como um objeto. Isso permite que você parametrize clientes com diferentes solicitações, enfileire ou registre (log) de solicitações, e suporte operações que podem ser desfeitas (undo).

Essencialmente, ele desacopla o objeto que invoca uma operação do objeto que sabe como realizá-la.

## Estrutura do Padrão

O padrão Command é composto por quatro partes principais:

1.  **Receiver (Receptor)**: O objeto que efetivamente executa a ação. É ele quem sabe como realizar o trabalho. No nosso exemplo, a classe `Light` é um Receiver.

2.  **Command (Comando)**: Uma interface ou classe abstrata que declara um método para executar uma ação (geralmente chamado de `execute`). Ele pode, opcionalmente, declarar um método para desfazer a ação (`undo`). A interface `ICommand` em nosso código representa isso.

3.  **ConcreteCommand (Comando Concreto)**: A implementação da interface `Command`. Ele mantém uma referência ao `Receiver` e implementa o método `execute` chamando a ação apropriada no `Receiver`. As classes `LightOnCommand` e `LightChangeColor` são exemplos de Comandos Concretos.

4.  **Invoker (Invocador)**: O objeto que solicita a execução de um comando. Ele não sabe nada sobre o `Receiver` ou a operação que está sendo executada; ele apenas invoca o método `execute` do objeto `Command`. Em nosso exemplo, a classe `RemoteController` atua como o `Invoker`.

5.  **Client (Cliente)**: O cliente é responsável por criar o `Receiver`, o `ConcreteCommand` e o `Invoker`, e associá-los. O bloco `if __name__ == "__main__":` do nosso script é o `Client`.

## Arquivos no Diretório

*   `command-1.py`:
    *   Este é o arquivo principal que contém a implementação do padrão Command em Python.
    *   Ele simula um sistema de controle de luzes inteligentes.
    *   **`Light`**: A classe `Receiver`, representa uma luz que pode ser ligada, desligada e ter sua cor alterada.
    *   **`ICommand`**: A interface abstrata para os comandos.
    *   **`LightOnCommand` e `LightChangeColor`**: Comandos concretos que encapsulam as ações de ligar a luz e mudar de cor. Eles também implementam a lógica para desfazer (`undo`) suas ações.
    *   **`RemoteController`**: O `Invoker`, que representa um controle remoto com botões. Cada botão é associado a um comando. Ele também mantém um histórico de ações para permitir o `undo` global.
    *   O código demonstra como o cliente configura os botões do controle remoto com diferentes comandos e como as ações podem ser executadas e desfeitas.

*   `command.png`:
    *   Uma imagem que representa visualmente a estrutura do padrão Command, mostrando como as diferentes partes (Client, Invoker, Command, Receiver) se relacionam. É um diagrama de classes que ajuda a entender a arquitetura do padrão.

*   `command.graphml`:
    *   Este é o arquivo-fonte do diagrama, provavelmente criado em uma ferramenta de diagramação como o yEd ou similar, que exportou a imagem `command.png`. Ele pode ser usado para editar o diagrama.

## Como Funciona

1.  O **Cliente** cria os objetos: uma ou mais luzes (`Light`), os comandos para interagir com essas luzes (`LightOnCommand`, `LightChangeColor`) e o controle remoto (`RemoteController`).
2.  O **Cliente** então "programa" o controle remoto, associando cada botão a um comando específico.
3.  Quando um botão no controle remoto (`Invoker`) é pressionado, ele chama o método `execute()` do comando associado àquele botão.
4.  O objeto de comando (`ConcreteCommand`), por sua vez, chama o método de ação apropriado no `Receiver` (a `Light`).
5.  O `Invoker` pode manter um histórico de comandos executados para implementar a funcionalidade de "desfazer". Quando o `undo` é solicitado, ele pega o último comando executado e chama seu método `undo()`.

A grande vantagem aqui é que o `RemoteController` não precisa saber nada sobre luzes. Ele só sabe que tem botões e que cada botão, quando pressionado, executa *algo*. Isso torna o sistema muito flexível e extensível. Poderíamos adicionar comandos para controlar a porta da garagem, o sistema de som ou qualquer outro dispositivo sem modificar o `RemoteController`.
