# Seção 14 - Teste Unitário, Unittest e TDD

Esta seção aborda conceitos fundamentais de Teste Unitário, a biblioteca `unittest` e o desenvolvimento orientado por testes (TDD). Abaixo está uma descrição dos conteúdos e recursos abordados nos programas desta pasta.

## Conteúdo

### 1. **Test Driven Development (TDD)**
- **Arquivo:** `src/conceito_tdd.py`
- **Descrição:**
  - Introdução ao conceito de TDD (Desenvolvimento Orientado por Testes).
  - Explicação do ciclo Red, Green, Refactor.
  - Implementação de uma função `bacon_com_ovos` que retorna diferentes valores com base em múltiplos de 3 e 5.

### 2. **Testes Unitários com Unittest**
- **Arquivo:** `tests/test-conceito-tdd.py`
- **Descrição:**
  - Criação de testes unitários para validar a função `bacon_com_ovos`.
  - Uso de `unittest.TestCase` para estruturar os testes.
  - Verificação de diferentes cenários de entrada e saída.

### 3. **Funções Matemáticas**
- **Arquivo:** `src/calculadora.py`
- **Descrição:**
  - Implementação de funções matemáticas básicas: `soma` e `subtrai`.
  - Uso de `assert` para validação de tipos de entrada.
  - Exemplos de uso com `doctest` para validar os resultados diretamente na documentação.

### 4. **Execução de Testes com Doctest**
- **Arquivo:** `src/calculadora.py`
- **Descrição:**
  - Uso do módulo `doctest` para executar testes embutidos na documentação das funções.
  - Demonstração de como validar o comportamento das funções diretamente nos comentários.

### 5. **Requisições HTTP**
- **Arquivo:** `src/pessoa.py`
- **Descrição:**
  - Implementação de uma classe `Pessoa` com atributos básicos.
  - Método `obter_todos_os_dados` para realizar requisições HTTP usando o módulo `requests`.
  - Tratamento de respostas HTTP para verificar conectividade.

### 6. **Execução de Programas**
- **Arquivo:** `main.py`
- **Descrição:**
  - Demonstração de como integrar funções e classes implementadas.
  - Uso de `try-except` para capturar erros em tempo de execução.
  - Execução de testes com `doctest` ao rodar o script diretamente.

## Recursos Abordados
- **Test Driven Development (TDD):**
  - Ciclo Red, Green, Refactor.
  - Escrita de testes antes da implementação.
- **Unittest:**
  - Estruturação de testes com `unittest.TestCase`.
  - Métodos de asserção como `assertEqual`, `assertTrue`, etc.
- **Doctest:**
  - Testes embutidos na documentação.
  - Execução automática de exemplos documentados.
- **Validação de Tipos:**
  - Uso de `assert` para garantir tipos corretos de entrada.
- **Requisições HTTP:**
  - Uso do módulo `requests` para realizar chamadas HTTP.
  - Tratamento de respostas com `resposta.ok`.

## Como Executar
1. Certifique-se de ter o Python instalado.
2. Navegue até a pasta `seção14-teste-unitario-unittest-tdd`.
3. Execute os arquivos diretamente ou rode os testes:
   ```bash
   python -m unittest discover tests
   ```
4. Para executar os testes com `doctest`, rode o arquivo correspondente:
   ```bash
   python src/calculadora.py
   ```

## Observações
- Certifique-se de instalar as dependências necessárias, como o módulo `requests`.
- Consulte os comentários nos arquivos para mais detalhes sobre a implementação.

---