"""
O Singleton tem a intenção de garantir que uma classe tenha somente
uma instância e fornece um ponto global de acesso para a mesma.

When discussing which patterns to drop, we found
that we still love them all.
(Not really—I'm in favor of dropping Singleton.
Its use is almost always a design smell.)
- Erich Gamma, em entrevista para informIT
http://www.informit.com/articles/article.aspx?p=1404056
"""


# Definição da classe AppSettings que implementará o padrão Singleton.
class AppSettings:
    # Atributo de classe para armazenar a única instância da classe.
    # Inicialmente definido como None, indicando que nenhuma instância foi criada ainda.
    _instance = None

    # O método __new__ é chamado antes do __init__ e é responsável por criar a instância do objeto.
    def __new__(cls, *args, **kwargs):
        # Verifica se já existe uma instância da classe.
        if not cls._instance:
            # Se não existir, chama o método __new__ da classe pai (object) para criar a instância.
            cls._instance = super().__new__(cls, *args, **kwargs)
        # Retorna a instância existente ou a recém-criada.
        return cls._instance

    # O método __init__ é o construtor da classe e é chamado após __new__.
    def __init__(self) -> None:
        """ O init será chamado todas as vezes """
        # Este comentário original indica que __init__ é chamado em cada "tentativa" de criação de instância,
        # mesmo que __new__ retorne uma instância já existente. Isso significa que o estado pode ser redefinido
        # se não for tratado com cuidado.
        self.tema = 'O tema escuro'  # Atributo para definir o tema da aplicação.
        self.font = '18px'          # Atributo para definir o tamanho da fonte.


# Bloco principal de execução do script.
if __name__ == "__main__":
    # Cria a primeira instância de AppSettings.
    # O método __new__ será chamado, criará a instância e a armazenará em _instance.
    # Em seguida, __init__ será chamado para inicializar tema e font.
    as1 = AppSettings()
    # Modifica o atributo 'tema' da instância.
    as1.tema = 'O tema claro'
    # Imprime o tema da primeira instância.
    print(as1.tema)

    # Tenta criar uma segunda instância de AppSettings.
    # O método __new__ será chamado, mas como _instance já existe, ele retornará a instância existente (as1).
    # O método __init__ será chamado novamente na mesma instância (as1), redefinindo o tema para 'O tema escuro'
    # e a fonte para '18px', se não fosse o caso de ter sido alterado acima.
    # Devido à execução sequencial, neste ponto as2 É A MESMA INSTÂNCIA QUE as1.
    as2 = AppSettings()
    # Imprime o tema da (agora única) instância, que será o último valor atribuído.
    # Isso demonstra que ambas as variáveis (as1 e as2) apontam para o mesmo objeto.
    print(as1.tema)

