# Padrão de Projeto: Façade (Fachada)

## Visão Geral

Este diretório contém um exemplo prático do **Padrão de Projeto Façade (Fachada)**, um padrão estrutural que visa simplificar a interface para um conjunto complexo de classes em um subsistema. A ideia é fornecer uma interface de nível mais alto que torne o subsistema mais fácil de usar para o cliente.

### O Que é o Padrão Façade?

Imagine que você tem um sistema com muitas partes interdependentes e complexas (um "subsistema"). Para que um cliente (outra parte do seu código) use esse subsistema, ele precisaria entender e interagir com todas essas partes individualmente, o que pode ser confuso e propenso a erros.

O padrão Façade resolve isso criando uma "fachada" – uma única classe que atua como uma interface simplificada para todo o subsistema. O cliente interage apenas com essa fachada, e a fachada, por sua vez, sabe como coordenar e delegar as chamadas para as classes internas do subsistema, escondendo a complexidade.

**Benefícios:**
*   **Simplificação:** Reduz a complexidade percebida do sistema.
*   **Acoplamento Reduzido:** O cliente se acopla à fachada, não às classes internas do subsistema, tornando o código mais flexível.
*   **Melhor Organização:** Ajuda a organizar o código em camadas.

## Arquivos no Diretório

### `facade-1.py`

Este arquivo Python implementa o padrão Façade utilizando um cenário de **Estação Meteorológica** e seus **Observadores**.

#### Estrutura do Código:

1.  **`IObservable` e `IObserver` (Interfaces/ABCs):**
    *   Definem os contratos (métodos obrigatórios) para objetos que podem ser observados (como uma estação meteorológica) e para os objetos que observam (como smartphones ou notebooks). Isso segue o Padrão Observer, que é um subsistema que a fachada está gerenciando.

2.  **`WeatherStation` (Observável Concreto):**
    *   Esta classe representa a estação meteorológica real. Ela mantém o estado atual do clima (temperatura, umidade) e uma lista de observadores. Quando o estado do clima muda, ela notifica todos os observadores registrados.

3.  **`Smartphone` e `Notebook` (Observadores Concretos):**
    *   São exemplos de dispositivos que "observam" a `WeatherStation`. Eles implementam o método `update()`, que é chamado pela `WeatherStation` quando há uma mudança no clima, permitindo que cada dispositivo reaja de sua própria maneira (por exemplo, exibindo a temperatura na tela).

4.  **`WeatherStationFacade` (A Fachada):**
    *   Esta é a classe central do padrão Façade neste exemplo. Ela encapsula a complexidade de interagir diretamente com a `WeatherStation` e seus `Observers`.
    *   A `WeatherStationFacade` cria e gerencia a instância da `WeatherStation` e também pode inicializar e registrar observadores (como `Smartphone` e `Notebook`).
    *   Ela oferece métodos simplificados como `change_state()` para atualizar o clima, `add_observer()`, `remove_observer()` e `reset_state()`. O cliente só precisa chamar esses métodos da fachada, sem se preocupar com os detalhes internos de como a `WeatherStation` notifica seus observadores.

#### Como a Fachada Simplifica o Uso:

Sem a `WeatherStationFacade`, um cliente precisaria:
*   Instanciar `WeatherStation`.
*   Instanciar `Smartphone` e `Notebook`.
*   Registrar manualmente cada `Smartphone` e `Notebook` na `WeatherStation` usando `add_observer()`.
*   Chamar `weather_station.state = {'temperatura': 'X'}` para atualizar o estado.

Com a `WeatherStationFacade`, o cliente simplesmente:
*   Instancia `WeatherStationFacade`.
*   Chama `facade.change_state({'temperatura': 'X'})`.

A fachada cuida de toda a orquestração interna, tornando o uso do subsistema muito mais simples e limpo.

### `facade.graphml` e `facade.png`

Estes arquivos provavelmente contêm:
*   **`facade.graphml`:** Um arquivo XML que descreve um diagrama (geralmente criado com ferramentas como yEd Graph Editor) que visualiza a estrutura do padrão Façade e as relações entre as classes.
*   **`facade.png`:** Uma imagem (PNG) que é a representação visual desse diagrama, mostrando graficamente como a fachada interage com o subsistema e como os clientes interagem apenas com a fachada.

Eles servem como uma representação visual clara de como o padrão Façade é aplicado neste contexto.
