"""
O Proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.
O proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como o proxies são usados,
nós os classificamos como:

- Proxy Virtual: controla acesso a recursos que podem
ser caros para criação ou utilização. Ele adia a criação
e inicialização de um objeto pesado até que ele seja
realmente necessário.
- Proxy Remoto: controla acesso a recursos que estão
em servidores remotos. Ele representa um objeto que
reside em um espaço de endereço diferente (máquina remota).
- Proxy de proteção: controla acesso a recursos que
possam necessitar autenticação ou permissão. Ele verifica
se o chamador tem os direitos de acesso necessários
para executar a solicitação.
- Proxy inteligente: além de controlar acesso ao
objeto real, também executa tarefas adicionais para
saber quando e como executar determinadas ações. Ele
adiciona lógica extra antes ou depois de encaminhar
a solicitação para o objeto real, como logging ou caching.

Proxies podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict


class IUser(ABC):
    """
    Subject Interface (Interface do Assunto)

    Define a interface comum para o RealSubject e o Proxy.
    Isso permite que o Proxy seja usado em qualquer lugar
    onde um RealSubject é esperado.
    """

    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]:
        """
        Método abstrato para obter a lista de endereços do usuário.
        """
        pass

    @abstractmethod
    def get_all_user_data(self) -> Dict:
        """
        Método abstrato para obter todos os dados do usuário.
        """
        pass


class RealUser(IUser):
    """
    Real Subject (Assunto Real)

    Esta classe contém a lógica de negócios principal.
    Ela simula operações que podem ser lentas ou consumir muitos recursos,
    como requisições a um banco de dados ou a uma API externa.
    """

    def __init__(self, firstname: str, lastname: str) -> None:
        # Simula um atraso na criação do objeto, como carregar dados pesados.
        sleep(2)
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        """
        Simula a busca de endereços do usuário, que é uma operação lenta.
        """
        sleep(2)  # Simulando requisição
        return [
            {'rua': 'Av. Brasil', 'numero': 500}
        ]

    def get_all_user_data(self) -> Dict:
        """
        Simula a busca de todos os dados do usuário, que é uma operação lenta.
        """
        sleep(2)  # Simulando requisição
        return {
            'cpf': '111.111.111-11',
            'rg': 'AB111222444'
        }


class UserProxy(IUser):
    """
    Proxy (Substituto)

    Esta classe atua como um substituto para o RealUser.
    Ela controla o acesso ao RealUser e pode adicionar funcionalidades
    extras, como lazy initialization (inicialização preguiçosa) e caching.
    """

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname

        # Esses atributos são inicializados apenas quando o RealUser
        # é realmente necessário (lazy initialization).
        # _real_user: Referência ao objeto RealUser.
        # _cached_addresses: Cache para os endereços do usuário.
        # _all_user_data: Cache para todos os dados do usuário.
        self._real_user: RealUser = None  # Inicializa como None
        self._cached_addresses: List[Dict] = None  # Inicializa como None
        self._all_user_data: Dict = None  # Inicializa como None

    def get_real_user(self) -> None:
        """
        Cria uma instância do RealUser somente se ela ainda não existir.
        Isso demonstra o conceito de Proxy Virtual (lazy initialization).
        """
        if self._real_user is None:  # Verifica se o RealUser já foi criado
            print('Criando RealUser...')
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_addresses(self) -> List[Dict]:
        """
        Retorna os endereços do usuário. Primeiro, verifica se o RealUser
        já foi criado. Em seguida, verifica se os endereços já estão em cache.
        Se não estiverem, busca do RealUser e armazena em cache.
        Isso demonstra o conceito de Proxy Inteligente (caching).
        """
        self.get_real_user()  # Garante que o RealUser seja criado

        if self._cached_addresses is None:  # Verifica se os dados estão em cache
            print('Buscando endereços do RealUser...')
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self) -> Dict:
        """
        Retorna todos os dados do usuário. Primeiro, verifica se o RealUser
        já foi criado. Em seguida, verifica se os dados já estão em cache.
        Se não estiverem, busca do RealUser e armazena em cache.
        Isso demonstra o conceito de Proxy Inteligente (caching).
        """
        self.get_real_user()  # Garante que o RealUser seja criado

        if self._all_user_data is None:  # Verifica se os dados estão em cache
            print('Buscando todos os dados do RealUser...')
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


if __name__ == "__main__":
    print('Client code starting...')
    # Instanciando o Proxy. O RealUser ainda não foi criado.
    luiz = UserProxy('Luiz', 'Otávio')

    # Acesso a atributos diretos do Proxy. Estes não disparam a criação do RealUser.
    print(f'Nome: {luiz.firstname}')
    print(f'Sobrenome: {luiz.lastname}')

    print('\nPrimeira chamada para get_all_user_data():')
    # Esta é a primeira vez que precisamos de dados do RealUser.
    # O Proxy vai criar o RealUser e buscar os dados. Haverá um atraso.
    print(luiz.get_all_user_data())

    print('\nPrimeira chamada para get_addresses():')
    # O RealUser já foi criado pela chamada anterior, mas os endereços não estão em cache.
    # O Proxy vai buscar os endereços do RealUser. Haverá um atraso.
    print(luiz.get_addresses())

    print('\nChamadas subsequentes (dados em cache):')
    # Estas chamadas devem ser instantâneas, pois os dados já foram
    # buscados e estão armazenados em cache dentro do Proxy.
    print('CACHED DATA:')
    for i in range(3):  # Testando múltiplas chamadas para ver o cache em ação
        print(luiz.get_addresses())
        print(luiz.get_all_user_data())
        # O RealUser é criado apenas uma vez, e os dados são buscados
        # apenas uma vez por tipo (endereços, todos os dados) devido ao cache.
    print('\nClient code finished.')
