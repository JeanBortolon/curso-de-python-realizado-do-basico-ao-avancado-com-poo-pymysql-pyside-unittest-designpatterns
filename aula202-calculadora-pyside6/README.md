# Calculadora com PySide6

Este projeto implementa uma calculadora gráfica utilizando a biblioteca PySide6. Abaixo está a descrição dos arquivos e os recursos abordados em cada um deles.

## Arquivos e Recursos

### `main.py`
- **Descrição**: Arquivo principal que inicializa a aplicação.
- **Recursos**:
  - Criação da aplicação com `QApplication`.
  - Aplicação de tema escuro com `qdarkstyle`.
  - Configuração da janela principal e widgets.

### `buttons.py`
- **Descrição**: Define os botões e o layout da grade de botões.
- **Recursos**:
  - Criação de botões personalizados com `QPushButton`.
  - Configuração de estilos e tamanhos dos botões.
  - Implementação de uma grade de botões com `QGridLayout`.

### `display.py`
- **Descrição**: Define o display da calculadora.
- **Recursos**:
  - Criação de um campo de entrada com `QLineEdit`.
  - Configuração de estilos e alinhamento do texto.
  - Tratamento de eventos de teclado para entrada de dados.

### `info.py`
- **Descrição**: Exibe informações adicionais no topo da calculadora.
- **Recursos**:
  - Criação de um rótulo com `QLabel`.
  - Configuração de estilos e alinhamento.

### `main_window.py`
- **Descrição**: Define a janela principal da aplicação.
- **Recursos**:
  - Configuração do layout principal com `QVBoxLayout`.
  - Ajuste do tamanho fixo da janela.
  - Adição de widgets ao layout.

### `styles.py`
- **Descrição**: Define estilos personalizados para os widgets.
- **Recursos**:
  - Criação de estilos com QSS (Qt Style Sheets).
  - Integração com o tema escuro.

### `utils.py`
- **Descrição**: Funções utilitárias para validação e conversão de dados.
- **Recursos**:
  - Validação de números e pontos decimais.
  - Conversão de strings para números.

### `variables.py`
- **Descrição**: Define variáveis globais para o projeto.
- **Recursos**:
  - Configuração de caminhos de arquivos.
  - Definição de cores e tamanhos de fonte.

### `files/`
- **Descrição**: Diretório para armazenar arquivos adicionais, como ícones.

## Como Executar
1. Certifique-se de ter o PySide6 instalado.
2. Execute o arquivo `main.py` para iniciar a aplicação:
   ```bash
   python main.py
   ```
