# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

# RESOLUÇÃO JEAN

def mult(num):
    a = num * 2
    b = num * 3
    c = num * 4
    return f' Seu número duplicado vale:{a},Seu número triplicado vale:{b}, Seu número quadruplicado vale:{c}'

mycalcs = mult(3)
print(mycalcs)

# RESOLUÇÃO PROFESSOR

# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2


# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
