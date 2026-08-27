# 🐍 Curso de Python — Do Básico ao Avançado (POO, Selenium, PyMySQL, PySide6, Unittest, Design Patterns)

Este documento organiza e resume **todo o conteúdo do curso**, pasta por pasta, para servir como guia de consulta rápida e revisão futura. Os materiais estão organizados por "aulas" (numeradas) e "seções" temáticas, cobrindo desde a sintaxe básica do Python até tópicos avançados como automação web, bancos de dados, interfaces gráficas e padrões de projeto.

> 💡 **Dica de uso:** use o índice abaixo para navegar direto ao assunto que você precisa relembrar. Cada pasta do projeto também possui seu próprio `README.md` com detalhes ainda mais aprofundados.

---

## 📑 Índice

1. [Fundamentos da Linguagem](#1-fundamentos-da-linguagem)
2. [Funções e Conceitos Funcionais](#2-funções-e-conceitos-funcionais)
3. [Estruturas de Dados Avançadas](#3-estruturas-de-dados-avançadas)
4. [Tratamento de Erros e Módulos](#4-tratamento-de-erros-e-módulos)
5. [Ambiente Virtual](#5-ambiente-virtual)
6. [Programação Orientada a Objetos (POO)](#6-programação-orientada-a-objetos-poo)
7. [Manipulação de Arquivos e Dados](#7-manipulação-de-arquivos-e-dados)
8. [Segurança, Aleatoriedade e Templates](#8-segurança-aleatoriedade-e-templates)
9. [Automação, Sistema e Linha de Comando](#9-automação-sistema-e-linha-de-comando)
10. [Web: HTTP, Scraping e Selenium](#10-web-http-scraping-e-selenium)
11. [Processos, Paralelismo e Jupyter](#11-processos-paralelismo-e-jupyter)
12. [Manipulação de PDFs, Planilhas e Imagens](#12-manipulação-de-pdfs-planilhas-e-imagens)
13. [Interfaces Gráficas com PySide6](#13-interfaces-gráficas-com-pyside6)
14. [Bancos de Dados (SQLite, MySQL/PyMySQL, Docker)](#14-bancos-de-dados-sqlite-mysqlpymysql-docker)
15. [Testes Unitários, TDD e Doctest](#15-testes-unitários-tdd-e-doctest)
16. [Design Patterns (Padrões de Projeto)](#16-design-patterns-padrões-de-projeto)

---

## 1. Fundamentos da Linguagem

### 📁 `aula01-python-inicial-print-input-tipos-fstrings-for-while-listas-etc/`
Ponto de partida do curso, com **mais de 60 arquivos** cobrindo a base da linguagem:
- `print`, comentários, `input`, tipos (`str`, `int`, `float`, `bool`) e coerção de tipos.
- Operadores matemáticos, de comparação, lógicos (`and`, `or`, `not`) e `in`/`not in`.
- F-strings, `str.format`, interpolação `%`, fatiamento e métodos de string (`split`, `join`, `strip`).
- Estruturas condicionais (`if/elif/else`) e de repetição (`while`, `for`, `break`, `continue`, `range`).
- Listas, tuplas, empacotamento/desempacotamento, `enumerate`, listas de listas.
- `try/except` introdutório e uso do debugger do VS Code.
- **Exercícios**: cálculo de IMC, calculadora, gerador de CPF (subpasta `exercicio-gerador-de-cpf/`) e uma pasta extra `exercicios-de-treino/` com problemas de fixação (palavra secreta, par/ímpar, contagem de letras, etc.).

## 2. Funções e Conceitos Funcionais

### 📁 `aula65-funcoes-conceitos-e-utilidades/`
- Definição de funções, argumentos nomeados/não nomeados, valores padrão de parâmetros.
- Escopo de funções em módulos, `global`, `return`.
- `*args`/`**kwargs`, funções de alta ordem (*high-order functions*) e *closures*.
- Exercícios práticos de fixação (aulas 72 e 75).

### 📁 `aula76-dicionarios-tipo-set-e-funcao-lambda/`
- Dicionários: criação, manipulação de chaves e métodos (`get`, `items`, `keys`, `values`).
- Tipo `set` e operações de conjunto; exercício de encontrar número duplicado.
- Funções `lambda` simples e compostas; empacotamento/desempacotamento de dicionários.

### 📁 `aula84-list-e-dictionary-comprehesion/`
- *List comprehension* (simples e com múltiplos `for`).
- *Dictionary* e *set comprehension*.

### 📁 `aula87-isinstance-truthy-e-falsy-generator-e-yield/`
- `isinstance`, valores *truthy*/*falsy*, tipos mutáveis vs. imutáveis.
- `dir`, `hasattr`, `getattr`.
- *Generator expressions*, funções geradoras e a palavra-chave `yield`.

### 📁 `aula100-execercio-3-em-1-ordenação-copy-sorted-sort/`
- Ordenação com `sorted()` (retorna nova lista) x `.sort()` (in-place).
- Cópias rasas e profundas de listas (`copy`).
- Ordenação personalizada com `lambda` e `itemgetter`.

### 📁 `aula101-variaveis-non-locals-adiamento-de-funcoes-decoradoras-e-conceitos/`
- Adiamento de execução de funções, *closures* e variáveis livres (`nonlocal`).
- Funções decoradoras: conceito, *syntax sugar* (`@decorator`), decoradores com parâmetros e ordem de execução de múltiplos decoradores.
- Exemplo real de parsing de payload MQTT (medidor Khomp).

### 📁 `aula107-funcoes-uteis-zip-count-groupby-filter-functools-map-etc/`
- `zip` (unir listas), `itertools.count` (iterador infinito), permutação/combinação.
- `itertools.groupby` (agrupamento), `map`, `functools.partial`, `filter`.
- `functools.reduce` e recursividade.

## 3. Estruturas de Dados Avançadas

### 📁 `aula198-deque-fifo-e-lifo/`
- Uso do `collections.deque` como fila (FIFO) e pilha (LIFO).

## 4. Tratamento de Erros e Módulos

### 📁 `aula93-try-except-e-raise/`
- `try/except` aprofundado, `try/finally` e `raise` para levantar exceções personalizadas.

### 📁 `aula96-trabalhando-com-modulos/`
- Criação e importação de módulos (`import`), modularização de código.
- Função `reload` para recarregar módulos já importados.

### 📁 `aula99-package-e-modulos/`
- Organização de código em **pacotes** Python (`__init__.py`), incluindo um sub-pacote (`dados_package/`) com múltiplos módulos.

## 5. Ambiente Virtual

### 📁 `aula115-ambiente-virtual-venv/`
- Criação e uso de ambientes virtuais (`venv`) para isolar dependências de projetos.

## 6. Programação Orientada a Objetos (POO)

### 📁 `aula120-progamacao-orientada-a-objetos/`
Pasta extensa (~40 arquivos) — o coração da POO em Python:
- Classes, objetos, `self`, escopo e estados de uma classe, atributos de classe.
- Serialização de objetos em JSON (salvar/recuperar).
- `@staticmethod`, `@classmethod` e *factories*.
- `@property` (getters e setters), encapsulamento e níveis de acesso.
- Associação, agregação e composição entre objetos.
- Herança, `super()`, herança múltipla, classes e métodos abstratos (`ABC`), polimorfismo.
- Parâmetros *positional-only*, tratamento de erros em classes.
- *Dunder/magic methods* (`__init__`, `__new__`, `__repr__`, `__call__`, etc.).
- *Context managers* em classes e módulo `contextlib`.
- Decoradores aplicados a classes e métodos.
- `dataclasses`, módulo `typing`, `NamedTuple` e criação de listas iteráveis personalizadas.

### 📁 `aula141-log-file-mixin-herança-multipla-e-abstração/`
- Classe abstrata `Log` com o método abstrato `_log`.
- **Mixins** (`LogFileMixin` salva em arquivo, `LogPrintMixin` só imprime) demonstrando reutilização de código via herança múltipla.

### 📁 `aula156-docstrings-em-classes/`
- Boas práticas de documentação com *docstrings* em funções, classes e módulos (inclusive multilinha) e uso de `help()`.

### 📁 `aula158-exercicio-poo-conta-bancaria.py/`
Projeto completo de **sistema bancário** para fixar POO:
- `pessoas.py`: classes `Pessoa` e `Cliente`.
- `contas.py`: classe base `Conta` e subclasses `ContaCorrente` (com limite) e `ContaPoupanca`.
- `banco.py`: classe `Banco` que autentica clientes/contas/agências antes de qualquer operação.
- Demonstra herança, composição, encapsulamento, polimorfismo e `__repr__`.

## 7. Manipulação de Arquivos e Dados

### 📁 `aula166-datetime-calendar-os-e-diretorios/`
- Módulo `datetime`: criação de datas, `strptime`, cálculos e formatação de datas.
- Módulo `calendar`: geração de calendários, `monthrange`, dias da semana, tradução com `locale`.
- Módulo `os`: caminhos (`splitext`), `isdir`/`listdir`, `os.walk`, tamanho de arquivos (`getsize`/`stat`).
- `shutil`: copiar e mover arquivos/diretórios.

### 📁 `aula175-trabalhando-com-arquivos-json-e-context-manager/`
- *Context managers* (`with open`) para leitura/escrita de arquivos (`write`, `read`, `readlines`).
- Persistência de dados em **JSON** (`json.dump`/`json.load`, `json.dumps`/`json.loads`), com `ensure_ascii` e `indent`.
- Problemas com parâmetros mutáveis (*mutable default arguments*).
- Exercícios: lista de tarefas persistida em JSON.
- Inclui imagem explicativa sobre `pathlib` (obtenção de caminhos).

### 📁 `aula178-arquivos-csv/`
- Estrutura do formato CSV; leitura com `csv.reader` e `csv.DictReader`.
- Escrita com `csv.writer` e `csv.DictWriter`.

## 8. Segurança, Aleatoriedade e Templates

### 📁 `aula181-funcao-random/`
- Módulo `random`: `seed`, `randrange`, `randint`, `uniform`, `random()`, `choice`, `shuffle`, `sample`, `choices`.
- Explica que são números **pseudoaleatórios** (não usar em contexto de segurança).

### 📁 `aula182-secrets-numeros-aleatorios-seguros/`
- Módulo `secrets` (`SystemRandom`) para geração **criptograficamente segura** de números, ideal para senhas e tokens.
- Comparação prática entre `random` (jogos/simulações) e `secrets` (segurança/autenticação).

### 📁 `aula183-string-template-exemplo-emails/`
- `string.Template` para substituir variáveis em textos — exemplo prático: e-mail de cobrança.

### 📁 `aula184-dotenv-variaveis-de-ambiente/`
- Uso do pacote `python-dotenv` para carregar variáveis sensíveis de um arquivo `.env` (inclui `.env-example` e `requirements.txt`).

### 📁 `aula185-envio-de-emails-smtp/`
- Envio de e-mails via **SMTP** em Python, incluindo template HTML (`aula185.html`) e variáveis de ambiente para credenciais.

### 📁 `aula186-compactar-e-descompactar-arquivos-zip/`
- Compactação e descompactação de arquivos `.zip` via módulo `zipfile`, com exemplos de diretórios de entrada/saída já gerados.

## 9. Automação, Sistema e Linha de Comando

### 📁 `aula187-sys.argv-exec-arquivos-com-args-no-sistema/`
- `sys.argv` para capturar argumentos de linha de comando (forma básica).
- `argparse.ArgumentParser` para criar CLIs profissionais (argumentos nomeados, `help`, obrigatórios/opcionais).

### 📁 `aula194-subprocess-executando-programas-e-comandos-externos/`
- Módulo `subprocess` (`subprocess.run`) para executar comandos do sistema operacional (Windows/Linux), capturar `stdout`/`stderr`, tratar codificação e usar `shell=True`.

### 📁 `aula196-threads-executando-processos-em-paralelo/`
- Criação de *threads* (herdando de `Thread`), uso de `target` e `join`.
- Controle de concorrência com `Lock` (exemplo: venda de ingressos evitando *race conditions*).

## 10. Web: HTTP, Scraping e Selenium

### 📁 `aula189-protocolo-http-hypertext-transfer-protocol/`
- Fundamentos do protocolo HTTP: métodos (GET, POST, PUT, PATCH, DELETE...), status codes, estrutura de requisição/resposta.
- Subpasta `aula190-site-em-html-e-css-e-http.server/`: site simples em HTML/CSS servido com `http.server`.
- `aula191-requests-http.py`: requisições HTTP reais com a biblioteca `requests`.

### 📁 `aula192-requests-beautiful-soup-web-scraping/`
- Web scraping com `requests` + `BeautifulSoup` (bs4): seletores CSS (`select`, `select_one`), limpeza de texto com regex e tratamento de codificação.

### 📁 `aula193-selenium-e-chromedriver.py/`
- Automação de navegador com **Selenium** + ChromeDriver: configuração do driver, `WebDriverWait`/`expected_conditions`, localização de elementos (ID, XPath), preenchimento de formulários e cliques automatizados.
- Exemplo real de login e "purga de cache" em painel WordPress, usando `.env` para credenciais.
- Inclui o executável `chromedriver.exe` na subpasta `drivers/`.

## 11. Processos, Paralelismo e Jupyter

### 📁 `aula195-jupyter/`
- Introdução ao **Jupyter Notebook**: células de código/markdown, execução interativa, boas práticas de organização.
- Contém notebooks de exemplo (`.ipynb`) e script de instalação/teste.

*(Ver também [Processos e Paralelismo](#9-automação-sistema-e-linha-de-comando) — `aula196-threads`.)*

## 12. Manipulação de PDFs, Planilhas e Imagens

### 📁 `aula197-pypdf/`
- Manipulação de PDFs com **PyPDF2**: leitura (`PdfReader`), extração de páginas, divisão e **junção (merge)** de arquivos PDF, uso de `pathlib` para gerenciar caminhos.
- Contém PDFs de exemplo (originais e gerados/mesclados).

### 📁 `aula199-openpyxl-trabalhando-com-planilhas/`
- Biblioteca **OpenPyXL** para arquivos Excel (`.xlsx`): criação, leitura, edição, estilização (cores, fontes, bordas), fórmulas e múltiplas abas.
- Arquivos `creating.py`, `reading.py` e uma planilha de exemplo (`workbook.xlsx`).

### 📁 `aula200-pillow-redimensionar-imagens/`
- Biblioteca **Pillow (PIL)** para processamento de imagens: abrir imagem, ler metadados EXIF, calcular redimensionamento **proporcional** (mantendo aspect ratio) e salvar com otimização/qualidade ajustável.
- Contém imagens de exemplo (`original.JPG` / `new.JPG`).

## 13. Interfaces Gráficas com PySide6

### 📁 `aula201-pyside6-interface-grafica-do-usuario-gui/`
- Introdução ao **PySide6**: `QApplication`, `QPushButton`, `QMainWindow`/`centralWidget`, sistema de **signals & slots**, classes e heranças de widgets.

### 📁 `aula202-calculadora-pyside6/`
Projeto prático: **calculadora gráfica completa** com PySide6, dividido em módulos:
- `main.py` (inicialização + tema escuro via `qdarkstyle`), `buttons.py` (grade de botões), `display.py` (campo de entrada), `info.py` (rótulo informativo), `main_window.py` (janela principal), `styles.py` (QSS/estilos), `utils.py` (validação/conversão de números) e `variables.py` (constantes/cores).
- Inclui ícone do app na subpasta `files/`.

## 14. Bancos de Dados (SQLite, MySQL/PyMySQL, Docker)

### 📁 `aula205-bases-de-dados-com-python-sqlite-e-pymysql/`
- Conexão e manipulação de bancos **SQLite** nativos do Python (`sqlite3`): criação de tabelas, `CREATE`/`INSERT`/`DELETE`, reset de sequência de IDs.
- `main.py`: ciclo **CRUD completo** (Create, Read, Update, Delete), inserção segura contra SQL Injection, inserções em lote.
- `select.py`: consultas (`SELECT`) simples e filtradas por ID.
- Gera o arquivo `db.sqlite3` como banco de dados de exemplo.

### 📁 `205-Bases-de-dados-com-python-sqlite-e-pymysql/`
- Pasta correlata (README ainda vazio/placeholder) — reservada para complementar os exemplos de SQLite/PyMySQL acima.

### 📁 `aula206-servidor-mysql-com-docker-compose/`
- Subida de um servidor **MySQL via Docker Compose** (`docker-compose.yml`) com variáveis de ambiente (`.env`/`.env-example`).
- Conexão com **PyMySQL**: `INSERT`/`SELECT`/`UPDATE`/`DELETE`, prevenção de SQL Injection com *placeholders* (`%s`, `%(name)s`).
- Cursores especiais: `DictCursor` (retorna dicionários), `SSCursor`/`SSDictCursor` (para grandes volumes de dados, *streaming*).
- Propriedades úteis: `rowcount`, `lastrowid`, `rownumber`, e uso de `mogrify` para depurar queries.

## 15. Testes Unitários, TDD e Doctest

### 📁 `seção-14-teste-unitario-unittest-tdd/`
- **TDD** (`src/conceito_tdd.py`): ciclo *Red, Green, Refactor* com o clássico exercício "Bacon com Ovos" (FizzBuzz).
- **Unittest** (`tests/`): testes com `unittest.TestCase`, `assertEqual`, `assertTrue`, para calculadora, pessoa e conceito de TDD.
- **Doctest** (`src/calculadora.py`, `doctests.py`): testes embutidos na documentação das funções, executáveis via `python -m doctest` ou diretamente no script.
- `src/pessoa.py`: classe com requisição HTTP (`requests`) para checar conectividade.
- Subpasta `tipagem-de-dados-type-hint-type-annotation/`: exemplos de *type hints*/*type annotations*.
- `assertion.py`: exemplos de `assert` para validação de tipos.

## 16. Design Patterns (Padrões de Projeto)

### 📁 `seção-17-design-patterns-python/`
Implementações práticas dos padrões clássicos do **GoF (Gang of Four)**, organizados em três categorias, cada padrão com seu próprio `.py`, `README.md` explicativo e, em vários casos, diagrama (`.png`/`.graphml`, editável no yEd). Inclui também um PDF teórico (`design-patterns.pdf`).

#### 🏗️ Creational (Padrões de Criação) — `creational/`
| Pasta | Padrão | Resumo |
|---|---|---|
| `singleton/` | **Singleton** | Garante que uma classe tenha apenas **uma instância** globalmente acessível. |
| `builder/` | **Builder** | Constrói objetos complexos passo a passo, separando construção de representação. |
| `prototype/` | **Prototype** | Cria novos objetos **clonando** um protótipo existente em vez de instanciar do zero. |
| `factories/simple-factory/` | **Simple Factory** | Centraliza a lógica de criação de objetos em um único método/classe. |
| `factories/factory-method/` | **Factory Method** | Delega a criação de objetos a subclasses, definindo uma interface comum de criação. |
| `factories/abstract-factory/` | **Abstract Factory** | Cria **famílias de objetos relacionados** sem especificar suas classes concretas. |

#### 🧱 Structural (Padrões Estruturais) — `structural/`
| Pasta | Padrão | Resumo |
|---|---|---|
| `adapter/` | **Adapter** | Permite que interfaces incompatíveis trabalhem juntas, "traduzindo" chamadas. |
| `bridge/` | **Bridge** | Desacopla uma abstração da sua implementação, permitindo que evoluam de forma independente. |
| `composite/` | **Composite** | Trata objetos individuais e composições (hierarquias parte-todo) de forma uniforme. |
| `decorator/` | **Decorator** | Adiciona funcionalidades a um objeto dinamicamente (exemplo: hotdog com ingredientes). |
| `facade/` | **Facade** | Fornece uma interface simplificada para um subsistema complexo (exemplo: estação meteorológica + observadores). |
| `flyweight/` | **Flyweight** | Otimiza memória compartilhando estado **intrínseco** entre muitos objetos (exemplo: endereços de clientes). |
| `proxy/` | **Proxy** | Objeto substituto que controla acesso ao objeto real — proxy **virtual** (lazy loading) e **inteligente** (cache), exemplo com `UserProxy`/`RealUser`. |

#### 🎭 Behavioral (Padrões Comportamentais) — `behavioral/`
| Pasta | Padrão | Resumo |
|---|---|---|
| `chain-of-responsibility/` | **Chain of Responsibility** | Passa uma solicitação por uma cadeia de handlers até que um a processe (versões com funções e com classes). |
| `command/` | **Command** | Encapsula uma solicitação/ação como um objeto, permitindo desfazer, enfileirar ou logar operações. |
| `iterator/` | **Iterator** | Permite percorrer elementos de uma coleção sem expor sua estrutura interna. |
| `mediator/` | **Mediator** | Centraliza a comunicação entre objetos, reduzindo o acoplamento direto entre eles. |
| `memento/` | **Memento** | Captura e restaura o estado interno de um objeto sem violar seu encapsulamento (ex: "desfazer"). |
| `observer/` | **Observer** | Notifica automaticamente múltiplos objetos ("observadores") quando o estado de outro objeto muda. |
| `state/` | **State** | Permite que um objeto altere seu comportamento quando seu estado interno muda. |
| `strategy/` | **Strategy** | Define uma família de algoritmos intercambiáveis, selecionados em tempo de execução. |
| `template-method/` | **Template Method** | Define o esqueleto de um algoritmo na superclasse, deixando etapas específicas para subclasses. |

---

## 🧰 Requisitos Gerais do Curso

A maior parte dos exemplos usa apenas a **biblioteca padrão** do Python. Alguns módulos exigem bibliotecas externas — cada pasta relevante tem seu próprio `requirements.txt`. As principais são:

- `python-dotenv` (variáveis de ambiente)
- `requests` e `beautifulsoup4` (HTTP e web scraping)
- `selenium` (automação de navegador)
- `pypdf2` (PDFs)
- `openpyxl` (planilhas Excel)
- `pillow` (imagens)
- `pyside6` + `qdarkstyle` (interfaces gráficas)
- `pymysql` (MySQL)
- `jupyter`/`notebook` (Jupyter Notebook)

> ⚠️ A pasta `.venv/` presente no material é o ambiente virtual usado durante o curso e **não** faz parte do conteúdo didático — pode ser ignorada ou recriada localmente com `python -m venv venv`.

---

## 📌 Como usar este README para revisão

1. Use o índice para pular direto ao tópico que precisa relembrar.
2. Cada pasta mencionada aqui tem, na maioria dos casos, seu **próprio `README.md`** com explicações linha a linha — abra-o quando precisar de mais profundidade.
3. Nas pastas de **Design Patterns**, sempre existe um diagrama (`.png`) que ajuda a visualizar as relações entre as classes — abra-o em conjunto com o `.py` correspondente.
4. Ao revisar POO (`aula120`), comece pelos conceitos básicos (classes, `self`, atributos) e avance progressivamente até os tópicos avançados (dunder methods, dataclasses, context managers).
