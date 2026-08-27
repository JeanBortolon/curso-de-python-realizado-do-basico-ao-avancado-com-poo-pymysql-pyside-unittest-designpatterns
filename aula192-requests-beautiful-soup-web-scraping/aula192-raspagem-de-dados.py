# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4

# IMPORTA A BIBLIOTECA DE EXPRESSÕES REGULARES PARA LIMPAR O TEXTO EXTRAÍDO DO HTML
import re
 
# IMPORTA AS BIBLIOTECAS NECESSÁRIAS PARA REALIZAR A RASPAGEM DE DADOS DE UM SITE REQUESTS E BEAUTIFULSOUP4
import requests
from bs4 import BeautifulSoup
 
# URL DO SITE CONSTRUÍDO NA AULA 189 RODANDO LOCAL HOST PARA BUSCARMOS DADOS 
url = 'http://127.0.0.1:5500/aula189-protocolo-http-hypertext-transfer-protocol/aula190-site-em-html-e-css-e-http.server/index.html#home'

# OBTÉM O CONTEÚDO DO SITE ATRAVÉS DE UM REQUEST HTTP COM GET E ARMAZENA EM UMA VARIÁVEL
response = requests.get(url)
# OBTÉM OS BYTES DO CONTEÚDO DO SITE PARA PARSEAR
bytes_html = response.content
# APLICA O BEAUTIFULSOUP PARA PARSEAR O HTML E TRANSFORMÁ-LO EM OBJETOS PYTHON, INFORMANDO A CODIFICAÇÃO DE CARACTERES UTF-8
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')
# SELECIONA O ELEMENTO H2 QUE ESTÁ DENTRO DO ARTIGO QUE FALA SOBRE AS VAGAS DE EMPREGO E ARMAZENA EM UMA VARIÁVEL
top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
# TRATA O TEXTO DO ELEMENTO H2 PARA REMOVER ESPAÇOS EXTRAS E IMPRIME O RESULTADO 
if top_jobs_heading is not None:
    article = top_jobs_heading.parent
    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())



'''Caso queira mudar a codificação de caracteres, envie os bytes diretamente para o BeautifulSoup 
e passe o valor da codificação de caracteres no atributo "from_encoding". Exemplo (para utf-8):
BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')
Perceba que troquei "response.text" para "response.content" para obter os bytes ao invés da string.'''