# Exemplo de abstração, herança e mixins para logging em Python
from pathlib import Path

# Define o caminho do arquivo de log
LOG_FILE = Path(__file__).parent / 'log.txt'


# Classe base abstrata para logging
class Log:
    def _log(self, msg):
        # Método abstrato: deve ser implementado nas subclasses/mixins
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        # Loga uma mensagem de erro
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        # Loga uma mensagem de sucesso
        return self._log(f'Success: {msg}')


# Mixin para logar mensagens em arquivo
class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)  # Exibe a mensagem no terminal
        msg_fomatada = f'{msg} ({self.__class__.__name__})'
        print('Salvando no log:', msg_fomatada)
        # Salva a mensagem formatada no arquivo de log
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_fomatada)
            arquivo.write('\n')


# Mixin para logar mensagens apenas no terminal
class LogPrintMixin(Log):
    def _log(self, msg):
        # Exibe a mensagem formatada no terminal
        print(f'{msg} ({self.__class__.__name__})')


# Testes dos mixins e métodos de log
if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_error('qualquer coisa')
    l.log_success('Que legal')
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_success('Que legal')
    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_success('Que legal')