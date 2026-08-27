"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

#CONVENÇÃO EM PYTHON PARA CRIAR UMA CONSTANTE
# É COLOCAR O NOME DA VAR EM MAIUSCULO POIS
# NÃO EXISTE CONSTANTE EM PYTHON

'''A IDÉIA ABAIXO É QUE O CARRO SEJA MULTADO
AO PASSAR DA VELOCIDADE PERMITIDA NO LOCAL DO
RADAR, COM RANGE DE LOCAL -1 E +1 OU SEJA
MULTAR NOS KM 99,100 E 101, VAMOS FAZER COM IF
E MUITA LÓGICA, MOSTRANDO COMO É RUIM E DEPOIS
ATRIBUIR LÓGICAS EM VARIÁVEIS PARA REDUZIR
CÓDIGO E OTIMIZAR, PARA QUEBRAR LINHA EM PYTHON
E NÃO SAIR ESCREVENDO MT CÓDIGO PARA LA >>
POSSO COLOCAR A BARRA INVERTIDA'''

#Exemplo com muita lógica:
'''
if velocidade > RADAR_1:
    print('Velocidade do carro acima do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
    velocidade > RADAR_1:
    print('carro multado no radar 1')
'''

#Exemplo com variáveis para reduzir a lógica
#Basicamente o conceito de flag atendendo criterio

vel_ultrapassa = velocidade > RADAR_1
carro_passou_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
carro_passou_2 = local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_passou_radar_1 = carro_passou_1 and carro_passou_2


if vel_ultrapassa:
    print('Velocidade do carro acima do radar 1')

if carro_passou_radar_1:
    print('carro passou no radar 1')

if vel_ultrapassa and carro_passou_radar_1:
    print('carro multado no radar 1')