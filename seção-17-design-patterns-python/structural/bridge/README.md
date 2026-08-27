# Padrão de Projeto Estrutural: Bridge

Este diretório contém um exemplo do padrão de projeto **Bridge**. O objetivo deste padrão é desacoplar uma abstração de sua implementação, permitindo que ambas possam evoluir de forma independente. Pense nisso como ter um controle remoto (a abstração) que pode controlar diferentes aparelhos (as implementações), sem que o controle remoto precise conhecer os detalhes específicos de cada aparelho.

## Arquivos no Diretório

*   `bridge-1.py`: Contém o código Python que demonstra o padrão Bridge.
*   `bridge.png`: Um diagrama visual que ilustra a estrutura do padrão Bridge aplicado neste exemplo.
*   `bridge.graphml`: Arquivo de dados do gráfico, usado para gerar o diagrama.

## Entendendo o Código (`bridge-1.py`)

O exemplo utiliza uma analogia com controles remotos e aparelhos eletrônicos para ilustrar o padrão.

### Componentes Principais

1.  **Abstração (`IRemoteControl`, `RemoteControl`, `RemoteControlWithMute`)**:
    *   `IRemoteControl`: É a interface da abstração, definindo os métodos que um controle remoto deve ter (`increase_volume`, `decrease_volume`, `power`).
    *   `RemoteControl`: É a abstração principal. Ela não executa o trabalho diretamente, mas sim delega a chamada para um objeto de "implementação" (um aparelho). Ela possui uma referência a um `IDevice`.
    *   `RemoteControlWithMute`: É uma abstração refinada, que herda de `RemoteControl` e adiciona uma nova funcionalidade (`mute`), mostrando que podemos estender a abstração sem impactar as implementações.

2.  **Implementação (`IDevice`, `TV`, `Radio`)**:
    *   `IDevice`: É a interface da implementação, que define os métodos que um aparelho deve ter (`volume`, `power`). Note que esta interface não precisa ser igual à da abstração.
    *   `TV` e `Radio`: São as implementações concretas. Elas contêm a lógica real para ligar/desligar e controlar o volume. Novos aparelhos podem ser adicionados sem precisar modificar as classes de controle remoto.

### Como Funciona a "Ponte" (Bridge)?

A "ponte" é a conexão que `RemoteControl` faz com `IDevice`. O `RemoteControl` (abstração) tem um `_device` (implementação) e, quando um de seus métodos é chamado (como `increase_volume`), ele simplesmente repassa a chamada para o `_device` correspondente.

```python
# Abstração delegando para a Implementação
def increase_volume(self) -> None:
    self._device.volume += 10
```

Isso permite que você troque o aparelho que está sendo controlado por um mesmo controle remoto sem que o controle precise saber. Você pode criar um `RemoteControl` para uma `TV` ou para um `Radio`, e o código do `RemoteControl` permanece o mesmo.

## Conclusão

O padrão Bridge é útil quando você precisa:
*   Evitar um acoplamento permanente entre uma abstração e sua implementação.
*   Permitir que tanto a abstração quanto a implementação possam ser estendidas por subclasses de forma independente.
*   Modificar a implementação em tempo de execução.

Ele promove um código mais flexível e de fácil manutenção, separando as preocupações de alto nível (o que o controle faz) das de baixo nível (como o aparelho executa a ação).
