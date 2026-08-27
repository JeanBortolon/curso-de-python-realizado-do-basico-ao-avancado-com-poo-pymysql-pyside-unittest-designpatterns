# Explicações sobre o Padrão de Projeto Abstract Factory

Nesta pasta, você encontrará exemplos e recursos relacionados ao padrão de projeto **Abstract Factory**. Este padrão é um dos padrões criacionais do GoF (Gang of Four) e é usado para fornecer uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.

## Arquivos no Diretório

- **`abstract-factory.py`**: Este é o arquivo principal que contém a implementação do padrão Abstract Factory em Python. Abaixo, você encontrará uma explicação detalhada de cada componente deste arquivo.
- **`abstract-factory.graphml`** e **`abstract-factory.png`**: Estes arquivos representam um diagrama visual do padrão implementado. O arquivo `.graphml` pode ser aberto em editores de diagrama como o yEd, enquanto o `.png` é uma imagem que pode ser visualizada diretamente.

## Entendendo a Implementação em `abstract-factory.py`

O código em `abstract-factory.py` demonstra um cenário onde precisamos criar diferentes tipos de veículos (carros e motos) que pertencem a diferentes categorias (popular e luxo) e são específicos para diferentes regiões (Zona Norte e Zona Sul).

### Componentes do Padrão

1.  **Produtos Abstratos (`VeiculoLuxo`, `VeiculoPopular`)**
    -   São as interfaces (classes base abstratas) para os tipos de objetos que a fábrica pode criar.
    -   `VeiculoLuxo` e `VeiculoPopular` definem um método `buscar_cliente()`, que as classes concretas devem implementar.

2.  **Produtos Concretos (`CarroLuxoZN`, `CarroPopularZN`, `MotoLuxoZS`, etc.)**
    -   São as implementações específicas dos produtos abstratos.
    -   Temos duas "famílias" de produtos: Zona Norte (ZN) e Zona Sul (ZS).
    -   Por exemplo, `CarroLuxoZN` é um `VeiculoLuxo` específico para a Zona Norte, e `CarroPopularZS` é um `VeiculoPopular` para a Zona Sul.

3.  **Fábrica Abstrata (`VeiculoFactory`)**
    -   É a interface que define os métodos para criar os produtos abstratos.
    -   Possui métodos como `get_carro_luxo()`, `get_carro_popular()`, etc.
    -   O código cliente interage com esta interface, e não com as fábricas concretas diretamente.

4.  **Fábricas Concretas (`ZonaNorteVeiculoFactory`, `ZonaSulVeiculoFactory`)**
    -   São as implementações da `VeiculoFactory`.
    -   Cada fábrica concreta é responsável por criar uma família de produtos.
    -   `ZonaNorteVeiculoFactory` cria veículos da Zona Norte (`CarroLuxoZN`, `CarroPopularZN`, etc.).
    -   `ZonaSulVeiculoFactory` cria veículos da Zona Sul (`CarroLuxoZS`, `CarroPopularZS`, etc.).

5.  **Cliente (`Cliente`)**
    -   A classe `Cliente` usa uma fábrica (sem saber qual é a concreta) para obter os veículos de que precisa.
    -   O cliente não está acoplado às classes de produtos concretos. Ele apenas sabe que precisa de um "carro de luxo" ou uma "moto popular" e a fábrica se encarrega de fornecer a instância correta (seja da Zona Norte ou da Zona Sul).

### Como Funciona

O ponto principal é a separação de responsabilidades. O cliente precisa de um objeto, a fábrica abstrata define como obter esse objeto, e as fábricas concretas decidem qual objeto específico instanciar. Isso permite que você troque a família de produtos que está sendo usada (por exemplo, de Zona Norte para Zona Sul) com uma alteração mínima no código do cliente — muitas vezes, apenas alterando a instância da fábrica que ele usa.
