# Documentação da pasta aula194-subprocess-executando-programas-e-comandos-externos

Esta pasta apresenta exemplos práticos de como executar comandos e programas externos em Python utilizando o módulo `subprocess`.

## Conteúdo dos Programas

### 1. Execução de comandos externos com subprocess
- Uso do método `subprocess.run()` para rodar comandos do sistema operacional diretamente pelo Python.
- Exemplos de comandos para diferentes sistemas:
  - Windows: `ping 127.0.0.1`
  - Linux/Mac: `ls -lah /` ou `ping 127.0.0.1 -c 4`
- Como capturar a saída padrão (`stdout`) e a saída de erro (`stderr`).
- Como tratar a entrada e saída como texto, especificando a codificação correta para cada sistema (ex: `utf_8` para Unix, `cp850` para Windows).
- Uso do argumento `shell=True` para executar comandos no shell do sistema.
- Como acessar o código de retorno do processo e os argumentos utilizados.

### 2. Boas práticas e dicas
- Comentários explicativos sobre cada argumento e retorno do `subprocess.run()`.
- Observações sobre diferenças de codificação entre sistemas operacionais.
- Recomendações para adaptar comandos conforme o sistema detectado.

## Requisitos
- Python 3.x
- Não requer bibliotecas externas além da padrão.

## Observações
- O código é útil para automatizar tarefas do sistema operacional, executar scripts, comandos de rede, manipular arquivos, etc.
- Sempre tenha cuidado ao usar `shell=True` para evitar riscos de segurança, especialmente com comandos dinâmicos.
- Consulte a documentação oficial para mais detalhes: https://docs.python.org/3/library/subprocess.html

---

Esta documentação serve como referência rápida para os recursos e exemplos de execução de comandos externos presentes nesta pasta.
