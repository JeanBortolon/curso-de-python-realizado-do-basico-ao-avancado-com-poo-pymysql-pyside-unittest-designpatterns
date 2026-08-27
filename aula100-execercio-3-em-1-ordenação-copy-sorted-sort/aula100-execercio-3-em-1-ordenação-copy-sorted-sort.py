# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy # módulo para trabalhar com cópia de dados 
from dados_package.produtos_modulo import produtos


# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# copy.deepcopy(produtos) cria uma cópia profunda

# Solução Professor
novos_produtos = [ {**p, 'preco':round(p['preco'] *1.1,2)} 
                  for p in copy.deepcopy(produtos) ]


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Solução Professor
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), key=lambda p:p['nome']
    ,reverse=True)


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
# Solução Professor
produtos_ordenados_por_preco = produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos), key=lambda p:p['preco']
    ,reverse=False)



print(*produtos, sep='\n') # * desempacota o dicionário da lista

print()  # print vazio para criar espaço entre os dicionários.
print()
      
print(*produtos_ordenados_por_nome, sep='\n') # inclui separador com quebra de linha
# para facilitar a visualização



'''SOLUÇÃO JEAN

# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

i = 0
while i <= 4:
    print()
    novos_produtos[i]['preco'] = round(novos_produtos[i]['preco'] * 1.1,2)
    i += 1

print(*novos_produtos, sep='\n')
'''




