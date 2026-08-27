"""
Template Method (comportamental) tem a intenção de definir
um algoritmo em um método, postergando alguns passos
para as subclasses por herança. Template method permite
que subclasses redefinam certos passos de um algoritmo
sem mudar a estrutura do mesmo.

Também é possível definir hooks para que as subclasses
utilizem caso necessário.

The Hollywood principle: "Don't Call Us, We'll Call You."
(IoC - Inversão de controle)
"""
from abc import ABC, abstractmethod


class Abstract(ABC):
    # O template_method define o esqueleto do algoritmo.
    # Ele contém uma série de chamadas para operações, algumas definidas na classe base
    # (como base_class_method), algumas como hooks (que subclasses podem opcionalmente
    # sobrescrever) e outras que são operações abstratas (que subclasses DEVEM implementar).
    def template_method(self) -> None:
        self.hook()  # Hook: Subclasses podem sobrescrever (opcional)
        self.operation1()  # Operação abstrata: Subclasses DEVEM implementar
        self.base_class_method()  # Método concreto: Definido na classe base, comum a todas as subclasses
        self.operation2()  # Operação abstrata: Subclasses DEVEM implementar

    # O 'hook' é um método opcional que subclasses podem sobrescrever para
    # injetar comportamento adicional no algoritmo sem alterar a estrutura.
    # Por padrão, ele não faz nada.
    def hook(self) -> None: pass

    # Este é um método concreto implementado na classe abstrata.
    # Ele será executado por todas as subclasses sem a necessidade de redefinição.
    def base_class_method(self) -> None:
        print('OLÁ EU SOU DA CLASSE ABSTRATA E SEREI EXECUTADO TAMBÉM')

    # operation1 é um método abstrato que deve ser implementado por todas as subclasses.
    # Ele representa um passo variável do algoritmo.
    @abstractmethod
    def operation1(self) -> None: pass

    # operation2 é outro método abstrato, também exigindo implementação pelas subclasses.
    # Representa outro passo variável do algoritmo.
    @abstractmethod
    def operation2(self) -> None: pass


class ConcreteClass1(Abstract):
    # ConcreteClass1 fornece implementações específicas para as operações abstratas
    # e decide sobrescrever o método hook para adicionar um comportamento customizado.
    def hook(self) -> None:
        print('Olha eu vou utilizar o hook')

    def operation1(self) -> None:
        print('Operaçao 1 concluída')

    def operation2(self) -> None:
        print('Operaçao 2 concluída')


class ConcreteClass2(Abstract):
    # ConcreteClass2 também fornece implementações específicas para as operações abstratas,
    # mas opta por não sobrescrever o método hook, usando a implementação padrão (vazia) da classe abstrata.
    def operation1(self) -> None:
        print('Operaçao 1 concluída (de maneira diferente)')

    def operation2(self) -> None:
        print('Operaçao 2 concluída  (de maneira diferente)')


if __name__ == "__main__":
    print('Executando ConcreteClass1:')
    # Instancia a primeira subclasse concreta
    c1 = ConcreteClass1()
    # Chama o template_method, que executa o algoritmo definido na classe abstrata,
    # utilizando as implementações específicas de ConcreteClass1.
    c1.template_method()

    print('\nExecutando ConcreteClass2:')
    # Instancia a segunda subclasse concreta
    c2 = ConcreteClass2()
    # Chama o template_method, que executa o mesmo algoritmo,
    # mas com as implementações específicas de ConcreteClass2.
    c2.template_method()
