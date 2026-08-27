"""
Flyweight é um padrão de projeto estrutural
que tem a intenção de usar compartilhamento
para suportar eficientemente grandes quantidades
de objetos de forma granular.

Só use o Flyweight quanto TODAS as condições
a seguir forem verdadeiras:

- uma aplicação utiliza uma grande quantidade de
objetos;
- os custos de armazenamento são altos por causa
da grande quantidade de objetos;
- a maioria dos estados de objetos podem se tornar
extrínsecos;
- muitos objetos podem ser substituídos por poucos
objetos compartilhados;
- a aplicação não depende da identidade dos objetos.

Importante:
- Estado intrínseco é o estado do objeto que não muda,
esse estado deve estar dentro do objeto flyweight;
- Estado extrínseco é o estado do objeto que muda,
esse estado pode ser movido para fora do objeto
flyweight;

Dicionário:
Intrínseco - que faz parte de ou que constitui a
essência, a natureza de algo; que é próprio de
algo; inerente.
Extrínseco - que não pertence à essência de algo;
que é exterior.
"""
from __future__ import annotations
from typing import List, Dict


class Client:
    """
    Client (Contexto):
    Contém o estado extrínseco que varia entre os diferentes usos do Flyweight.
    Neste exemplo, o 'Client' armazena o nome, número e detalhes do endereço,
    que são informações específicas de cada cliente e não do endereço em si.
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

        # address_number e address_details são estados extrínsecos,
        # ou seja, variam de um cliente para outro, mesmo que o endereço (flyweight)
        # seja o mesmo. Eles são passados para o flyweight no momento do uso.
        self.address_number: str
        self.address_details: str

    def add_address(self, address: Address) -> None:
        """Adiciona um objeto Flyweight (Address) à lista de endereços do cliente."""
        self._addresses.append(address)

    def list_addresses(self) -> None:
        """
        Lista os endereços do cliente, passando os estados extrínsecos
        (número e detalhes) para o método `show_address` do Flyweight.
        """
        print(f'Endereços de {self.name}:')
        for address in self._addresses:
            address.show_address(self.address_number, self.address_details)
        print()


class Address:
    """
    Flyweight (Endereço):
    Contém o estado intrínseco, que é a parte compartilhável do objeto.
    Neste caso, rua, bairro e CEP são intrínsecos, pois são propriedades
    fixas do endereço, independentemente de quem o usa.
    """

    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_details: str) -> None:
        """
        Exibe o endereço completo, combinando o estado intrínseco
        (rua, bairro, CEP) com o estado extrínseco (número, detalhes)
        passado pelo cliente no momento da chamada.
        """
        print(
            self._street, address_number, self._neighbourhood, address_details,
            self._zip_code
        )


class AddressFactory:
    """
    Flyweight Factory (Fábrica de Endereços):
    Responsável por gerenciar e compartilhar os objetos Flyweight.
    Ele garante que, se um objeto Flyweight com o mesmo estado intrínseco
    já existir, ele será reutilizado em vez de criar um novo.
    """
    _addresses: Dict[str, Address] = {}  # Cache para armazenar os flyweights existentes

    def _get_key(self, **kwargs) -> str:
        """Gera uma chave única para o cache baseada nos atributos intrínsecos."""
        # A ordem dos kwargs pode importar para a chave, garantir consistência.
        # Poderíamos também ordenar as chaves ou usar um hash mais robusto.
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        """
        Retorna um objeto Address (Flyweight) existente ou cria um novo.
        A lógica de criação/reutilização baseia-se na chave gerada
        a partir dos atributos intrínsecos.
        """
        key = self._get_key(**kwargs)

        try:
            # Tenta recuperar o flyweight do cache
            address_flyweight = self._addresses[key]
            print(f'Usando objeto de endereço já criado para a chave: {key}')
        except KeyError:
            # Se não existir no cache, cria um novo flyweight e o armazena
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print(f'Criando novo objeto de endereço para a chave: {key}')

        return address_flyweight


if __name__ == "__main__":
    # Instancia a fábrica de endereços
    address_factory = AddressFactory()

    # Solicita dois objetos de endereço à fábrica.
    # Como os atributos intrínsecos são os mesmos, a fábrica deve retornar o mesmo objeto.
    a1 = address_factory.get_address(
        street='Av Brasil',
        neighbourhood='Centro',
        zip_code='000000-000'
    )

    # Note o espaço extra em 'Av Brasil ' para demonstrar que pequenas diferenças
    # nos atributos intrínsecos criam um novo flyweight.
    a2 = address_factory.get_address(
        street='Av Brasil ', # Com um espaço extra, será um novo objeto
        neighbourhood='Centro',
        zip_code='000000-000'
    )

    # Cria um cliente e associa o endereço 'a1' a ele.
    # Define o estado extrínseco específico para Luiz.
    luiz = Client('Luiz')
    luiz.address_number = '50'
    luiz.address_details = 'Casa'
    luiz.add_address(a1)
    luiz.list_addresses()

    # Cria outro cliente e associa o endereço 'a2' a ele.
    # Define o estado extrínseco específico para Joana.
    joana = Client('Joana')
    joana.address_number = '250A'
    joana.address_details = 'AP 555'
    joana.add_address(a2)
    joana.list_addresses()

    # Verifica se 'a1' e 'a2' são o mesmo objeto na memória.
    # Devido à diferença na string 'Av Brasil' (com e sem espaço), eles serão objetos diferentes.
    # Se fossem idênticos, o resultado seria True, demonstrando o compartilhamento.
    print(f'a1 é o mesmo objeto que a2? {a1 == a2}')

    # Exemplo de como seria se os atributos intrínsecos fossem idênticos:
    print("\n--- Testando com atributos intrínsecos idênticos ---")
    a3 = address_factory.get_address(
        street='Av Principal',
        neighbourhood='Bairro Novo',
        zip_code='11111-111'
    )
    a4 = address_factory.get_address(
        street='Av Principal',
        neighbourhood='Bairro Novo',
        zip_code='11111-111'
    )
    print(f'a3 é o mesmo objeto que a4? {a3 == a4}') # Deve ser True, pois o mesmo flyweight é reutilizado

