# Documentação da pasta aula196-threads-executando-processos-em-paralelo

Esta pasta apresenta exemplos práticos de execução paralela e concorrente em Python utilizando threads, além de técnicas para evitar problemas de concorrência com o uso de locks.

## Conteúdo dos Programas

### 1. Threads em Python
- Criação de threads personalizadas herdando de `Thread`.
- Execução de funções em paralelo usando `Thread` e o argumento `target`.
- Uso do método `join` para aguardar o término de uma thread.
- Simulação de tarefas demoradas e execução concorrente de múltiplas tarefas.

### 2. Controle de Concorrência com Lock
- Utilização de `Lock` para evitar condições de corrida (race conditions) ao acessar e modificar recursos compartilhados.
- Exemplo prático: classe `Ingressos` que controla a venda de ingressos de forma segura entre múltiplas threads.
- Demonstração de como trancar e liberar recursos críticos durante operações concorrentes.

### 3. Boas práticas e dicas
- Comentários explicativos sobre cada parte do código e exemplos de uso.
- Demonstração de problemas que podem ocorrer sem o uso de locks e como resolvê-los.
- Uso de `sleep` para simular tempo de processamento e facilitar a visualização do paralelismo.

## Requisitos
- Python 3.x
- Não requer bibliotecas externas além da padrão.

## Observações
- O código é útil para entender conceitos de paralelismo, concorrência e sincronização de threads em Python.
- Sempre utilize locks ou outras formas de sincronização ao manipular recursos compartilhados entre threads.
- Consulte a documentação oficial para mais detalhes: https://docs.python.org/3/library/threading.html

---

Esta documentação serve como referência rápida para os recursos e exemplos de threads e concorrência presentes nesta pasta.
