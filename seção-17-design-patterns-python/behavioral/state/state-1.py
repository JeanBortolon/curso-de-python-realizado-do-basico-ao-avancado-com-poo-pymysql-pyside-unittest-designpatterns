"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.

Este exemplo demonstra como o padrão State pode ser usado para gerenciar
os diferentes estados de um pedido (Order), como "Pagamento Pendente",
"Pagamento Aprovado" e "Pagamento Rejeitado".
"""
from __future__ import annotations  # Permite usar anotações de tipo com classes não totalmente definidas (forward references)
from abc import ABC, abstractmethod  # Importa classes para criar interfaces abstratas e métodos abstratos


class Order:
    """
    Context: A classe Context mantém uma instância de uma subclasse State concreta,
    que representa o estado atual do Context. O Context delega chamadas de comportamento
    sensíveis ao estado para o objeto State atual.
    """

    def __init__(self) -> None:
        # O estado inicial de um pedido é PaymentPending (Pagamento Pendente).
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        """
        Tenta mover o pedido para o estado de "pendente".
        O comportamento real depende do estado atual.
        """
        print('Tentando executar pending()')
        self.state.pending()  # Delega a ação para o objeto de estado atual
        print('Estado atual: ', self.state)
        print()

    def approve(self) -> None:
        """
        Tenta aprovar o pedido.
        O comportamento real depende do estado atual.
        """
        print('Tentando executar approve()')
        self.state.approve()  # Delega a ação para o objeto de estado atual
        print('Estado atual: ', self.state)
        print()

    def reject(self) -> None:
        """
        Tenta rejeitar o pedido.
        O comportamento real depende do estado atual.
        """
        print('Tentando executar reject()')
        self.state.reject()  # Delega a ação para o objeto de estado atual
        print('Estado atual: ', self.state)
        print()


class OrderState(ABC):
    """
    State (Estado): A interface State declara métodos específicos do estado.
    Estes métodos devem fazer sentido para todos os estados concretos,
    embora alguns possam não fazer nada ou lançar exceções se o Context
    chamar o método errado.
    """

    def __init__(self, order: Order) -> None:
        # Cada estado concreto recebe uma referência ao objeto Context (Order)
        # para que possa fazer a transição do Context para outro estado.
        self.order = order

    @abstractmethod
    def pending(self) -> None:
        """ Método abstrato para lidar com a transição para estado pendente. """
        pass

    @abstractmethod
    def approve(self) -> None:
        """ Método abstrato para lidar com a transição para estado aprovado. """
        pass

    @abstractmethod
    def reject(self) -> None:
        """ Método abstrato para lidar com a transição para estado rejeitado. """
        pass

    def __str__(self):
        """ Retorna o nome da classe do estado atual para representação em string. """
        return self.__class__.__name__


class PaymentPending(OrderState):
    """ Concrete State (Estado Concreto): Implementa o comportamento específico do estado. """

    def pending(self) -> None:
        """ Se já está pendente, não há nada a fazer. """
        print('Pagamento já pendente, não posso fazer nada.')

    def approve(self) -> None:
        """ Transita o estado do pedido para PaymentApproved. """
        self.order.state = PaymentApproved(self.order)
        print('Pagamento aprovado')

    def reject(self) -> None:
        """ Transita o estado do pedido para PaymentRejected. """
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado')


class PaymentApproved(OrderState):
    """ Concrete State (Estado Concreto): Implementa o comportamento específico do estado. """

    def pending(self) -> None:
        """ Transita o estado do pedido para PaymentPending. """
        self.order.state = PaymentPending(self.order)
        print('Pagamento pendente')

    def approve(self) -> None:
        """ Se já está aprovado, não há nada a fazer. """
        print('Pagamento já aprovado, não posso fazer nada.')

    def reject(self) -> None:
        """ Transita o estado do pedido para PaymentRejected. """
        self.order.state = PaymentRejected(self.order)
        print('Pagamento recusado')


class PaymentRejected(OrderState):
    """ Concrete State (Estado Concreto): Implementa o comportamento específico do estado. """

    def pending(self) -> None:
        """ Se o pagamento foi recusado, não pode voltar para pendente diretamente. """
        print('Pagamento recusado. Não vou mover para pendente.')

    def approve(self) -> None:
        """ Se o pagamento foi recusado, não pode ser aprovado diretamente. """
        print('Pagamento recusado. Não vou aprovar.')

    def reject(self) -> None:
        """ Se já foi recusado, não há nada a fazer. """
        print('Pagamento recusado. Não vou recusar novamente.')


if __name__ == "__main__":
    # Exemplo de uso
    order = Order()  # Cria um novo pedido, que começa no estado PaymentPending
    order.pending()  # Chama pending() no estado atual (PaymentPending)
    order.approve()  # Chama approve(), transita para PaymentApproved
    order.pending()  # Chama pending(), transita para PaymentPending
    order.reject()   # Chama reject(), transita para PaymentRejected
    order.pending()  # Chama pending() no estado PaymentRejected (comportamento diferente)
    order.approve()  # Chama approve() no estado PaymentRejected (comportamento diferente)
