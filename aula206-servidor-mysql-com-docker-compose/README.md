# Servidor MySQL com Docker Compose

Esta pasta contém exemplos e scripts para trabalhar com um servidor MySQL executado via Docker Compose e acesso ao banco a partir de scripts Python usando PyMySQL.

## Estrutura da pasta

- `.env` / `.env-example` - Arquivos de variáveis de ambiente para configuração do container MySQL (usuário, senha, database, host).
- `docker-compose.yml` - Configuração do serviço MySQL para uso em ambiente local via Docker Compose.
- `aula206-pymysql-cliente-mysql-com-python.py` - Exemplo básico de conexão ao MySQL usando PyMySQL e inserção de registros.
- `aula206-evitando-sql-injection-nao-enviar-dados-na-consulta.py` - Demonstra técnicas para evitar SQL Injection usando placeholders e parâmetros.
- `aula206-rowcount-rownumber-lastrowid.py` - Mostra como usar propriedades como `rowcount`, `rownumber` e `lastrowid` com cursores do PyMySQL.
- `aula206-sscursor-ssdictcursor-para-conjuntos-de-dados-grandes.py` - Exemplo de uso de cursores não-buffered (SSCursor/SSDictCursor) para trabalhar com grandes volumes de dados.
- `aula206-delete-e-update-com-set.py` - Demonstra operações de DELETE e UPDATE usando placeholders.
- `aula206-cursor-class-dict-cursor-retorna-dicts.py` - Mostra o uso de `cursorclass=pymysql.cursors.DictCursor` para retornar resultados como dicionários.

## Recursos e conceitos abordados

- Criação e configuração de um servidor MySQL usando Docker Compose.
- Uso de variáveis de ambiente para configurar conexões seguras (`.env`).
- Conexão ao MySQL a partir de Python usando a biblioteca PyMySQL.
- Execução de comandos SQL: `CREATE TABLE`, `TRUNCATE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`.
- Uso de placeholders (`%s`, `%(name)s`) para prevenir SQL Injection.
- Inserção única e em massa (`execute`, `executemany`).
- Cursores customizados (`DictCursor`, `SSCursor`, `SSDictCursor`) e suas vantagens.
- Propriedades úteis do cursor: `rowcount`, `lastrowid`, `rownumber`.
- Uso de `mogrify` para visualizar a consulta final com parâmetros.

## Como usar

1. Certifique-se de ter Docker e Docker Compose instalados.
2. Configure o `.env` com as variáveis necessárias (MYSQL_ROOT_PASSWORD, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD, etc.) ou copie o `.env-example` para `.env` e ajuste.
3. Inicie o serviço MySQL:
   ```powershell
   docker-compose up -d
   ```
4. Instale dependências Python, por exemplo:
   ```powershell
   pip install pymysql python-dotenv
   ```
5. Execute os scripts conforme desejar:
   ```powershell
   python aula206-pymysql-cliente-mysql-com-python.py
   python aula206-evitando-sql-injection-nao-enviar-dados-na-consulta.py
   ```

## Observações
- Os scripts incluem comandos que truncam tabelas e inserem dados de exemplo. Use com cautela em ambientes com dados reais.
- A porta exposta no `docker-compose.yml` é `3307:3306` para permitir execução paralela caso já exista um MySQL local.

Consulte os comentários internos de cada script para mais detalhes sobre cada etapa.
