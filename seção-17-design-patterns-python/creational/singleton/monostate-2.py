"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
Ou seja, embora existam múltiplas instâncias da classe, todas compartilham
o mesmo dicionário de atributos.
"""
from __future__ import annotations # Permite o uso de anotações de tipo forward reference (tipos definidos mais tarde)
from typing import Dict # Importa o tipo Dict para anotações de tipo

# Mixin para fornecer uma representação de string útil para as classes
class StringReprMixin:
    # Método __str__ para representação "informal" do objeto
    def __str__(self) -> str:
        # Constrói uma string com todos os atributos e seus valores do dicionário __dict__ do objeto
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()] # Itera sobre os itens do dicionário e formata "chave=valor"
        )
        # Retorna o nome da classe seguido pelos atributos formatados
        return f'{self.__class__.__name__}({params})'

    # Método __repr__ para representação "oficial" do objeto (usado em depuração)
    def __repr__(self) -> str:
        # Por simplicidade, __repr__ chama __str__
        return self.__str__()


# Classe principal que implementa o padrão Monostate
class MonoState(StringReprMixin):
    # _state é um dicionário compartilhado por TODAS as instâncias da classe MonoState e suas subclasses.
    # Esta é a essência do Monostate: o estado é global, não por instância.
    _state: Dict = {}

    # O método __new__ é chamado antes do __init__ e é responsável por criar a instância do objeto.
    def __new__(cls, *args, **kwargs):
        # Chama o __new__ da classe pai para criar uma nova instância
        obj = super().__new__(cls)
        # ASSOCIA o dicionário de atributos da nova instância (_obj.__dict__) ao dicionário de estado compartilhado (_cls._state).
        # Isso significa que todas as instâncias terão o mesmo dicionário interno de atributos.
        obj.__dict__ = cls._state
        return obj

    # O método __init__ é chamado após o __new__ e é responsável por inicializar a instância.
    def __init__(self, nome=None, sobrenome=None) -> None:
        # Se 'nome' for fornecido, ele é adicionado/atualizado no dicionário _state (via obj.__dict__).
        if nome is not None:
            self.nome = nome
        # Se 'sobrenome' for fornecido, ele é adicionado/atualizado no dicionário _state.
        if sobrenome is not None:
            self.sobrenome = sobrenome


# Uma subclasse de MonoState. Ela também compartilhará o mesmo estado de _state.
class A(MonoState):
    pass


# Bloco principal para execução do código quando o script é executado diretamente
if __name__ == "__main__":
    # Cria a primeira instância de MonoState, definindo 'nome'.
    # Isso adiciona 'nome': 'Jean' ao _state compartilhado.
    m1 = MonoState(nome='Jean')
    # Cria uma instância da subclasse A, definindo 'sobrenome'.
    # Como A também é Monostate, ela compartilha o _state.
    # Isso adiciona 'sobrenome': 'Bortolon' ao MESMO _state.
    m2 = A(sobrenome='Bortolon')

    # Imprime m1. Agora, m1 terá tanto 'nome' quanto 'sobrenome',
    # porque ambos os atributos foram definidos no _state compartilhado.
    print(m1) # Saída esperada: MonoState(nome=Jean, sobrenome=Bortolon)
    # Imprime m2. m2 também terá tanto 'nome' quanto 'sobrenome'.
    print(m2) # Saída esperada: A(nome=Jean, sobrenome=Bortolon)

    # Para demonstrar que eles compartilham o mesmo estado, vamos adicionar outro atributo via m1
    m1.idade = 30
    print(f'm1 com idade: {m1}')
    print(f'm2 com idade: {m2}') # m2 também terá 'idade', pois o estado é compartilhado

    # Podemos verificar o dicionário de estado diretamente, se quisermos (apenas para debug/entendimento)
    # print(MonoState._state) # Saída esperada: {'nome': 'Jean', 'sobrenome': 'Bortolon', 'idade': 30}

