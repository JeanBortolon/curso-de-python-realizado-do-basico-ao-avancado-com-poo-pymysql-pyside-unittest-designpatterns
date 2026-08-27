# Aula 198 — Deque, FIFO e LIFO em Python

Este diretório contém exemplos práticos sobre como implementar e manipular as estruturas de dados **Pilha (Stack)** e **Fila (Queue)** utilizando listas padrão e a classe `deque` do módulo `collections` [Source Program, 21].

## 📌 Visão Geral
O foco desta aula é entender o comportamento dos protocolos de organização de dados e como a escolha da estrutura impacta a **performance** do algoritmo (Complexidade de Tempo) [Source Program].

## 📂 Conteúdo Abordado

### 1. LIFO (Last In First Out) — Pilha (Stack)
No protocolo **LIFO**, o último item a entrar é o primeiro a ser removido [Source Program]. 
*   **Estrutura utilizada:** Listas padrão do Python (`list`) [Source Program, 161].
*   **Operações principais:** 
    *   `append()`: Adiciona um item ao final da pilha [Source Program, 164].
    *   `pop()`: Remove o último item do final da pilha [Source Program, 165].
*   **Eficiência:** Realizar operações no **final** de uma lista tem complexidade **$O(1)$ (Tempo Constante)**, o que é extremamente eficiente [Source Program].

### 2. FIFO (First In First Out) — Fila (Queue)
No protocolo **FIFO**, o primeiro item a entrar é o primeiro a ser removido [Source Program, 21].
*   **Problema com Listas:** Usar `lista.insert(0, valor)` ou `lista.pop(0)` para gerenciar filas é ineficiente, pois requer o deslocamento de todos os outros elementos na memória, resultando em complexidade **$O(n)$ (Tempo Linear)** [Source Program, 4].
*   **Solução Recomendada:** A classe **`deque`** (Double-ended queue) [Source Program].

### 3. `collections.deque`
O `deque` é uma lista de extremidade dupla otimizada para adições e remoções rápidas em ambos os lados [Source Program].
*   **Vantagem:** Possui complexidade **$O(1)$** para tirar ou colocar itens tanto no início quanto no final [Source Program].
*   **Métodos exclusivos:**
    *   **`appendleft(valor)`**: Adiciona um item no início da fila [Source Program].
    *   **`popleft()`**: Remove e retorna o primeiro item da fila [Source Program].

## 🚀 Exemplo de Código (FIFO com `deque`)
```python
from collections import deque

fila = deque()
fila.append(4)          # Adiciona no final
fila.appendleft(0)      # Adiciona no começo -> deque()
fila.popleft()          # Remove o 0
```

## 📖 Recursos Complementares
*   [Artigo: Pilhas em Python com Listas](https://www.otaviomiranda.com.br/2020/pilhas-em-python-com-listas-stack/) [Source Program].
*   [Artigo: Filas em Python com Deque](https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/) [Source Program].

---

**Dica Técnica:** Quase tudo em Python é tratado como um **objeto**, incluindo as instâncias de `deque`, o que permite que elas herdem métodos de iteração e possam ser convertidas em listas comuns se necessário.