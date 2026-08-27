# Importa os módulos de contas e pessoas, que contêm as classes usadas no sistema bancário
import contas
import pessoas

# Classe principal que representa o Banco
class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
    ):
        # Inicializa listas de agências, clientes e contas
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    # Verifica se a agência da conta está cadastrada no banco
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('_checa_agencia', True)
            return True
        print('_checa_agencia', False)
        return False

    # Verifica se o cliente está cadastrado no banco
    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('_checa_cliente', True)
            return True
        print('_checa_cliente', False)
        return False

    # Verifica se a conta está cadastrada no banco
    def _checa_conta(self, conta):
        if conta in self.contas:
            print('_checa_conta', True)
            return True
        print('_checa_conta', False)
        return False

    # Verifica se a conta realmente pertence ao cliente informado
    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

    # Método principal de autenticação: só retorna True se todas as checagens passarem
    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
            self._checa_conta(conta) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    # Representação do banco para debug e exibição
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'

# Bloco de teste: cria clientes, contas, adiciona ao banco e realiza operações
if __name__ == '__main__':
    # Cria um cliente e uma conta corrente
    c1 = pessoas.Cliente('Luiz', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    # Cria outro cliente e uma conta poupança
    c2 = pessoas.Cliente('Maria', 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    # Cria o banco e adiciona clientes, contas e agências
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    # Autentica o cliente e realiza operações se tudo estiver correto
    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(100)
        print(c1.conta)