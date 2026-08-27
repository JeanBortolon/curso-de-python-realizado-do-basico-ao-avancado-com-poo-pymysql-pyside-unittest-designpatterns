# Padrões de Projeto - Criacionais - Singleton e Monostate

Esta pasta contém exemplos de implementação dos padrões de projeto **Singleton** e **Monostate (ou Borg)**, que são ambos padrões criacionais. Padrões criacionais tratam da criação de objetos de uma maneira que é apropriada para a situação, buscando otimizar o processo de instanciamento e controlar a forma como os objetos são criados.

## Padrão Singleton

**Definição:** O padrão Singleton garante que uma classe tenha apenas uma única instância em toda a aplicação e fornece um ponto de acesso global para essa instância. Isso é útil quando você precisa de um objeto que coordene ações em um sistema (por exemplo, um gerenciador de configurações, um pool de conexões de banco de dados ou um logger).

**Propósito:**
*   **Garantir uma única instância:** Impede que múltiplas instâncias da mesma classe sejam criadas.
*   **Ponto de acesso global:** Oferece uma maneira fácil e consistente de acessar essa instância em qualquer parte do código.

### Implementações nesta pasta:

#### `singleton-1.py` - Singleton com Sobrescrita de `__new__`

Este arquivo demonstra uma implementação clássica do Singleton em Python, onde o método especial `__new__` da classe é sobrescrito.

*   **Como funciona:** O `__new__` é o primeiro método a ser chamado quando você tenta criar uma instância de uma classe. Nele, verificamos se a instância já existe. Se não existir, criamos uma nova e a armazenamos em um atributo de classe (`_instance`). Se já existir, simplesmente retornamos a instância existente.
*   **Ponto de Atenção:** O método `__init__` (o construtor) é chamado *todas as vezes* que você tenta "instanciar" a classe, mesmo que `__new__` retorne uma instância já existente. Isso significa que você precisa ter cuidado para não redefinir o estado da sua instância Singleton a cada chamada, se esse não for o comportamento desejado.

#### `singleton-2.py` - Singleton com Metaclasse

Esta abordagem utiliza uma metaclasse para implementar o padrão Singleton. Metaclasses são classes que criam classes, oferecendo um controle mais profundo sobre o processo de criação de uma classe e suas instâncias.

*   **Como funciona:** A classe `Singleton` atua como uma metaclasse. Seu método `__call__` é invocado sempre que a classe `AppSettings` (que usa `Singleton` como metaclasse) é instanciada. Dentro de `__call__`, a metaclasse gerencia um dicionário de instâncias (`_instances`) e garante que, para cada classe, apenas uma instância seja criada e retornada.
*   **Vantagem:** Com a metaclasse, o `__init__` da sua classe (e.g., `AppSettings`) é chamado apenas uma única vez, na primeira vez que a instância é criada, o que simplifica o gerenciamento do estado inicial da instância.

#### `singleton-3.py` - Singleton com Decorador

Este arquivo apresenta o padrão Singleton implementado usando um decorador. Decoradores são funções que modificam o comportamento de outras funções ou classes.

*   **Como funciona:** A função `singleton` atua como um decorador. Ela recebe a classe a ser decorada e retorna uma função (`get_class`). Esta função interna gerencia um dicionário de instâncias. Na primeira vez que a classe decorada é "chamada", uma instância é criada e armazenada. Nas chamadas subsequentes, a função `get_class` simplesmente retorna a instância já existente.
*   **Vantagem:** É uma forma limpa e Pythonica de aplicar o padrão, sem modificar a estrutura interna da classe que será um Singleton.

## Padrão Monostate (ou Borg)

**Definição:** O padrão Monostate (também conhecido como Borg, em referência aos Borg de Star Trek, que compartilham uma mente coletiva) é uma variação do Singleton com uma intenção ligeiramente diferente. Em vez de garantir que haja apenas *uma* instância de uma classe, ele garante que *todas as instâncias* de uma classe compartilhem o *mesmo estado*. Isso significa que você pode ter múltiplas instâncias de um objeto Monostate, mas todas elas verão e modificarão os mesmos dados.

**Propósito:**
*   **Compartilhamento de estado:** Permite que diferentes objetos independentes manipulem um conjunto de dados comum.
*   **Abordagem semântica:** A ideia é que o comportamento deve ser o mesmo, mesmo que a identidade do objeto possa ser diferente.

### Implementações nesta pasta:

#### `monostate-1.py` - Monostate com Atribuição de `__dict__` em `__init__`

Este exemplo mostra uma forma direta de implementar o Monostate.

*   **Como funciona:** Dentro do método `__init__`, o atributo `__dict__` da instância (que normalmente contém os atributos próprios do objeto) é explicitamente sobrescrito para apontar para um dicionário de classe compartilhado (`_state`). Dessa forma, qualquer atribuição de atributo à instância (`self.nome = ...`) na verdade modifica o dicionário de estado compartilhado.
*   **Resultado:** Múltiplas instâncias parecerão ter seus próprios atributos, mas internamente todos estão acessando e modificando o mesmo dicionário de dados.

#### `monostate-2.py` - Monostate com Atribuição de `__dict__` em `__new__` e Herança

Este arquivo aprimora a implementação do Monostate, transferindo a lógica de compartilhamento de estado para o método `__new__`, que é executado antes de `__init__`.

*   **Como funciona:** Similar ao `monostate-1.py`, mas a atribuição de `__dict__` da instância para o dicionário `_state` da classe é feita dentro de `__new__`. Isso garante que o estado compartilhado seja configurado antes mesmo de `__init__` ser chamado.
*   **Benefício:** Essa abordagem é considerada um pouco mais robusta, pois garante que a instância já nasce com seu dicionário de atributos apontando para o estado compartilhado. O exemplo também inclui uma subclasse (`A`) para demonstrar que o comportamento Monostate é herdado, ou seja, a subclasse também compartilha o mesmo estado da classe base Monostate.

## Diagramas

*   `singleton.graphml`: Um arquivo GraphML que provavelmente contém o diagrama UML para o padrão Singleton, descrevendo suas classes e interações.
*   `singleton.png`: Uma imagem PNG que é uma representação visual do diagrama contido em `singleton.graphml`, facilitando a compreensão rápida da estrutura do padrão.

Estes arquivos visuais são excelentes para consolidar o entendimento dos padrões apresentados.
