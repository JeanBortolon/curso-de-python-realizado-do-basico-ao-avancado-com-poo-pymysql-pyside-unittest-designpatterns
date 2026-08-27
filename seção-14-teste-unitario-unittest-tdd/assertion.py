"""
Uma instrução assert em Python é uma ferramenta de depuração que
testa uma condição. Se a condição for verdadeira, o programa
continua. Caso contrário, levanta um erro AssertionError. Elas
validam suposições internas e ajudam a detectar falhas no
desenvolvimento.
"""

# assert condicao, "Mensagem de erro opcional"

def calcular_desconto(preco, percentual):
    # Garante que o preço nunca seja negativo
    assert preco >= 0, "O preço não pode ser negativo"
    
    desconto = preco * (percentual / 100)
    return preco - desconto

# Uso normal
print(calcular_desconto(100, 10))

# Isso irá gerar um AssertionError: "O preço não pode ser negativo"
calcular_desconto(-50, 10)

