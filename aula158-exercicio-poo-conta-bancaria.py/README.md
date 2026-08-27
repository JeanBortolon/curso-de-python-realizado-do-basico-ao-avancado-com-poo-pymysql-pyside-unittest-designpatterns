# Projeto: Sistema Bancário em Python (POO)

Esta pasta contém um projeto completo de um sistema bancário simples, desenvolvido para praticar e fixar conceitos de Programação Orientada a Objetos (POO) em Python. Abaixo está um resumo didático de cada arquivo e dos principais recursos utilizados.

## Estrutura e Arquivos do Projeto

### 1. `banco.py`
- **Função:** Gerencia o banco, autentica clientes, contas e agências.
- **Recursos:**
  - Classe `Banco` com métodos para checar agência, cliente, conta e se a conta pertence ao cliente.
  - Método `autenticar` para validar todas as informações antes de permitir operações.
  - Exemplo de uso no bloco `if __name__ == '__main__'`.

### 2. `contas.py`
- **Função:** Define as classes de contas bancárias.
- **Recursos:**
  - Classe base `Conta` com métodos de depósito, saque e saldo.
  - Classes filhas: `ContaCorrente` (com limite de crédito) e `ContaPoupanca` (sem limite, apenas saldo).
  - Métodos para movimentação de valores e representação das contas.

### 3. `pessoas.py`
- **Função:** Define as pessoas do sistema.
- **Recursos:**
  - Classe base `Pessoa` (nome, idade).
  - Classe `Cliente` (herda de Pessoa) e pode ter uma conta associada.

## Conceitos Abordados
- **POO:** Herança, composição, encapsulamento e polimorfismo.
- **Associação de objetos:** Cliente possui uma conta, banco gerencia listas de clientes, contas e agências.
- **Métodos especiais:** `__init__`, `__repr__` para melhor visualização dos objetos.
- **Validação e autenticação:** Antes de qualquer operação, o sistema checa se tudo está correto.
- **Exemplo prático:** O bloco principal mostra como criar clientes, contas, adicionar ao banco e realizar operações.

## Como usar
1. Crie clientes e contas.
2. Adicione-os ao banco.
3. Use o método `autenticar` para validar antes de operar.
4. Realize depósitos, saques e consulte o saldo.

## Dicas rápidas
- Sempre associe uma conta ao cliente antes de adicionar ao banco.
- O banco só permite operações se todas as validações passarem.
- O projeto é modular: cada arquivo tem uma responsabilidade clara.

---

Este projeto é ideal para revisar POO, autenticação e organização de código em Python. Consulte este README sempre que quiser relembrar como estruturar sistemas orientados a objetos!
