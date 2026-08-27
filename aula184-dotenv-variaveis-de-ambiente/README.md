
# Aula 184 — Variáveis de Ambiente com Python e `python-dotenv`

Este diretório contém exemplos práticos de como gerenciar **variáveis de ambiente** em Python, uma prática essencial para configurar aplicações e proteger dados sensíveis.

## 📌 Visão Geral
Variáveis de ambiente são valores dinâmicos que podem afetar o comportamento de processos em um computador. Na programação, elas são amplamente utilizadas para armazenar **segredos** (como senhas de banco de dados e chaves de API) e configurações que mudam entre ambientes de desenvolvimento e produção.

## 🛠️ Recursos e Comandos Abordados

### 1. Configuração no Sistema Operacional
Antes de rodar o script, você pode definir variáveis diretamente no terminal:
*   **Windows (PowerShell):** `$env:VARIAVEL="VALOR"`
*   **Linux e Mac:** `export NOME_VARIAVEL="VALOR"`

### 2. O Módulo `os` (Nativo)
O Python fornece o módulo **`os`** para interagir com o sistema operacional:
*   **`os.environ`**: Um dicionário contendo todas as variáveis de ambiente do sistema.
*   **`os.getenv('CHAVE')`**: Método seguro para recuperar o valor de uma variável. Se a chave não existir, ele retorna `None` em vez de gerar um erro.
*   **`os.environ['CHAVE'] = 'valor'`**: Permite configurar ou sobrescrever uma variável em tempo de execução.

### 3. A Biblioteca `python-dotenv`
Para facilitar o desenvolvimento local, utilizamos o pacote **`python-dotenv`**. Ele permite que você crie um arquivo chamado **`.env`** na raiz do projeto e carregue essas variáveis automaticamente.

**Instalação:**
```bash
pip install python-dotenv
```

**Uso no Código:**
```python
from dotenv import load_dotenv
load_dotenv() # Carrega as variáveis do arquivo .env para o ambiente
```

## 🔐 Boas Práticas e Segurança
*   **Nunca envie seu arquivo `.env` para repositórios públicos (GitHub)**. Ele contém seus segredos e deve ser listado no arquivo `.gitignore`.
*   **Sempre crie um arquivo `.env-example`**: Este arquivo deve conter apenas as chaves (sem os valores reais), servindo como um guia para que outros desenvolvedores saibam quais variáveis precisam configurar para rodar o projeto.

## 🚀 Exemplo de Execução
O programa demonstrado na aula busca uma senha de banco de dados:
```python
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv('BD_PASSWORD')) # Retorna o valor definido no seu .env
```

---

**Dica técnica:** O uso de variáveis de ambiente torna seu código mais **modular e flexível**, permitindo que a mesma aplicação se comporte de maneira diferente apenas alterando as configurações externas, sem tocar no código-fonte.