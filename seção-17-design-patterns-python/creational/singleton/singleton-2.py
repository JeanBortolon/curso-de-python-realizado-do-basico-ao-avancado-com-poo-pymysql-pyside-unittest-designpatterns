# O padrão Singleton garante que uma classe tenha apenas uma instância
# e fornece um ponto de acesso global para essa instância.

def singleton(the_class):
    # Dicionário para armazenar as instâncias das classes decoradas.
    # A chave é a classe e o valor é a instância única dessa classe.
    instances = {}

    # Esta função interna será a responsável por gerenciar a criação
    # e retorno da instância única.
    def get_class(*args, **kwargs):
        # Verifica se a classe ainda não possui uma instância no dicionário.
        if the_class not in instances:
            # Se não houver, cria uma nova instância da classe
            # e a armazena no dicionário.
            instances[the_class] = the_class(*args, **kwargs)
        # Retorna a instância única da classe.
        return instances[the_class]

    # Retorna a função interna que gerencia a instância.
    return get_class


# Aplica o decorator 'singleton' à classe AppSettings.
# Isso garante que AppSettings terá apenas uma instância.
@singleton
class AppSettings:
    def __init__(self) -> None:
        # Inicializa os atributos da instância.
        # Estes atributos serão os mesmos para todas as "referências" à instância única.
        self.tema = 'O tema escuro'
        self.font = '18px'


# Aplica o decorator 'singleton' à classe Teste.
# Isso garante que Teste terá apenas uma instância.
@singleton
class Teste:
    def __init__(self) -> None:
        # A classe Teste não tem atributos específicos, apenas demonstra o Singleton.
        pass


# Bloco principal de execução, que será executado quando o script for rodado diretamente.
if __name__ == "__main__":
    # Cria (ou obtém a instância única de) AppSettings.
    as1 = AppSettings()
    # Modifica um atributo da instância única.
    as1.tema = 'O tema claro'
    # Imprime o valor do atributo modificado.
    print(as1.tema)

    # Cria (ou obtém a *mesma* instância única de) AppSettings.
    # Note que as2 não é uma nova instância, mas uma referência à instância existente.
    as2 = AppSettings()
    # Imprime o atributo 'tema' através de as1.
    # O valor será 'O tema claro' porque as1 e as2 compartilham a mesma instância.
    print(as1.tema)

    # Cria (ou obtém a instância única de) Teste.
    t1 = Teste()
    # Cria (ou obtém a *mesma* instância única de) Teste.
    t2 = Teste()
    # Compara se t1 e t2 são a mesma instância.
    # Deve imprimir True, confirmando que o padrão Singleton está funcionando.
    print(t1 == t2)
