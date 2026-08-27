# IMPORTANDO O TIME PARA UTILIZAR O SLEEP E VER O NAVEGADOR ABERTO ANTES DE FECHAR
import time
# IMPORTANDO O OS PARA UTILIZAR VARIÁVEIS DE AMBIENTE
import os
# IMPORTANDO O DOTENV PARA CARREGAR AS VARIÁVEIS DE AMBIENTE DO ARQUIVO .ENV
from dotenv import load_dotenv
# IMPORTANDO O PATH PARA DEFINIR O CAMINHO DO CHROME DRIVER
from pathlib import Path
#I IMPORTANDO O WEBDRIVER DO SELENIUM PARA UTILIZAR O CHROME DRIVER
from selenium import webdriver
# IMPORTANDO O SERVICE DO SELENIUM PARA DEFINIR O CAMINHO DO CHROME DRIVER
from selenium.webdriver.chrome.service import Service   
# IMPORTANDO O BY DO SELENIUM PARA LOCALIZAR ELEMENTOS NA PÁGINA
from selenium.webdriver.common.by import By 
# IMPORTANDO O KEYS DO SELENIUM PARA UTILIZAR TECLAS DE ATALHO COMO ENTER, TAB, ETC
from selenium.webdriver.common.keys import Keys
# IMPORTANDO O SUPPORT WAIT - WEBDRIVERWAIT PARA ESPERAR ELEMENTOS APARECEREM NA PÁGINA
from selenium.webdriver.support.wait import WebDriverWait
# IMPORTANDO O SUPPORT EXPECTED CONDITIONS - EC PARA DEFINIR CONDIÇÕES DE ESPERA
from selenium.webdriver.support import expected_conditions as EC

# FUNÇÃO PARA CARREGAR AS VARIÁVEIS DE AMBIENTE DO ARQUIVO .ENV
load_dotenv()

# UTILIZANDO PATH PARA DEFINIR O CAMINHO DO CHROME DRIVER
PASTA_RAIZ = Path(__file__).parent

# NAVEGA ATÉ A PASTA DRIVER CONCATENANDO O CAMINHO NA PASTA RAIZ
PASTA_DO_DRIVER = PASTA_RAIZ / 'drivers'

# NAVEGA ATÉ O ARQUIVO CHROME DRIVER CONCATENANDO O CAMINHO NA PASTA DO DRIVER
CHROME_DRIVER_PATH = PASTA_DO_DRIVER / 'chromedriver.exe'

print(CHROME_DRIVER_PATH)

# print(CHROME_DRIVER_PATH)

# CHAMANDO O CHROME DRIVER PARA APLICAR CONFIGURAÇÕES
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--log-level=0')

# CHAMANDO O CHROME SERVICE PARA DEFINIR O CAMINHO DO CHROME DRIVER
chrome_service = Service(executable_path= str(CHROME_DRIVER_PATH))

# CHAMANDO O CHROME BROWSER PARA DEFINIR O NOME DO NAVEGADOR
chrome_browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

# A CONFIGURAÇÃO ACIMA É A BASE PARA QUALQUER UTILIZAÇÃO DO SELENIUM

# AGORA VOU ABRIR UM SITE UTILIZANDO GET - ADMIN DO WORD PRESS
chrome_browser.get(os.getenv("WP_URL"))

# ESPERE PARA ENCONTRAR CAMPO DE USUÁRIO O WEBDRIVERWAIT E O BY PARA LOCALIZAR O ELEMENTO PELO NOME
search_input = WebDriverWait(chrome_browser, 10).until(
    EC.presence_of_element_located((By.ID, 'user_login'))
)
time.sleep(2)
# ENVIE O TEXTO DE USUÁRIO PARA O CAMPO LOGIN DO ADM WORD PRESS
search_input.send_keys(os.getenv("WP_USER"))
time.sleep(2)

# ENCONTRA O CAMPO SENHA
search_input = WebDriverWait(chrome_browser, 10).until(
    EC.presence_of_element_located((By.ID, 'user_pass'))
)
time.sleep(2)
# ESCREVE A SENHA NO CAMPO ENCONTRADO
search_input.send_keys(os.getenv("WP_PASS"))
time.sleep(2)
# APERTA ENTER PARA LOGAR
search_input.send_keys(Keys.ENTER)
time.sleep(4)

# APÓS LOGAR CLICA NO BOTÃO DE PURGAR O CACHE DO SITE - PRIMEIRO BOTÃO
purge_btn = WebDriverWait(chrome_browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='wp-admin-bar-wpo_purge_cache']/a"))
)
purge_btn.click()
time.sleep(1)

# FINALIZA CLICANDO NO SEGUNDO BOTÃO QUE EXECUTA OS COMANDOS
purge_all_btn = WebDriverWait(chrome_browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='wp-admin-bar-wpo_purge_all_pages_cache']/a"))
)
purge_all_btn.click()
time.sleep(1)



# TEMPO PARA VER O NAVEGADOR ABERTO ANTES DE FECHAR 10 SEGUNDOS
time.sleep(10)