# Padrão de Projeto Estrutural: Proxy

Este diretório contém um exemplo do padrão de projeto **Proxy**. O objetivo desse padrão é fornecer um objeto substituto (o *proxy*) que atua como se fosse o objeto real que o cliente gostaria de usar. O proxy intercepta as solicitações e tem controle sobre como e quando repassá-las ao objeto real.

## O que foi estudado?

O padrão Proxy permite controlar o acesso a um objeto, adicionando uma camada de indireção. Isso é útil para várias finalidades, como:

- **Proxy Virtual:** Adiar a criação de objetos que consomem muitos recursos (objetos "pesados") até que sejam realmente necessários. Isso é conhecido como *lazy initialization*.
- **Proxy de Proteção:** Controlar o acesso a métodos ou dados sensíveis, verificando permissões ou autenticando o cliente antes de permitir a execução da solicitação.
- **Proxy Remoto:** Permitir a comunicação com um objeto que está em um local diferente, como em outro servidor na rede.
- **Proxy Inteligente:** Adicionar funcionalidades extras quando uma solicitação é feita, como logging, caching de resultados, ou travas de acesso concorrente.

O exemplo `proxy-1.py` demonstra a implementação de um **Proxy Virtual** e **Inteligente**.

## Arquivos no Diretório

- **`proxy-1.py`**:
  - Contém a implementação do padrão Proxy em Python.
  - **`IUser` (Interface):** Define a interface comum que tanto o objeto real (`RealUser`) quanto o proxy (`UserProxy`) devem seguir. Isso garante que o cliente possa usar o proxy da mesma forma que usaria o objeto real.
  - **`RealUser` (Objeto Real):** É a classe que contém a lógica de negócios principal. No exemplo, ela simula operações lentas (como acesso a um banco de dados) com `sleep()`. A criação de um `RealUser` também é simulada como uma operação cara.
  - **`UserProxy` (Proxy):** É a classe que o cliente utiliza diretamente. Ele:
    1. **Adia a criação do `RealUser`** até que um de seus métodos de dados (`get_addresses` ou `get_all_user_data`) seja chamado pela primeira vez (Proxy Virtual).
    2. **Armazena em cache (caching)** os resultados obtidos do `RealUser`. Em chamadas subsequentes, os dados são retornados do cache instantaneamente, evitando a repetição das operações lentas (Proxy Inteligente).
  - O código no `if __name__ == "__main__"` demonstra como o cliente interage com o `UserProxy` e como o proxy gerencia a criação e o cache dos dados do `RealUser`.

- **`proxy.png` e `proxy.graphml`**:
  - São arquivos gráficos que provavelmente representam o diagrama de classes ou a estrutura do padrão Proxy, ajudando a visualizar a relação entre o Cliente, a Interface, o Proxy e o Objeto Real. `proxy.png` é a imagem e `proxy.graphml` é o arquivo-fonte do diagrama, que pode ser aberto em editores de grafos como o yEd.

## Como o Código Funciona

1. O cliente instancia `UserProxy`, que é uma operação rápida, pois o `RealUser` (objeto pesado) não é criado neste momento.
2. Quando o cliente chama um método como `get_all_user_data()` pela primeira vez no proxy:
   - O `UserProxy` verifica que o `RealUser` ainda não existe e o instancia (operação lenta).
   - Em seguida, ele chama o método correspondente no `RealUser` para buscar os dados (outra operação lenta).
   - O resultado é armazenado em uma variável de cache dentro do `UserProxy`.
   - O resultado é retornado ao cliente.
3. Em qualquer chamada futura ao mesmo método, o `UserProxy` simplesmente retorna o dado que está em cache, sem precisar instanciar o `RealUser` novamente ou executar a operação lenta. A resposta é instantânea.

Este exemplo ilustra de forma clara como o Proxy pode otimizar o desempenho e o uso de recursos, além de adicionar uma camada de controle sobre o acesso a objetos.
