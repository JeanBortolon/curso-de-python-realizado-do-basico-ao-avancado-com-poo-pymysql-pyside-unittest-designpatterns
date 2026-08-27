# Importa o módulo requests para realizar requisições HTTP
import requests

# Define a classe Pessoa que representa uma pessoa
class Pessoa:
    # Método construtor que inicializa os atributos da classe
    def __init__(self, nome, sobrenome):
        self.nome = nome  # Atributo para armazenar o nome da pessoa
        self.sobrenome = sobrenome  # Atributo para armazenar o sobrenome da pessoa
        self.dados_obtidos = False  # Atributo para indicar se os dados foram obtidos

    # Método para obter todos os dados de uma pessoa
    def obter_todos_os_dados(self):
        # Realiza uma requisição HTTP GET para obter dados (URL está vazia no momento)
        # resposta = requests.get('https:/jsonplaceholder.typicode.com/users/1')
        resposta = requests.get('')

        # Verifica se a resposta da requisição foi bem-sucedida
        if resposta.ok:
            return 'CONECTADO'  # Retorna "CONECTADO" se a requisição foi bem-sucedida
        else:
            return 'ERRO 404'  # Retorna "ERRO 404" se houve erro na requisição