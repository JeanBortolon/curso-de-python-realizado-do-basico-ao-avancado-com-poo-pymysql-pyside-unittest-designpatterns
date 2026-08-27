# 🏭 Padrão de Projeto: Factory Method (Método de Fábrica)

Este documento serve como um guia para entender o padrão de projeto criacional **Factory Method**, explicando seu propósito, estrutura e como aplicá-lo em Python de forma clara e didática.

## 🎯 O Problema que o Factory Method Resolve

Imagine que você está criando um sistema de logística. Inicialmente, seu aplicativo só precisa lidar com transporte por caminhões. O código para criar um objeto `Caminhao` está espalhado por toda a sua aplicação.

```python
# Em vários lugares do seu código...
transporte = Caminhao()
transporte.entregar()
```

Agora, seu cliente pede para adicionar transporte por navios. O que você faz? Você teria que procurar em todo o seu código onde `Caminhao()` é chamado e adicionar uma lógica condicional (`if/else`) para decidir se cria um `Caminhao` ou um `Navio`.

```python
# Código se torna mais complexo
if tipo_transporte == 'TERRESTRE':
    transporte = Caminhao()
else if tipo_transporte == 'MARITIMO':
    transporte = Navio()

transporte.entregar()
```

Isso torna o código **acoplado** e difícil de manter. A cada novo tipo de transporte (trem, avião), você teria que modificar mais e mais lugares. O Factory Method resolve exatamente isso!

## 🚀 A Solução: O que é o Factory Method?

O **Factory Method** é um padrão de projeto que propõe a criação de objetos por meio de um "método de fábrica" em vez de chamar o construtor da classe diretamente (`new` ou `Classe()`). [3, 17]

A ideia principal é:
1.  Definir uma **interface** (ou classe abstrata) para os objetos que serão criados (os "produtos", como `Transporte`).
2.  Definir uma **classe criadora** (a "fábrica") que possui um método abstrato para criar esses produtos (o `factory_method`).
3.  As **subclasses da fábrica** (fábricas concretas) decidem qual classe concreta de produto instanciar. [3]

Dessa forma, o código cliente (que usa os objetos) não precisa saber qual classe concreta está sendo criada. Ele apenas pede à fábrica para "criar um objeto", e a fábrica se encarrega dos detalhes. [19] Isso diminui o acoplamento e torna o sistema mais flexível. [2, 6]

## 🏗️ Estrutura do Padrão

O padrão é composto por quatro partes principais:

1.  **Product (Produto)**: A interface ou classe abstrata para os objetos que a fábrica irá criar. (Ex: `Transporte`)
2.  **ConcreteProduct (Produto Concreto)**: As implementações reais da interface do produto. (Ex: `Caminhao`, `Navio`)
3.  **Creator (Criador/Fábrica)**: A classe que declara o `factory_method`. Ela pode ter uma implementação padrão ou ser totalmente abstrata.
4.  **ConcreteCreator (Criador Concreto)**: As subclasses que implementam o `factory_method` para retornar uma instância de um `ConcreteProduct` específico.

## 🐍 Exemplo em Python: Sistema de Logística

Vamos aplicar o padrão ao nosso problema de logística.

### 1. Arquivos do Projeto (Exemplo)

```
factory-method/
├── main.py                 # Código cliente que usa a fábrica
└── veiculos.py             # Definição dos produtos e fábricas
```

### 2. Código (`veiculos.py`)

```python
from abc import ABC, abstractmethod

# 1. Product (Interface do Produto)
class Veiculo(ABC):
    @abstractmethod
    def entregar(self, nome_cliente: str) -> None: pass

# 2. ConcreteProducts (Produtos Concretos)
class Carro(Veiculo):
    def entregar(self, nome_cliente: str) -> None:
        print(f"Carro está entregando para {nome_cliente}")

class Moto(Veiculo):
    def entregar(self, nome_cliente: str) -> None:
        print(f"Moto está entregando para {nome_cliente}")

# 3. Creator (Fábrica Abstrata)
class FabricaVeiculos(ABC):
    @abstractmethod
    def criar_veiculo(self) -> Veiculo: pass

# 4. ConcreteCreators (Fábricas Concretas)
class FabricaCarros(FabricaVeiculos):
    def criar_veiculo(self) -> Veiculo:
        return Carro()

class FabricaMotos(FabricaVeiculos):
    def criar_veiculo(self) -> Veiculo:
        return Moto()
```

### 3. Código (`main.py`)

```python
from veiculos import FabricaCarros, FabricaMotos

if __name__ == "__main__":
    # Usando a fábrica de carros
    fabrica_carros = FabricaCarros()
    carro = fabrica_carros.criar_veiculo()
    carro.entregar("Ana")

    # Usando a fábrica de motos
    fabrica_motos = FabricaMotos()
    moto = fabrica_motos.criar_veiculo()
    moto.entregar("João")
```

**Explicação:**

- O `main.py` (código cliente) não sabe mais sobre `Carro` ou `Moto`. Ele apenas interage com a `FabricaVeiculos`.
- Se precisarmos adicionar um `Drone` como meio de transporte, basta criar a classe `Drone` e a `FabricaDrones`, sem precisar alterar o código cliente existente. Isso segue o **Princípio Aberto/Fechado**. [18]

## ✅ Vantagens do Factory Method

1.  **Baixo Acoplamento**: O código que usa os produtos não depende das classes concretas desses produtos. [19]
2.  **Flexibilidade e Extensibilidade**: Adicionar novos tipos de produtos é fácil. Basta criar uma nova classe de produto e uma nova fábrica. [3]
3.  **Centralização da Lógica de Criação**: A lógica para instanciar objetos fica em um único lugar, facilitando a manutenção. [8, 19]

## 👎 Desvantagens

- **Aumento do número de classes**: O padrão pode introduzir muitas classes novas (fábricas concretas), o que pode tornar o código mais complexo se o número de produtos for grande. [2, 18]

## 💡 Quando Usar?

- Quando uma classe não pode antecipar a classe dos objetos que precisa criar. [2]
- Quando você quer dar às subclasses a responsabilidade de especificar os objetos que elas criam.
- Para evitar condicionais complexas (`if/elif/else`) na criação de objetos. [1]