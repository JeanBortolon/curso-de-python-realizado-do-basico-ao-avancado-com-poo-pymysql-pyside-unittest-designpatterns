# Padrão de Projeto Decorator

Este diretório contém exemplos do padrão de projeto **Decorator**. O objetivo deste padrão é adicionar novas funcionalidades a um objeto dinamicamente, sem alterar sua estrutura. Isso é feito envolvendo o objeto original em um ou mais "decoradores" que contêm os novos comportamentos.

## O que foi estudado?

O padrão Decorator é um padrão de projeto estrutural que permite adicionar novos comportamentos a objetos, envolvendo-os em "wrappers" (decoradores).

A principal vantagem do Decorator é a flexibilidade. Em vez de criar subclasses para cada combinação de funcionalidades, você pode "decorar" um objeto base com as funcionalidades que desejar, em tempo de execução.

### Estrutura do Padrão

- **Componente**: A interface ou classe abstrata que define os métodos que serão implementados pelos objetos concretos e pelos decoradores. No nosso exemplo, a classe `Hotdog`.
- **Componente Concreto**: A classe do objeto original ao qual queremos adicionar funcionalidades. Em nossos exemplos, são `SimpleHotdog` e `SpecialHotdog`.
- **Decorador**: A classe abstrata que envolve o componente. Ela mantém uma referência ao objeto componente e implementa a mesma interface do componente. Em `decorator-2.py`, `HotdogDecorator` é a classe base para os decoradores.
- **Decorador Concreto**: A classe que implementa as novas funcionalidades. Ela adiciona seu próprio comportamento antes ou depois de delegar a chamada para o objeto componente. No `decorator-2.py`, `BaconDecorator` é um exemplo.

## Arquivos de Exemplo

Temos dois arquivos principais que ilustram o padrão Decorator:

1.  `decorator-1.py`: Uma abordagem mais flexível e genérica.
2.  `decorator-2.py`: Uma implementação mais clássica do padrão.

---

### 1. `decorator-1.py`

Neste arquivo, o padrão Decorator é implementado de uma forma mais genérica. Temos uma única classe `HotdogDecorator` que pode ser usada para adicionar qualquer ingrediente a um hotdog.

**Como funciona:**

1.  A classe `Hotdog` define a interface para nossos hotdogs.
2.  `SimpleHotdog` e `SpecialHotdog` são os nossos objetos base.
3.  A classe `HotdogDecorator` é o nosso decorador. Ao ser instanciada, ela recebe o `hotdog` a ser decorado e o `ingredient` a ser adicionado.
4.  O `HotdogDecorator` então cria uma nova lista de ingredientes (copiando os do hotdog original e adicionando o novo) e recalcula o preço.

**Trecho de Código:**

```python
# decorator-1.py

# Decorador Abstrato / Concreto
# HotdogDecorator atua como um decorador concreto, estendendo a funcionalidade de Hotdog.
class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog, ingredient: Ingredient) -> None:
        # Armazena a instância do hotdog sendo decorado
        self.hotdog = hotdog
        # Armazena o novo ingrediente a ser adicionado
        self._ingredient = ingredient

        # Copia os ingredientes do hotdog original e adiciona o novo ingrediente
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def name(self) -> str:
        # Altera o nome para refletir o ingrediente adicionado
        return f'{self.hotdog.name} +{self._ingredient.__class__.__name__}'
```

**Uso:**

```python
# decorator-1.py

# Decorando um hotdog simples com bacon
bacon_simple_hotdog = HotdogDecorator(simple_hotdog, Bacon())

# Decorando com mais um ingrediente
egg_bacon_simple_hotdog = HotdogDecorator(bacon_simple_hotdog, Egg())
```

Esta abordagem é muito flexível, pois não precisamos criar uma nova classe de decorador para cada ingrediente.

---

### 2. `decorator-2.py`

Este arquivo mostra uma implementação mais tradicional do padrão Decorator. Aqui, temos uma classe de decorador específica para cada ingrediente que queremos adicionar.

**Como funciona:**

1.  A classe `Hotdog` continua sendo a nossa interface.
2.  `SimpleHotdog` e `SpecialHotdog` são os objetos base.
3.  `HotdogDecorator` é uma classe abstrata que serve como base para todos os decoradores concretos. Ela apenas "envolve" o hotdog.
4.  Para cada ingrediente, criamos um decorador concreto, como `BaconDecorator`, que herda de `HotdogDecorator` e adiciona o ingrediente e seu comportamento (preço, nome).

**Trecho de Código:**

```python
# decorator-2.py

# Decorador base
class HotdogDecorator(Hotdog):
    def __init__(self, hotdog: Hotdog) -> None:
        self.hotdog = hotdog
    # ... delega as chamadas para self.hotdog

# Decorador concreto
class BaconDecorator(HotdogDecorator):
    def __init__(self, hotdog: Hotdog) -> None:
        super().__init__(hotdog)
        self._ingredient = Bacon()
        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def price(self) -> float:
        # ... recalcula o preço
    # ...
```

**Uso:**

```python
# decorator-2.py

# Decorando o hotdog simples com Bacon.
bacon_simple_hotdog = BaconDecorator(simple_hotdog)

# Decorando com duplo bacon
bacon_simple_hotdog_2 = BaconDecorator(bacon_simple_hotdog)
```

Essa abordagem é mais verbosa, pois exige uma classe para cada "decoração", mas pode ser mais clara se os decoradores tiverem lógicas muito diferentes entre si.

## Conclusão

Ambos os exemplos demonstram como o padrão Decorator pode ser usado para estender a funcionalidade de objetos de forma flexível. A escolha entre uma abordagem genérica (`decorator-1.py`) e uma específica (`decorator-2.py`) depende das necessidades do projeto. Para o nosso exemplo de hotdog, a abordagem genérica é mais simples e escalável.

Os arquivos `.png` e `.graphml` são representações visuais do diagrama de classes UML para este padrão.
