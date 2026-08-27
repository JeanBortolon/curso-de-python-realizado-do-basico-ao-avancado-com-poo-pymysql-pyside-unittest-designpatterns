# Usando subprocess para executar comandos externos
# subprocess é um módulo do Python para executar
# processos e comandos externos no seu programa.
# O método mais simples para atingir o objetivo é usando subprocess.run().
# Argumentos principais de subprocess.run():
# - stdout, stdin e stderr -> Redirecionam saída, entrada e erros
# - capture_output -> captura a saída e erro para uso posterior
# - text -> Se True, entradas e saídas serão tratadas como texto
#   e automaticamente codificadas ou decodificadas com o conjunto
#   de caracteres padrão da plataforma (geralmente UTF-8).
# - shell -> Se True, terá acesso ao shell do sistema. Ao usar
#   shell (True), recomendo enviar o comando e os argumentos juntos.
# - executable -> pode ser usado para especificar o caminho
#   do executável que iniciará o subprocesso.
# Retorno:
#   stdout, stderr, returncode e args
# Importante: a codificação de caracteres do Windows pode ser
# diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
# mac, use utf_8.

import subprocess  # Importa o módulo para executar comandos externos
import sys         # Importa para identificar o sistema operacional

# sys.platform pode ser: linux, linux2, darwin, win32

print(sys.platform)  # Exibe o sistema operacional atual

# Comando padrão para sistemas Unix (Linux/Mac)
cmd = ['ls -lah /']
encoding = 'utf_8'  # Codificação padrão para Unix
system = sys.platform  # Identifica o sistema operacional

# Se for Windows, ajusta o comando e a codificação
if system == "win32":
    cmd = ['ping', '127.0.0.1']  # Comando de exemplo para Windows
    encoding = 'cp850'           # Codificação comum no Windows

# Executa o comando externo usando subprocess.run
proc = subprocess.run(
    cmd, capture_output=True,   # Captura stdout e stderr
    text=True,                 # Trata entrada/saída como texto
    encoding=encoding,         # Usa a codificação correta
    shell=True,                # Executa no shell do sistema
)

print()  # Linha em branco para separar a saída

# Exibe a saída padrão do comando executado
print(proc.stdout)
# Outras opções úteis (comentadas):
# print(proc.args)      # Mostra os argumentos usados
# print(proc.stderr)    # Mostra a saída de erro, se houver
# print(proc.returncode) # Mostra o código de retorno do processo