# Documentação da pasta aula141-log-file-mixin-herança-multipla-e-abstração

Esta pasta apresenta exemplos práticos de conceitos fundamentais de Programação Orientada a Objetos em Python, como abstração, herança, mixins e logging.

## Conteúdo dos Programas

### 1. Abstração
- Uso de uma classe base abstrata (`Log`) que define a interface para logging.
- O método `_log` é abstrato e deve ser implementado nas subclasses.

### 2. Herança e Mixins
- Criação de mixins (`LogFileMixin` e `LogPrintMixin`) que herdam de `Log` e implementam o método `_log` de formas diferentes:
  - `LogFileMixin`: salva logs em arquivo e imprime no terminal.
  - `LogPrintMixin`: apenas imprime logs no terminal.
- Demonstração de como mixins facilitam a reutilização de código e a customização de comportamentos.

### 3. Logging
- Métodos para logar mensagens de erro (`log_error`) e sucesso (`log_success`), formatando as mensagens automaticamente.
- Exemplo de uso dos mixins no bloco principal (`if __name__ == '__main__'`).

## Requisitos
- Python 3.x
- Não requer bibliotecas externas além da padrão.

## Observações
- O arquivo `log.txt` será criado automaticamente para armazenar logs quando o `LogFileMixin` for utilizado.
- O código é um ótimo exemplo de como aplicar abstração, herança e mixins para resolver problemas comuns de logging em projetos Python.

---

Esta documentação serve como referência rápida para os conceitos e exemplos de abstração, herança e mixins presentes nesta pasta.
