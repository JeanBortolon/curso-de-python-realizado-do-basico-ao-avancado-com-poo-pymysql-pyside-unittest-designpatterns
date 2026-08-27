# Bases de Dados com Python, SQLite e PyMySQL

Esta pasta contém exemplos práticos de manipulação de bancos de dados utilizando Python, SQLite e conceitos de SQL. Os principais recursos abordados nos programas são:

## Conteúdo dos Arquivos

### 205-bases-de-dados-com-python-sqlite-e-pymysql.py
- Demonstra como criar e conectar a um banco de dados SQLite.
- Criação de tabelas com SQL.
- Limpeza de tabelas e reset de sequência de IDs.
- Uso de comandos SQL básicos: `CREATE TABLE`, `DELETE`, `INSERT`.

### 205-criando-meu-primeiro-arquivo-db.sqlite3.py
- Exemplo de criação e manipulação de um arquivo de banco de dados SQLite.
- (Arquivo está vazio ou serve como placeholder para estudo prático.)

### main.py
- Demonstra o ciclo completo CRUD (Create, Read, Update, Delete) em SQLite.
- Criação e limpeza de tabelas.
- Inserção de dados com segurança (evitando SQL Injection).
- Uso de parâmetros nomeados e múltiplas inserções.
- Seleção, atualização e remoção de registros.

### select.py
- Demonstra como realizar consultas (SELECT) em tabelas SQLite.
- Impressão de todos os registros e consulta filtrada por ID.

### db.sqlite3
- Arquivo de banco de dados SQLite gerado pelos scripts.

## Recursos Abordados
- Conexão e manipulação de bancos de dados SQLite com Python (`sqlite3`).
- Criação, leitura, atualização e exclusão de dados (CRUD).
- Uso de comandos SQL diretamente do Python.
- Prevenção de SQL Injection com parâmetros.
- Reset de sequência de IDs em tabelas.
- Consulta e iteração sobre resultados.

## Como Executar
1. Certifique-se de ter Python instalado.
2. Execute os scripts desejados para testar os exemplos:
   ```bash
   python main.py
   python select.py
   ```
3. O arquivo `db.sqlite3` será criado/atualizado automaticamente.

Consulte os comentários nos scripts para entender cada etapa do processo.
