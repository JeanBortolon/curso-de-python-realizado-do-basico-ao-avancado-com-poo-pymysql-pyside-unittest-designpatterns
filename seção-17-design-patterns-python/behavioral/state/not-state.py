"""
Este módulo demonstra um código que *não* utiliza o padrão de projeto State.
Ele serve como um exemplo do problema que o padrão State se propõe a resolver:
a complexidade de gerenciar transições de estado através de grandes estruturas
condicionais (if/elif/else) dentro de uma única classe.

No padrão State, cada estado é encapsulado em uma classe separada, e a lógica
de transição de um estado para outro é delegada a essas classes de estado,
tornando o código mais organizado, flexível e fácil de manter.
"""

from __future__ import annotations
from enum import Enum, auto


class Payment(Enum):
    """
    Define um enumerador (Enum) para representar os possíveis estados
    do pagamento de um pedido.

    - Pending: O pagamento está aguardando processamento.
    - Approved: O pagamento foi aprovado.
    - Rejected: O pagamento foi recusado.

    Utiliza `auto()` para atribuir automaticamente valores únicos aos membros.
    """
    Pending = auto()
    Approved = auto()
    Rejected = auto()

    def __str__(self) -> str:
        """
        Retorna uma representação em string do estado do pagamento.
        Exemplo: "PaymentPending", "PaymentApproved", "PaymentRejected".
        """
        return f'{self.__class__.__name__}{self.name}'


class Order:
    """
    Representa um Pedido, que possui um estado de pagamento.
    Esta classe *não* utiliza o padrão State e, portanto, gerencia
    as transições de estado internamente com uma lógica condicional.
    """

    def __init__(self) -> None:
        """
        Inicializa um novo Pedido com o estado de pagamento `Pending` (Pendente).
        """
        self.state: Payment = Payment.Pending

    def change_state(self, state: Payment) -> None:
        """
        Método responsável por alterar o estado do pagamento do pedido.

        PROBLEMA: Esta função exemplifica o "problema" que o padrão State resolve.
        Ela contém uma grande e complexa estrutura condicional (if/elif)
        que precisa saber sobre todos os estados possíveis e todas as transições
        válidas (ou inválidas) entre eles.

        À medida que o número de estados ou as regras de transição aumentam,
        esta função se torna cada vez mais difícil de ler, entender, manter
        e estender. Qualquer nova regra de negócio ou estado exige modificação
        direta nesta função, aumentando o risco de bugs.
        """

        # Lógica para transições a partir do estado PENDENTE
        if self.state == Payment.Pending and state == Payment.Pending:
            print('ERRO: Pagamento já pendente. Não é possível mover para pendente novamente.')
        elif self.state == Payment.Pending and state == Payment.Approved:
            self.state = Payment.Approved
            print('SUCESSO: Pagamento aprovado.')
        elif self.state == Payment.Pending and state == Payment.Rejected:
            self.state = Payment.Rejected
            print('SUCESSO: Pagamento recusado.')

        # Lógica para transições a partir do estado APROVADO
        elif self.state == Payment.Approved and state == Payment.Approved:
            print('ERRO: Pagamento já aprovado. Não é possível aprovar novamente.')
        elif self.state == Payment.Approved and state == Payment.Rejected:
            self.state = Payment.Rejected
            print('SUCESSO: Pagamento recusado.')
        elif self.state == Payment.Approved and state == Payment.Pending:
            # Esta transição pode ser considerada inválida em alguns contextos reais.
            # Aqui, é permitida para demonstrar a complexidade do controle manual.
            self.state = Payment.Pending
            print('ALERTA: Pagamento movido para pendente a partir de aprovado.')

        # Lógica para transições a partir do estado RECUSADO
        elif self.state == Payment.Rejected and state == Payment.Approved:
            print('ERRO: Pagamento recusado. Não é possível aprovar diretamente de um estado recusado.')
        elif self.state == Payment.Rejected and state == Payment.Rejected:
            print('ERRO: Pagamento já recusado. Não é possível recusar novamente.')
        elif self.state == Payment.Rejected and state == Payment.Pending:
            print('ERRO: Pagamento recusado. Não é possível mover para pendente a partir de um estado recusado.')
            # Em um sistema real, um pagamento recusado geralmente não pode voltar para pendente
            # sem um novo processo de pagamento. Isso ilustra as regras de negócio complexas.

        print(f'Estado atual do Pedido: {self.state}')
        print()

    def pending(self) -> None:
        """
        Tenta mudar o estado do pedido para Pendente.
        """
        print('Tentando mudar estado para PENDING via método pending()')
        self.change_state(Payment.Pending)

    def approve(self) -> None:
        """
        Tenta mudar o estado do pedido para Aprovado.
        """
        print('Tentando mudar estado para APPROVED via método approve()')
        self.change_state(Payment.Approved)

    def reject(self) -> None:
        """
        Tenta mudar o estado do pedido para Recusado.
        """
        print('Tentando mudar estado para REJECTED via método reject()')
        self.change_state(Payment.Rejected)


if __name__ == "__main__":
    # Cria uma instância do Pedido
    o1 = Order()
    print(f'Pedido inicializado. Estado: {o1.state}\n')

    # Demonstração das transições de estado
    o1.approve()  # Tenta aprovar
    o1.approve()  # Tenta aprovar novamente (deve mostrar erro/aviso)
    o1.reject()   # Tenta recusar
    o1.approve()  # Tenta aprovar de um estado recusado (deve mostrar erro)
    o1.pending()  # Tenta mover para pendente de um estado recusado (deve mostrar erro)

    # Exemplo de uma transição que pode ser permitida dependendo da regra de negócio
    # mas que o padrão State ajudaria a gerenciar de forma mais elegante.
    print("-" * 30)
    o2 = Order()
    o2.approve()
    o2.pending() # Se a regra permitir, volta para pendente
    o2.reject()
    o2.pending() # Não deve permitir, conforme a lógica implementada

