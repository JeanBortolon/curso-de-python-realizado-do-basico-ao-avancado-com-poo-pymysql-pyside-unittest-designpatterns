# Padrão de Projeto Flyweight

O padrão de projeto **Flyweight** (peso-leve) é um padrão estrutural que visa otimizar o uso de memória ao permitir o compartilhamento eficiente de um grande número de objetos. Ele é ideal quando uma aplicação precisa criar muitos objetos que possuem grande parte de seu estado idêntico.

## Quando Usar o Padrão Flyweight?

Utilize o Flyweight quando todas as condições a seguir forem verdadeiras:

1.  A aplicação utiliza uma **grande quantidade de objetos**.
2.  Os custos de armazenamento são altos devido a essa grande quantidade de objetos.
3.  A maioria dos estados dos objetos pode ser tornada **extrínseca** (contextual).
4.  Muitos objetos podem ser substituídos por um número menor de objetos **compartilhados**.
5.  A aplicação não depende da identidade única de cada objeto (ou seja, `objeto1 is objeto2` pode ser `True` se eles representam o mesmo Flyweight).

## Conceitos Chave

No padrão Flyweight, o estado de um objeto é dividido em duas partes:

*   **Estado Intrínseco (Intrinsic State):** É a parte do estado do objeto que é **constante e compartilhável** entre múltiplos objetos. Ele é armazenado dentro do objeto Flyweight e não muda.
    *   *Exemplo:* No contexto de endereços, a rua, o bairro e o CEP são partes intrínsecas, pois definem o endereço em si e são os mesmos para qualquer pessoa que resida nele.
*   **Estado Extrínseco (Extrinsic State):** É a parte do estado do objeto que **varia de acordo com o contexto** em que o Flyweight é usado. Ele não é armazenado no Flyweight, mas é passado como parâmetro para os métodos do Flyweight no momento da sua utilização.
    *   *Exemplo:* O número da casa e um complemento (como "Casa", "Apartamento 555") são extrínsecos, pois são específicos de uma ocupação daquele endereço e variam de um cliente para outro, mesmo que compartilhem o mesmo endereço base.

## Estrutura no Código (`flyweight.py`)

No exemplo fornecido em `flyweight.py`, a implementação do padrão Flyweight é composta por:

1.  **`Address` (Flyweight):**
    *   Representa o objeto Flyweight.
    *   Armazena o **estado intrínseco**: `_street` (rua), `_neighbourhood` (bairro) e `_zip_code` (CEP).
    *   Possui o método `show_address(address_number, address_details)` que recebe o **estado extrínseco** (`address_number`, `address_details`) como parâmetro para exibir o endereço completo.

2.  **`Client` (Contexto):**
    *   Representa o cliente que usa os objetos Flyweight.
    *   Armazena o **estado extrínseco**: `name` (nome do cliente), `address_number` (número) e `address_details` (detalhes adicionais).
    *   Possui o método `add_address` para associar um objeto `Address` (Flyweight) e `list_addresses` para exibir os endereços, passando os estados extrínsecos para o Flyweight.

3.  **`AddressFactory` (Flyweight Factory):**
    *   Responsável por criar e gerenciar os objetos `Address` (Flyweight).
    *   Mantém um **cache** (`_addresses`) de Flyweights já criados.
    *   O método `get_address(**kwargs)` verifica se um Flyweight com os mesmos atributos intrínsecos (rua, bairro, CEP) já existe no cache. Se existir, ele retorna a instância existente (compartilhamento); caso contrário, cria uma nova instância, a armazena no cache e a retorna. Isso garante que Flyweights idênticos sejam reutilizados.

## Exemplo de Uso

No bloco `if __name__ == "__main__":`, o `AddressFactory` é utilizado para obter instâncias de `Address`. Se os parâmetros intrínsecos forem os mesmos, a fábrica retorna o mesmo objeto `Address`. Clientes diferentes (`Luiz` e `Joana`) podem então usar o mesmo objeto `Address` Flyweight, fornecendo seus próprios detalhes extrínsecos (número e complemento) para contextualizar o endereço. Isso demonstra como múltiplos clientes podem compartilhar o mesmo objeto de endereço sem que cada um precise armazenar uma cópia completa.

## Arquivos Nesta Pasta

*   **`flyweight.py`**: A implementação em Python do padrão Flyweight, conforme descrito acima. Contém as classes `Client`, `Address` e `AddressFactory`, além de um exemplo de uso.
*   **`flyweight.graphml`**: Um arquivo GraphML, provavelmente um diagrama de fluxo ou de classes criado com uma ferramenta como yEd Graph Editor, que visualiza a estrutura do padrão Flyweight.
*   **`flyweight.png`**: Uma imagem PNG, provavelmente uma representação visual do diagrama contido em `flyweight.graphml`, oferecendo uma compreensão rápida da arquitetura.
