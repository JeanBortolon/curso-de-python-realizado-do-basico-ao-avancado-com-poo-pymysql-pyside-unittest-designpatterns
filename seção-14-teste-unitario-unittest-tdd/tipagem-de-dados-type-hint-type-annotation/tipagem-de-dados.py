# Importando tipos do módulo typing para usar anotações de tipo
from typing import List, Union, Tuple, Dict, NewType, Callable, Sequence, Iterable

# Primitivos
numero: int = 10  # Variável do tipo inteiro
flutuante: float = 10.5  # Variável do tipo float (número de ponto flutuante)
booleano: bool = False  # Variável do tipo booleano
string: str = 'Luiz Otávio'  # Variável do tipo string

# Sequências
lista: List[int] = [1, 2, 3]  # Lista contendo apenas inteiros
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Luiz']  # Lista contendo inteiros ou strings
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Luiz')  # Tupla com tipos definidos para cada posição

# Dicionários e conjuntos

# Criando um alias (apelido) para um tipo de dicionário
MeuDict = Dict[str, Union[str, int, List[int]]]  # Dicionário com chaves string e valores variados

# Dicionário com chaves string e valores string ou inteiro
pessoa: Dict[str, Union[str, int]] = {
    'nome': 'Luiz Otávio', 'sobrenome': 'Miranda', 'idade': 30
}

# Dicionário usando o alias criado anteriormente
pessoa2: MeuDict = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 30,
    'l': [1, 2]  # Lista de inteiros como valor
}

# Criando um novo tipo chamado UserId
UserId = NewType('UserId', int)  # Define um tipo distinto baseado em int
user_id = UserId(325456789)  # Variável do tipo UserId

# Função que recebe outra função como argumento e retorna uma função
def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao

# Função que soma dois números inteiros e retorna um inteiro
def soma(x: int, y: int) -> int:
    return x + y

# Chamando a função retorna_funcao com a função soma e executando-a com argumentos
print(retorna_funcao(soma)(10, 20))

# Classe que representa uma pessoa
class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        # Atributos da classe com tipos definidos
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    # Método que imprime uma mensagem indicando que a pessoa está falando
    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')