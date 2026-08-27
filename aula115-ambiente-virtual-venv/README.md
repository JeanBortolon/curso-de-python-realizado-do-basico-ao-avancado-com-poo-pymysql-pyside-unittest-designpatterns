# Aula 115 — Ambientes Virtuais (`venv`) e Gerenciamento de Pacotes (`pip`)

Este diretório contém orientações e comandos essenciais para a criação de **ambientes virtuais** e o uso do gerenciador de pacotes **`pip`** em Python.

## 📌 Visão Geral
Um ambiente virtual é uma pasta que carrega uma instalação isolada do Python [User Code]. Ele permite que diferentes projetos possuam suas próprias versões de bibliotecas, evitando conflitos entre dependências globais do sistema e necessidades específicas de uma aplicação.

## 🛠️ Recursos e Comandos Abordados

### 1. Criando o Ambiente Virtual
O módulo padrão utilizado para essa tarefa é o **`venv`** [User Code].
*   **Comando para criar:** `python -m venv .venv`.
*   **Nomes comuns:** `.venv`, `venv`, `env`, `.env` [User Code, 1670].

### 2. Ativação e Desativação
Para utilizar a instalação do ambiente virtual, é necessário "ativá-lo" no terminal [User Code].
*   **Linux e Mac:** `source venv/bin/activate` [User Code, 1742].
*   **Windows (PowerShell):** `.\.venv\Scripts\activate`.
*   **Desativar:** Basta digitar `deactivate` para retornar ao ambiente global do sistema [User Code, 1672].

### 3. Gerenciamento de Pacotes com `pip`
O **`pip`** é o instalador de pacotes padrão do Python, que busca bibliotecas no *Python Package Index* (PyPI).
*   **Instalar última versão:** `pip install nome_pacote` [User Code, 819].
*   **Instalar versão específica:** `pip install nome_pacote==0.0.0` [User Code, 1665].
*   **Desinstalar:** `pip uninstall nome_pacote` [User Code, 1667].
*   **Listar pacotes:** `pip list` mostra o que está instalado no ambiente atual.

### 4. O Arquivo `requirements.txt`
Este arquivo é fundamental para a **reprodutibilidade** do projeto, permitindo que outros desenvolvedores instalem exatamente as mesmas dependências.
*   **Gerar o arquivo:** `pip freeze > requirements.txt` (salva todas as versões instaladas) [User Code, 1679].
*   **Instalar a partir dele:** `pip install -r requirements.txt` [User Code, 1743].

## 🔐 Boas Práticas
*   **Isolamento:** Sempre ative o ambiente virtual antes de instalar novas bibliotecas para evitar poluir o Python global.
*   **Git:** Nunca envie a pasta do ambiente virtual (`.venv`) para repositórios como o GitHub. Utilize um arquivo `.gitignore` para excluí-la.

---

**Dica Técnica:** No VS Code, você pode abrir a **Paleta de Comandos** (`Ctrl+Shift+P`) e usar **"Python: Select Interpreter"** para garantir que o editor está usando o interpretador do ambiente virtual que você criou.