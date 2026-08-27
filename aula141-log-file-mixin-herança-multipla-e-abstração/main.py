# Importa os mixins de log e a classe Smartphone
from log import LogFileMixin, LogPrintMixin
from eletronico import Smartphone

# Cria instâncias de Smartphone
galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('iPhone')

# Liga o Galaxy S (irá logar sucesso)
galaxy_s.ligar()
# Desliga o iPhone (irá logar erro, pois já está desligado)
iphone.desligar()