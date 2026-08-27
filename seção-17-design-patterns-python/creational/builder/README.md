# Padrão de Projeto Builder

O padrão de projeto **Builder** é um padrão de criação que visa separar a construção de um objeto complexo da sua representação. Isso permite que o mesmo processo de construção possa criar diferentes representações do objeto.

## Arquivos

-   `builder-1.py`: Contém o código de exemplo do padrão Builder.
-   `builder.graphml`: Arquivo que pode ser usado para visualizar um diagrama do padrão.
-   `builder.png`: Imagem do diagrama do padrão.

## Explicação do Código

O arquivo `builder-1.py` implementa o padrão Builder para criar um objeto `User`.

### `StringReprMixin`

Esta classe é um mixin que fornece uma representação em string para as classes que a herdam.

### `User`

Esta classe representa o objeto complexo que queremos criar. Ela possui atributos como `firstname`, `lastname`, `age`, `phone_numbers` e `addresses`.

### `IUserBuilder` (Interface)

Esta é uma classe abstrata que define a interface para o `Builder`. Ela declara os métodos que o `Builder` deve implementar.

### `UserBuilder` (Builder Concreto)

Esta classe implementa a interface `IUserBuilder` e é responsável por construir o objeto `User` passo a passo. Cada método de adição (`add_firstname`, `add_lastname`, etc.) retorna a própria instância do `Builder`, permitindo o encadeamento de métodos (method chaining).

O método `result` retorna o objeto `User` construído e reinicia o `Builder` para que ele possa ser reutilizado.

### `UserDirector` (Diretor)

Esta classe é opcional e é responsável por orquestrar a construção do objeto `User` usando o `Builder`. Ela define métodos que constroem o objeto `User` com configurações específicas.

## Como Executar

O trecho `if __name__ == "__main__":` demonstra como usar o `UserBuilder` e o `UserDirector` para criar instâncias de `User`.

```python
if __name__ == "__main__":
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age('Jean', 'Lucas', 30)
    user2 = user_director.with_address('Maria', 'Bortolon', 'Av Brasil')
    print(user1)
    print(user2)
```

Neste exemplo, o `UserDirector` é usado para criar dois objetos `User` com diferentes configurações. O `user1` é criado com idade, enquanto o `user2` é criado com um endereço.
