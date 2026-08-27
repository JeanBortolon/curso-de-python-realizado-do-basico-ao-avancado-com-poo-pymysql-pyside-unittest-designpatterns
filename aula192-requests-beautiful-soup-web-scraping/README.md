# Documentação da pasta aula192-requests-beautiful-soup-web-scraping

Esta pasta contém exemplos práticos de Web Scraping em Python utilizando as bibliotecas `requests` e `BeautifulSoup` (bs4). Os scripts demonstram como coletar, interpretar e tratar dados de páginas web de forma automatizada.

## Conteúdo dos Programas

### 1. Web Scraping com Requests e BeautifulSoup
- Explicação do conceito de Web Scraping e suas aplicações.
- Uso da biblioteca `requests` para realizar requisições HTTP e obter o conteúdo de páginas web.
- Utilização do `BeautifulSoup` para fazer o parsing do HTML e navegar pela estrutura da página.
- Seleção de elementos HTML usando seletores CSS (`select_one`, `select`).
- Extração e limpeza de textos de elementos HTML utilizando expressões regulares (`re.sub`).
- Tratamento de codificação de caracteres ao processar o conteúdo das páginas.

### 2. Boas Práticas e Dicas
- Como identificar e selecionar elementos específicos em uma página HTML.
- Diferença entre `response.text` (string) e `response.content` (bytes) e quando usar cada um.
- Como garantir a correta leitura de caracteres especiais usando o parâmetro `from_encoding` no BeautifulSoup.
- Comentários explicativos para facilitar o entendimento do fluxo do código.

## Requisitos
- Python 3.x
- Pacotes: `requests`, `beautifulsoup4`

## Exemplos de arquivos presentes
- `aula192-raspagem-de-dados.py`: Script principal demonstrando o processo completo de scraping, parsing e extração de dados de uma página HTML local.

## Observações
- Sempre respeite as políticas de uso dos sites ao fazer scraping.
- Consulte a documentação oficial para aprofundar:
  - Requests: https://docs.python-requests.org/
  - BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/

---

Esta documentação serve como referência rápida para os recursos e exemplos de Web Scraping presentes nesta pasta.
