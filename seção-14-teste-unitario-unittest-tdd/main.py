# Importa a função soma do módulo calculadora
from calculadora import soma

# Linhas comentadas que poderiam ser usadas para testar a função soma com diferentes valores
# print(soma(10,20))  # Soma de dois números inteiros
# print(soma(-10,20))  # Soma de um número negativo com um positivo
# print(soma(1.5,2.5))  # Soma de dois números de ponto flutuante

# Bloco try-except para capturar erros de validação na função soma
try:
    # Tenta realizar a soma de uma string com um número inteiro, o que deve gerar um erro
    print(soma('15', 15))
except AssertionError as e:
    # Captura o erro e imprime uma mensagem indicando que a conta é inválida
    print(f'Conta inválida: {e}')

# Realiza uma soma válida e imprime o resultado
print('Conta', soma(25,25))

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    # Importa o módulo doctest para executar testes embutidos na documentação
    import doctest
    # Executa os testes definidos na documentação do módulo
    doctest.testmod()