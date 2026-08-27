# Padrão de Projeto Comportamental - Template Method

Este diretório contém exemplos que demonstram o uso do padrão de projeto **Template Method**.

## O que é o Template Method?

O **Template Method** é um padrão de projeto comportamental que define o esqueleto de um algoritmo em uma classe base, mas permite que as subclasses forneçam a implementação de alguns dos passos desse algoritmo. Em outras palavras, ele estabelece uma sequência de passos fixa, mas deixa a cargo das classes filhas como cada um desses passos será realizado.

Este padrão promove a reutilização de código e segue o **"Princípio de Hollywood"**: *"Não nos chame, nós chamaremos você."*. Isso significa que a classe base (o "framework") chama os métodos das subclasses, e não o contrário. Esse conceito também é conhecido como **Inversão de Controle (IoC)**.

### Componentes Principais

1.  **AbstractClass (Classe Abstrata):**
    *   Define o `template_method()`, que é o método principal que contém o esqueleto do algoritmo.
    *   Pode implementar alguns dos passos do algoritmo como **métodos concretos** (que são comuns a todas as subclasses).
    *   Declara os passos que devem ser implementados pelas subclasses como **métodos abstratos**.
    *   Pode incluir **"hooks"**, que são métodos com uma implementação padrão (geralmente vazia) que as subclasses podem ou não sobrescrever para adicionar comportamento opcional em pontos específicos do algoritmo.

2.  **ConcreteClass (Classe Concreta):**
    *   Herda da `AbstractClass`.
    *   Implementa (sobrescreve) os **métodos abstratos** obrigatórios para fornecer os detalhes específicos do algoritmo.
    *   Pode opcionalmente sobrescrever os **hooks** para customizar o comportamento.

## Arquivos no Diretório

### 1. `template-method-1.py`

Este arquivo ilustra o padrão Template Method com um exemplo prático e fácil de entender: a preparação de uma pizza.

*   **`Pizza` (AbstractClass):**
    *   É a classe abstrata que define o método `prepare()`, que atua como o *Template Method*.
    *   O método `prepare()` define a sequência de passos para fazer uma pizza: adicionar ingredientes, cozinhar, cortar e servir.
    *   `add_ingrentients()` e `cook()` são **métodos abstratos**, pois o tipo de ingrediente e o tempo de cozimento variam para cada pizza.
    *   `cut()` e `serve()` são **métodos concretos**, pois cortar e servir são ações iguais para todas as pizzas.
    *   `hook_before_add_ingredients()` e `hook_after_add_ingredients()` são **hooks** que permitem às subclasses adicionar ações personalizadas antes ou depois de adicionar os ingredientes.

*   **`AModa` e `Veg` (ConcreteClasses):**
    *   São classes concretas que herdam de `Pizza`.
    *   `AModa` implementa os métodos para fazer uma pizza "À Moda".
    *   `Veg` implementa os métodos para uma pizza vegana e também utiliza o `hook_before_add_ingredients()` para adicionar um passo extra ("Lavar ingredientes").

Ao executar o arquivo, você verá que o método `prepare()` é chamado para ambos os tipos de pizza, mas o resultado é diferente porque cada subclasse implementou os passos de forma única, seguindo o mesmo "molde" (template).

### 2. `template-method-2.py`

Este arquivo apresenta uma visão mais genérica e teórica do padrão, utilizando uma nomenclatura clássica de design patterns.

*   **`Abstract` (AbstractClass):**
    *   Contém o `template_method()`, que orquestra a execução de `operation1()`, `operation2()`, e outros métodos.
    *   `base_class_method()` é um método concreto.
    *   `operation1()` e `operation2()` são os **métodos abstratos** a serem implementados.
    *   `hook()` é um método opcional que as subclasses podem sobrescrever.

*   **`ConcreteClass1` e `ConcreteClass2` (ConcreteClasses):**
    *   Implementam as operações abstratas (`operation1` e `operation2`) de maneiras distintas.
    *   `ConcreteClass1` decide utilizar o `hook()` para adicionar um comportamento extra, enquanto `ConcreteClass2` não o utiliza.

Este exemplo é útil para entender a estrutura fundamental do padrão, sem se prender a um contexto de negócio específico.

## Conclusão

O Template Method é ideal quando você tem um algoritmo com uma estrutura bem definida, mas com detalhes de implementação que variam. Ele permite criar um framework flexível e extensível, evitando a duplicação de código e garantindo que a estrutura principal do algoritmo não seja alterada pelas subclasses.
