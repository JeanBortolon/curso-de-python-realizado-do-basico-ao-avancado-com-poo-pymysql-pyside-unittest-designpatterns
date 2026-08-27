
# Aula 183 — `string.Template` para Substituição de Variáveis

Este diretório contém exemplos práticos de como utilizar a classe **`string.Template`** do Python para realizar a substituição dinâmica de variáveis em textos, como modelos de e-mails ou documentos.

## 📌 Visão Geral
O recurso `string.Template` é uma alternativa poderosa e segura ao uso de f-strings ou do método `.format()` quando lidamos com textos externos ou templates onde a sintaxe de substituição precisa ser simplificada para o usuário final. Ele permite definir espaços reservados (placeholders) que serão preenchidos por dados contidos em um dicionário ou argumentos nomeados [Source Program, 1473].

## 🛠️ Recursos e Métodos Abordados

### 1. Métodos de Substituição
O programa demonstra a diferença fundamental entre os dois principais métodos de preenchimento:
*   **`substitute(mapping)`**: Realiza a substituição das variáveis. Caso alguma chave esperada no template não seja encontrada no dicionário de dados, ele **lança um erro** (`KeyError`) [Source Program].
*   **`safe_substitute(mapping)`**: Realiza a substituição de forma "segura". Se faltar alguma variável, ele não gera erro; em vez disso, mantém o placeholder original no texto final [Source Program].

### 2. Customização com Herança de Classe
O código utiliza o conceito de **Orientação a Objetos** para modificar o comportamento padrão do template.
*   **`MyTemplate(string.Template)`**: Ao criar uma subclasse, é possível alterar o **delimitador** padrão (que normalmente é o `$`) para outros caracteres, como o `%` (`delimiter = '%'`) [Source Program, 1614].

### 3. Internacionalização e Formatação
Para tornar o exemplo mais realista (como um e-mail de cobrança), foram integradas bibliotecas auxiliares:
*   **`locale`**: Utilizada para configurar as convenções regionais do sistema (`setlocale`) e formatar números automaticamente como moeda brasileira (**R$**) através do método `currency` [Source Program].
*   **`datetime`**: Usada para manipular e formatar datas em padrões específicos (ex: `dd/mm/aaaa`) usando `strftime` [Source Program].
*   **`pathlib`**: Empregada para gerenciar caminhos de arquivos de forma moderna e independente do sistema operacional (`Path(__file__)`) [Source Program].

## 🚀 Exemplo de Execução
O programa lê um arquivo de texto externo (`aula183.txt`), cria um objeto de template personalizado e injeta um dicionário de dados (`dados`) que contém o nome do cliente, valor formatado e informações de contato [Source Program].

```python
# Trecho do código para criar o template personalizado
class MyTemplate(string.Template):
    delimiter = '%'

template = MyTemplate(texto)
print(template.substitute(dados))
```

## 📖 Referências Úteis
*   [Documentação oficial do Python — Template Strings](https://docs.python.org/3/library/string.html#template-strings) [Source Program].

---