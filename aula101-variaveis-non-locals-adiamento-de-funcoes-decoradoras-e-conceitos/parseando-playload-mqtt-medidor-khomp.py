khomp = [{"bn": "F8033201000309A3", "bt": 1766151487},\
        {"n": "uplink", "u": "count", "v": 536},\
        {"n": "activation_mode", "vs": "OTAA"},\
        {"n": "datarate", "vs": "SF9BW125"},\
        {"n": "rssi", "u": "dBW", "v": -90},\
        {"n": "snr", "u": "dB", "v": 9.5}, \
        {"n": "model", "vs": "nit21li"}, \
        {"n": "ext_pwr", "vb": True},\
        {"n": "temperatura", "u": "Cel", "v": 30.480000000000018},\
        {"n": "umidade", "u": "%RH", "v": 38.5},\
        {"n": "C1", "vb": False},\
        {"n": "C2", "vb": False},\
        {"n": "current-E1", "u": "A", "v": 1.9999999999999999e-06},\
        {"n": "current-E2", "u": "A", "v": 3.6999999999999998e-05},\
        {"n": "current-E3", "u": "A", "v": 1.9999999999999999e-06},\
        {"n": "current-E4", "u": "A", "v": 1.9999999999999999e-06},\
        {"n": "gateway", "vs": "F80332034EA70000"}]



for i, item in enumerate(khomp):
    globals()[f"dict_{i}"] = item

#Exemplo de acesso aos dicionários individuais
#print(dict_8)
#print(dict_9)


temp = f'"{dict_8['n']}": "{dict_8['v']}"' #Concatena nome temp e valor
umi = f'"{dict_9['n']}": "{dict_9['v']}"' #Concatena nome umi e valor

payload_khomp = '{' + temp + "," + umi + '}' #monta payload completa
print(payload_khomp)


'''Para acessar cada valor do dicionário `{'n': 'temperatura', 'u': 'Cel', 'v': 30.480000000000018}` de forma individual em Python, você pode usar as chaves do dicionário. Aqui está um exemplo:

# Dicionário
dados = {'n': 'temperatura', 'u': 'Cel', 'v': 30.480000000000018}

[b]Acessando os valores individualmente[/b]
nome = dados['n'] # 'temperatura'
unidade = dados['u'] # 'Cel'
valor = dados['v'] # 30.480000000000018

[b]Exibindo os valores[/b]
print(f"Nome: {nome}")
print(f"Unidade: {unidade}")
print(f"Valor: {valor}")

Saída:
Nome: temperatura
Unidade: Cel
Valor: 30.480000000000018'''