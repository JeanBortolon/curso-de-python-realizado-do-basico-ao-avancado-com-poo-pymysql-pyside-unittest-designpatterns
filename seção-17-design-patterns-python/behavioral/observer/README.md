# Padrão de Projeto Observer (Observador)

Este diretório contém um exemplo prático do **Padrão de Projeto Observer (Observador)**, que é um padrão comportamental.

## O que é o Padrão Observer?

O padrão Observer é uma forma de criar uma dependência de "um para muitos" entre objetos. Isso significa que, quando um objeto (chamado **Subject** ou **Observável**) muda seu estado, todos os outros objetos que dependem dele (chamados **Observers** ou **Observadores**) são automaticamente notificados e atualizados.

Pense nisso como um serviço de notícias:
*   Você se inscreve em um jornal (o **Observável**).
*   Quando uma nova notícia é publicada (o estado do jornal muda), você e todos os outros assinantes (os **Observadores**) recebem essa notícia.

### Conceitos Chave:

*   **Observável (Subject):** É o objeto que detém o estado que pode mudar. Ele mantém uma lista de Observadores e tem métodos para:
    *   Adicionar um Observador (`add_observer`).
    *   Remover um Observador (`remove_observer`).
    *   Notificar todos os Observadores sobre uma mudança (`notify_observers`).
*   **Observador (Observer):** É o objeto que deseja ser notificado sobre as mudanças no Observável. Ele implementa um método de atualização (`update`) que é chamado pelo Observável quando algo acontece.

## Arquivos neste Diretório:

### `observer-1.py`

Este arquivo Python implementa o Padrão Observer usando o exemplo de uma **Estação Meteorológica**.

*   **`IObservable` (Interface Abstrata para Observável):** Define o "contrato" para qualquer objeto que possa ser observado. Garante que qualquer Observável terá métodos para gerenciar Observadores e notificar sobre mudanças de estado.
*   **`WeatherStation` (Estação Meteorológica - Observável Concreto):** Esta é a nossa estação meteorológica. Ela é o "sujeito" que gera informações (temperatura, umidade).
    *   Ela mantém uma lista de dispositivos (Smartphones, Notebooks) que estão interessados nos dados do tempo.
    *   Quando a temperatura ou umidade mudam, ela **notifica** todos os dispositivos registrados.
*   **`IObserver` (Interface Abstrata para Observador):** Define o "contrato" para qualquer objeto que queira observar outro. Garante que qualquer Observador terá um método para receber atualizações.
*   **`Smartphone` (Observador Concreto):** Representa um smartphone que se registra na `WeatherStation`. Quando a estação meteorológica muda seu estado, o smartphone é notificado e imprime a nova informação.
*   **`Notebook` (Observador Concreto):** Representa um notebook que também se registra na `WeatherStation`. Ele também é notificado e processa a informação de uma maneira ligeiramente diferente, mostrando que cada Observador pode ter sua própria lógica de reação.

#### Como funciona no `observer-1.py`:

1.  Uma `WeatherStation` é criada (o Observável).
2.  `Smartphone`s e `Notebook`s são criados e "se inscrevem" (são adicionados como Observadores) na `WeatherStation`.
3.  Quando o estado da `WeatherStation` é alterado (por exemplo, `weather_station.state = {'temperature': '30'}`), ela automaticamente percorre sua lista de Observadores e chama o método `update()` de cada um.
4.  Cada Observador (`Smartphone` e `Notebook`) executa sua própria lógica de `update()` para processar a nova informação.
5.  É demonstrado como um Observador pode ser removido e como isso afeta as notificações futuras.

Este exemplo mostra de forma clara como o padrão Observer permite que os objetos se comuniquem sem ter um forte acoplamento (ou seja, o Observável não precisa saber detalhes sobre a implementação de cada Observador, apenas que eles têm um método `update`).