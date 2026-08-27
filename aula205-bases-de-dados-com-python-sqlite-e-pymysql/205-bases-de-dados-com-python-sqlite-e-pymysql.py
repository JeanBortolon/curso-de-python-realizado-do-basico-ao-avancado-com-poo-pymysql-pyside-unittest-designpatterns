import sqlite3
from pathlib import Path

# OBTENDO O DIRETÓRIO DA PASTA ONDE O NOSSO PROJETO ESTÁ
ROOT_DIR = Path(__file__).parent
# CRIANDO O NOME DO ARQUIVO DATABASE DO SQLITE
DB_NAME = 'db.sqlite3'
# INFORMANDO A ESTRUTURA FINAL DO ARQUIVO
DB_FILE = ROOT_DIR / DB_NAME
# NOME DA TABELA QUE SERÁ CRIADA NO DB
TABLE_NAME = 'customers'
# CONECTA NO ARQUIVO DO BANCO DE DADOS
connection = sqlite3.connect(DB_FILE)
# CHAMA O CURSOR PARA A CONEXÃO ESTABELECIDA COM O BANCO PARA PERCORES OS RESULTADOS
cursor = connection.cursor()

# CUIDADO: FAZENDO DELETE SEM WHERE PARA LIMPAR A TABELA
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
# MÉTODO COMMIT NECESSÁRIO PARA EXECUTAR O COMANDO SQL APÓS A ESTRUTURAÇÃO REALIZADA
connection.commit()

# DELETE USANDO SQLITE SEQUENCE PARA RECOMEÇAR A SEQUENCIA DE ID'S
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# EXECUTA O COMANDO SQL PARA CRIAR TABELA SE NAO EXISTIR COM ID PRIMARY KEY, NOME E PESO
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TXT,'
    'weight REAL'
    ')'
)
# MÉTODO COMMIT NECESSÁRIO PARA EXECUTAR O COMANDO SQL APÓS A ESTRUTURAÇÃO REALIZADA
connection.commit()
'''
# REGISTRAR VALORES NA COLUNA DA TABELA
# cursor.executemany('') executa múltiplos comandos
# cursor.execute executa 1 comando
# Cuidado: SQL Injection
cursor.execute(
    f'INSERT INTO {TABLE_NAME} '
    '(id, name, weight)' 
    'VALUES' 
    '(NULL, "Helena", 50.4),(NULL, "Paola", 63.58),(NULL, "Jean", 84.5)'
) 
connection.commit()
'''

# Estratégia para evitar SQL Injection, corrigindo a estrutura do comando SQL
# utilização de placeholders ou bindings
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES (?, ?)'
)
# Permite que o usuário escreva os valores na lista e não no SQL
# cursor.execute(sql, ["Joana", 4])

# Executando vários comandos passando lista de listas ou tupla de tuplas
cursor.executemany(
    sql,
    (
        ('Joana', 4), ('Luiz', 5)
    )
)



# Executando vários comandos passando dicionários e lista de dicionários
'''
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(?, ?)'
    '(:nome, :peso)'
)
cursor.execute(sql, {'nome': 'Sem nome', 'peso': 3})
cursor.executemany(sql, (
    {'nome': 'Joãozinho', 'peso': 3},
    {'nome': 'Maria', 'peso': 2},
    {'nome': 'Helena', 'peso': 4},
    {'nome': 'Joana', 'peso': 5},
))
'''
connection.commit()

# FECHA TUDO QUE ESTAVA ABERTO APÓS EXECUTAR COMANDOS
cursor.close()
connection.close()