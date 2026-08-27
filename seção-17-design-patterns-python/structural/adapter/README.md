# Padrão de Projeto Adapter

Este diretório contém um exemplo do padrão de projeto estrutural **Adapter**. O objetivo do Adapter é permitir que interfaces incompatíveis trabalhem juntas. Ele atua como um invólucro (wrapper) para uma classe existente, convertendo sua interface em outra interface que o cliente espera.

## Arquivos no Diretório

- `adapter-1.py`: Contém a implementação em Python de duas variações do padrão Adapter: **Adapter de Objeto** e **Adapter de Classe**.
- `adapter-class.png` e `adapter-class.graphml`: Diagramas que ilustram a estrutura do Adapter de Classe.
- `adapter-object.png` e `adapter-object.graphml`: Diagramas que ilustram a estrutura do Adapter de Objeto.

## O que foi estudado?

O código em `adapter-1.py` demonstra como integrar uma nova classe (`NewControl`) com um sistema que espera uma interface mais antiga (`IControl`).

### Componentes do Código

1.  **`IControl` (Interface Alvo):**
    - É uma classe abstrata que define a interface que o cliente (o código que usa o controle) espera.
    - Possui os métodos: `top()`, `right()`, `down()`, `left()`.

2.  **`Control` (Classe Cliente):**
    - Uma implementação concreta da interface `IControl`. Representa o sistema original.

3.  **`NewControl` (Classe a ser Adaptada - "Adaptee"):**
    - Esta é a nova classe com uma interface "incompatível". Em vez de `top()`, `right()`, etc., ela usa `move_top()`, `move_right()`, etc.
    - O objetivo é fazer com que esta classe funcione no nosso sistema sem alterar seu código-fonte.

### Tipos de Adapter Implementados

O padrão foi implementado de duas maneiras no arquivo:

#### 1. Adapter de Objeto (`ControlAdapter`)

-   **Como funciona?** Este adaptador utiliza **composição**. Ele "envolve" uma instância da classe `NewControl`.
-   A classe `ControlAdapter` herda da interface `IControl` e implementa os métodos esperados (`top`, `right`, etc.).
-   Dentro de cada método, ele chama o método correspondente do objeto `NewControl` que ele contém. Por exemplo, o método `top()` do adaptador chama `self.new_control.move_top()`.

```python
class ControlAdapter:
    """ Adapter Object """
    def __init__(self, new_control: NewControl) -> None:
        self.new_control = new_control

    def top(self) -> None:
        self.new_control.move_top()
    # ... e assim por diante
```

#### 2. Adapter de Classe (`ControlAdapter2`)

-   **Como funciona?** Este adaptador utiliza **herança múltipla**.
-   A classe `ControlAdapter2` herda tanto da classe base `Control` (para ter a interface `IControl`) quanto da classe `NewControl` (para ter os novos métodos).
-   Ele então sobrepõe os métodos da interface (`top`, `right`, etc.) para chamar os métodos correspondentes da `NewControl` (`move_top`, `move_right`, etc.) que ele herdou.

```python
class ControlAdapter2(Control, NewControl):
    """ Adapter Class """
    def top(self) -> None:
        self.move_top()
    # ... e assim por diante
```

### Resumo

O padrão Adapter é útil quando você precisa integrar uma classe cuja interface não é compatível com o resto do seu código. Em vez de modificar a classe existente (o que nem sempre é possível), você cria um "adaptador" que faz a ponte entre o seu código e a nova classe. A escolha entre o Adapter de Objeto (composição) e o de Classe (herança) depende das necessidades do projeto, mas a composição é frequentemente preferida por ser mais flexível.
