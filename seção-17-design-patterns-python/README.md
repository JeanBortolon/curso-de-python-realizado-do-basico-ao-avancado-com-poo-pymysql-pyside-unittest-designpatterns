# 🏛️ Seção 17: Padrões de Projeto (Design Patterns) em Python

Este diretório contém implementações práticas dos padrões de projeto mais comuns, utilizando Python. O objetivo é fornecer uma referência clara e exemplos funcionais para que você possa entender, aplicar e revisitar esses conceitos fundamentais de engenharia de software.

## 🎯 O que são Padrões de Projeto?

Padrões de Projeto (Design Patterns) são soluções testadas e comprovadas para problemas recorrentes no desenvolvimento de software. [1] Eles não são um código final, mas sim um modelo ou descrição de como resolver um problema que pode ser usado em muitas situações diferentes. [1] Utilizá-los ajuda a criar um código mais flexível, reutilizável e de fácil manutenção.

## 📂 Estrutura do Diretório

Os padrões estão organizados em três categorias principais, cada uma em sua própria pasta, conforme a classificação clássica do "Gang of Four" (GoF).

```
seção-17-design-patterns-python/
├── creational/         # Padrões de Criação
├── structural/         # Padrões Estruturais
│   └── composite/      # Exemplo: Padrão Composite
└── behavioral/         # Padrões Comportamentais
```

Dentro de cada categoria, você encontrará uma pasta para cada padrão específico, contendo:
-   Um arquivo `.py` com a implementação do padrão.
-   Um arquivo `README.md` explicando o padrão em detalhes.
-   Diagramas ou outros arquivos de apoio.

---

## 📚 Categorias de Padrões Abordadas

### 1. **Padrões de Criação (Creational)**

Esses padrões lidam com os mecanismos de criação de objetos, tentando criar objetos de uma maneira adequada a cada situação. [2] Eles aumentam a flexibilidade e a reutilização do código.

**Exemplos que você pode encontrar aqui:**
-   Singleton
-   Factory Method
-   Abstract Factory
-   Builder
-   Prototype

### 2. **Padrões Estruturais (Structural)**

Esses padrões explicam como montar objetos e classes em estruturas maiores, mantendo a flexibilidade e eficiência da estrutura. [3] Eles se concentram em como as classes e objetos podem ser compostos para formar estruturas maiores e mais complexas.

**Exemplos que você pode encontrar aqui:**
-   **Composite**: Como visto na subpasta `structural/composite`, este padrão permite tratar objetos individuais e composições de objetos de maneira uniforme. É ideal para representar hierarquias "parte-todo".
-   Adapter
-   Decorator
-   Facade
-   Proxy

### 3. **Padrões Comportamentais (Behavioral)**

Esses padrões se concentram nos algoritmos e na atribuição de responsabilidades entre os objetos. [4] Eles descrevem como os objetos interagem e distribuem responsabilidades.

**Exemplos que você pode encontrar aqui:**
-   Strategy
-   Observer
-   Command
-   Template Method
-   State
-   Iterator

---

## 💡 Como Estudar

1.  **Escolha uma categoria**: Comece pela que mais lhe interessa (Criação, Estrutural ou Comportamental).
2.  **Selecione um padrão**: Entre na pasta do padrão desejado.
3.  **Leia o `README.md` local**: Entenda o problema que o padrão resolve e sua estrutura.
4.  **Analise o código**: Veja a implementação em Python e como os conceitos foram aplicados.
5.  **Execute o exemplo**: Rode o arquivo `.py` para ver o padrão em ação.
