# Documentação da pasta aula193-selenium-e-chromedriver.py

Esta pasta contém exemplos práticos de automação de tarefas no navegador utilizando Selenium WebDriver com o ChromeDriver em Python. Abaixo estão os principais recursos abordados nos scripts presentes na pasta:

## Conteúdo dos Programas

### 1. Configuração do Selenium e ChromeDriver
- Como definir o caminho do `chromedriver.exe` usando `pathlib.Path`.
- Criação de instância do navegador Chrome com opções customizadas (`webdriver.ChromeOptions`).
- Uso do `Service` para especificar o executável do driver.

### 2. Abertura e navegação em sites
- Abertura de sites com `browser.get(url)`.
- Espera explícita de elementos usando `WebDriverWait` e `expected_conditions` (EC).
- Interação com campos de formulário (login, senha, busca) usando `send_keys` e `Keys.ENTER`.

### 3. Localização de elementos
- Localização por ID, XPATH e outros seletores com `By`.
- Uso de `element_to_be_clickable` para garantir que o elemento está pronto para interação.

### 4. Execução de ações automatizadas
- Preenchimento de campos de login e senha.
- Clique em botões e links usando `.click()`.
- Execução de comandos sequenciais para automação de tarefas administrativas (ex: purgar cache em painel WordPress).

### 5. Uso de variáveis de ambiente
- Carregamento de variáveis sensíveis (usuário, senha, URL) a partir de arquivo `.env` usando o pacote `python-dotenv`.
- Boas práticas para não expor dados sensíveis no código-fonte.

### 6. Boas práticas e dicas
- Uso de `time.sleep()` para aguardar visualização ou carregamento.
- Impressão de caminhos e mensagens para depuração.
- Organização do código em etapas lógicas e comentadas.

## Requisitos
- Python 3.x
- Pacotes: `selenium`, `python-dotenv`
- ChromeDriver compatível com a versão do Google Chrome instalada

## Exemplos de arquivos presentes
- `aula193-selenium-e-chromedriver.py`: Exemplo básico de automação com Selenium e ChromeDriver.
- `aula193-teste-jean.py`: Script de automação de login e busca no Google.
- `aula193-teste-jean-purga-site.py`: Script de automação de login e purga de cache em painel WordPress, usando variáveis de ambiente.

## Observações
- Sempre mantenha o ChromeDriver atualizado e compatível com seu navegador.
- Nunca compartilhe arquivos `.env` com dados sensíveis.
- Consulte a documentação oficial do Selenium para mais recursos: https://selenium-python.readthedocs.io/

---

Esta documentação serve como referência rápida para os recursos e exemplos de automação web presentes nesta pasta.
