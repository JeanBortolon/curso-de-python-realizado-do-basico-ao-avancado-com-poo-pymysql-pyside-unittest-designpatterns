# (Parte 3) Threads - Executando processamentos em paralelo

# Importa Lock e Thread para controle de concorrência e execução paralela
from threading import Lock, Thread
from time import sleep

"""
# Exemplo de herança de Thread para criar threads personalizadas
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)

# Criação e início de múltiplas threads
# Cada thread imprime um texto após um tempo diferente
# t1 = MeuThread('Thread 1', 5)
# t1.start()
# t2 = MeuThread('Thread 2', 3)
# t2.start()
# t3 = MeuThread('Thread 3', 2)
# t3.start()
# for i in range(20):
#     print(i)
#     sleep(1)
"""

"""
# Exemplo de uso de Thread com função como alvo
# Função que simula uma tarefa demorada
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

# Criação de threads para executar a função com diferentes argumentos
# t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
# t1.start()
# t2 = Thread(target=vai_demorar, args=('Olá mundo 2!', 1))
# t2.start()
# t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 2))
# t3.start()
# for i in range(20):
#     print(i)
#     sleep(.5)
"""

"""
# Exemplo de uso de join para aguardar o término da thread
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

# t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 10))
# t1.start()
# t1.join()  # Aguarda a thread terminar
# print('Thread acabou!')
"""

# Classe que simula a venda de ingressos com controle de concorrência
class Ingressos:
    """
    Classe que vende ingressos
    """

    def __init__(self, estoque: int):
        """ Inicializando...
        :param estoque: quantidade de ingressos em estoque
        """
        self.estoque = estoque
        # Cria um Lock para evitar condições de corrida
        self.lock = Lock()

    def comprar(self, quantidade: int):
        """
        Compra determinada quantidade de ingressos
        :param quantidade: A quantidade de ingressos que deseja comprar
        :type quantidade: int
        :return: Nada
        :rtype: None
        """
        # Tranca o método para evitar que múltiplas threads alterem o estoque ao mesmo tempo
        self.lock.acquire()

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            # Libera o Lock antes de retornar
            self.lock.release()
            return

        sleep(1)  # Simula o tempo de processamento da compra

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s). '
              f'Ainda temos {self.estoque} em estoque.')

        # Libera o Lock após a operação
        self.lock.release()

# Bloco principal de execução
if __name__ == '__main__':
    ingressos = Ingressos(10)  # Cria o estoque inicial de ingressos

    # Cria e inicia várias threads para simular várias compras concorrentes
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print(ingressos.estoque)  # Mostra o estoque final (pode não ser zero devido à concorrência)