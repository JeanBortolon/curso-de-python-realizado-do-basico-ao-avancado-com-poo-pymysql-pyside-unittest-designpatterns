# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('CALL é executado')
#         return super().__call__(*args, **kwargs)


# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwargs):
#         print('NEW é executado')
#         return super().__new__(cls)

#     def __init__(self, nome):
#         print('INIT é executado')
#         self.nome = nome

#     def __call__(self, x, y):
#         print('Call chamado', self.nome, x + y)


# p1 = Pessoa('Jean')
# print(p1.nome)
from typing import Dict


class Singleton(type):
    # Dicionário para armazenar as instâncias únicas de cada classe que usa esta metaclasse.
    _instances: Dict = {}

    # O método __call__ de uma metaclasse é chamado quando uma classe (que usa esta metaclasse)
    # é "chamada" ou instanciada (e.g., AppSettings()).
    def __call__(cls, *args, **kwargs):
        # Verifica se a classe atual (cls) já possui uma instância no dicionário _instances.
        if cls not in cls._instances:
            # Se não houver uma instância, cria uma nova chamando o __call__ da superclasse (type).
            # Isso efetivamente chama o __new__ e depois o __init__ da classe.
            cls._instances[cls] = super().__call__(*args, **kwargs)
        # Retorna a instância única armazenada para a classe.
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    # AppSettings usa Singleton como sua metaclasse, garantindo que apenas uma instância
    # de AppSettings possa ser criada.
    def __init__(self) -> None:
        # Define atributos iniciais para a única instância de AppSettings.
        self.tema = 'O tema escuro'
        self.font = '18px'


if __name__ == "__main__":
    # A primeira instanciação de AppSettings.
    # A metaclasse Singleton garante que esta é a única vez que __init__ será chamado.
    as1 = AppSettings()

    # Modificando um atributo da única instância.
    as1.tema = 'Qualquer outra coisa'

    # A segunda e terceira instanciações de AppSettings.
    # A metaclasse Singleton retornará a instância existente (as1) e não criará novas.
    as2 = AppSettings()
    as3 = AppSettings()

    # Imprime o tema de as3. Como as1, as2 e as3 são a mesma instância,
    # o valor será 'Qualquer outra coisa'.
    print(as3.tema)
    # Verifica se as1 e as2 são a mesma instância (deve ser True).
    print(as1 == as2)
    # Verifica se as1 e as3 são a mesma instância (deve ser True).
    print(as1 == as3)
    # Verifica se as2 e as3 são a mesma instância (deve ser True).
    print(as2 == as3)

