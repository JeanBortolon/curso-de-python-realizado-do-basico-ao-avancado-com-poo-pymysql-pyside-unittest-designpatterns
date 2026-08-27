"""
Monostate (ou Borg) - É uma variação do Singleton proposto
por Alex Martelli que tem a intenção de garantir que o
estado do objeto seja igual para todas as instâncias.
Ou seja, todos os objetos compartilham o mesmo dicionário de atributos.
"""
from __future__ import annotations
from typing import Dict


# Mixin para fornecer uma representação de string amigável para classes
# herdando dele. Isso facilita a depuração e a visualização dos objetos.
class StringReprMixin:
    # Retorna uma representação de string do objeto para exibição em log ou print.
    def __str__(self) -> str:
        # Constrói uma string com os atributos e seus valores (ex: "nome=Jean, sobrenome=Bortolon").
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        # Retorna o nome da classe seguido dos atributos entre parênteses.
        return f'{self.__class__.__name__}({params})'

    # Retorna uma representação "oficial" do objeto. Por convenção, chama __str__.
    def __repr__(self) -> str:
        return self.__str__()


# Implementação do padrão Monostate.
# Todos os objetos desta classe (e suas subclasses, se houver) compartilharão
# o mesmo estado (os mesmos atributos e valores).
class MonoStateSimple(StringReprMixin):
    # _state é o dicionário que conterá o estado compartilhado entre todas as instâncias.
    # Ele é uma variável de classe e, portanto, é o mesmo para todos os objetos.
    _state: Dict = {}

    # O método construtor.
    def __init__(self, nome=None, sobrenome=None) -> None:
        # CRUCIAL para o Monostate: Redireciona o dicionário de instância (__dict__)
        # para o dicionário de estado compartilhado (_state).
        # Isso faz com que todas as instâncias operem no mesmo conjunto de dados.
        self.__dict__ = self._state

        # Se 'nome' for fornecido, atualiza o atributo 'nome' no estado compartilhado.
        if nome is not None:
            self.nome = nome

        # Se 'sobrenome' for fornecido, atualiza o atributo 'sobrenome' no estado compartilhado.
        if sobrenome is not None:
            self.sobrenome = sobrenome


# Bloco principal para testar a implementação do Monostate.
if __name__ == "__main__":
    # Cria a primeira instância. Define 'nome'.
    m1 = MonoStateSimple(nome='Jean')
    # Cria a segunda instância. Define 'sobrenome'.
    # Como o estado é compartilhado, 'm2' terá o 'nome' de 'm1' e adicionará seu 'sobrenome'.
    m2 = MonoStateSimple(sobrenome='Bortolon')
    
    # Imprime m1. Ele exibirá tanto 'nome' quanto 'sobrenome', pois o estado é o mesmo que m2.
    print(m1)
    # Imprime m2. Ele exibirá tanto 'nome' quanto 'sobrenome', o mesmo estado que m1.
    print(m2)

    # Cria uma terceira instância, alterando o 'nome'.
    # Isso afetará 'm1' e 'm2' também, pois todos compartilham o mesmo estado.
    m3 = MonoStateSimple(nome='João')
    print(m3)
    print(m1) # m1 agora também terá o nome 'João'

