# Importa o mixin de log para salvar mensagens em arquivo
from log import LogFileMixin


# Classe base para eletrônicos
class Eletronico:
    def __init__(self, nome):
        self._nome = nome  # Nome do eletrônico
        self._ligado = False  # Estado inicial: desligado

    def ligar(self):
        # Liga o eletrônico se estiver desligado
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        # Desliga o eletrônico se estiver ligado
        if self._ligado:
            self._ligado = False


# Classe Smartphone herda de Eletronico e LogFileMixin para logar ações
class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()  # Chama o método ligar da classe base

        if self._ligado:
            msg = f'{self._nome} está ligado'
            self.log_success(msg)  # Loga mensagem de sucesso ao ligar

    def desligar(self):
        super().desligar()  # Chama o método desligar da classe base

        if not self._ligado:
            msg = f'{self._nome} está desligado'
            self.log_error(msg)  # Loga mensagem de erro ao desligar