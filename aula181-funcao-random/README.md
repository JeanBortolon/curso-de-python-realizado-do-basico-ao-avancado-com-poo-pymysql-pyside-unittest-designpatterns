
# Aula 181 — Módulo `random` em Python

Este repositório contém exemplos práticos de como utilizar o módulo **`random`** do Python para gerar números e realizar seleções **pseudoaleatórias**.

## 📌 Visão Geral
O módulo `random` é uma ferramenta da biblioteca padrão do Python usada para automação de tarefas e análise de dados. É importante notar que ele gera números **pseudoaleatórios**, o que significa que, embora pareçam aleatórios, são gerados por algorítmos previsíveis a partir de uma entrada específica (seed). Portanto, **não deve ser utilizado para fins de segurança ou criptografia**.

## 🛠️ Recursos e Funções Abordados

### 1. Inicialização e Controle
*   **`random.seed(x)`**: Inicializa o gerador de números aleatórios. Definir uma semente (seed) torna os resultados **reprodutíveis**, o que é útil para testes.

### 2. Geração de Números
*   **`random.randrange(início, fim, passo)`**: Gera um número inteiro aleatório dentro de um intervalo, permitindo definir um **passo** (ex: apenas números pares).
*   **`random.randint(início, fim)`**: Produz um **número inteiro** aleatório entre o intervalo especificado (inclusive). É comumente usado para simular o lançamento de dados.
*   **`random.uniform(início, fim)`**: Gera um **número flutuante** (com casas decimais) aleatório dentro de um intervalo.
*   **`random.random()`**: Retorna um número flutuante aleatório entre **0.0 e 1.0**.

### 3. Manipulação de Sequências e Coleções
*   **`random.choice(Iterável)`**: Seleciona e retorna **um único elemento** aleatório de uma sequência (como uma lista ou tupla).
*   **`random.shuffle(SequênciaMutável)`**: **Embaralha** os elementos de uma lista original diretamente (modifica a lista *in-place*). É ideal para jogos de cartas.
*   **`random.sample(Iterável, k=N)`**: Escolhe $N$ elementos de um iterável e retorna uma nova lista com esses valores **sem repetição**.
*   **`random.choices(Iterável, k=N)`**: Semelhante ao sample, mas permite que os elementos sejam escolhidos **com repetição** (um mesmo valor pode aparecer mais de uma vez no resultado).

## 🚀 Exemplo de Uso Rápido
```python
import random

# Gerar um dado de 6 lados
dado = random.randint(1, 6) 

# Escolher um nome aleatório
nomes = ['Luiz', 'Maria', 'Helena']
escolhido = random.choice(nomes)
```

## 📖 Documentação Oficial
Para mais detalhes, consulte a [documentação oficial do Python](https://docs.python.org/pt-br/3/library/random.html).

---

**Dica Didática:** Lembre-se que funções como `shuffle` possuem **efeitos colaterais**, pois alteram o objeto original na memória. Já funções como `sample` e `choices` retornam novos objetos sem alterar a fonte.