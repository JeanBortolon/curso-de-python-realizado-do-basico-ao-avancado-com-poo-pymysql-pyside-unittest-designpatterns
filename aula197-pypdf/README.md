
# Aula 197 — Manipulação de PDFs com `PyPDF2`

Este diretório contém exemplos práticos de como ler, extrair, dividir e unir arquivos PDF utilizando a biblioteca **`PyPDF2`**, uma ferramenta feita em Python puro, gratuita e de código aberto [Source Program].

## 📌 Visão Geral
A biblioteca `PyPDF2` é capaz de realizar diversas tarefas complexas em documentos PDF, como manipulação de metadados, transformação de páginas, extração de texto e imagens, além de unir múltiplos arquivos em um só [Source Program].

## 🛠️ Recursos e Classes Abordados

### 1. Gerenciamento de Arquivos (`pathlib`)
O programa utiliza `pathlib.Path` para gerenciar caminhos de forma dinâmica, criando a pasta `arquivos_novos` automaticamente caso ela não exista através do método `.mkdir(exist_ok=True)` [Source Program].

### 2. Leitura de PDFs (`PdfReader`)
*   **`PdfReader(caminho)`**: Abre o arquivo PDF para leitura [Source Program].
*   **`reader.pages`**: Permite acessar as páginas do documento como uma lista. É possível obter a quantidade de páginas com `len(reader.pages)` [Source Program].
*   **Extração de Conteúdo**: O código demonstra (em comentários) como extrair texto com `extract_text()` e como acessar imagens contidas nas páginas através do atributo `.images` [Source Program].

### 3. Escrita e Divisão (`PdfWriter`)
*   **`PdfWriter()`**: Cria um novo objeto para "escrever" um arquivo PDF do zero [Source Program].
*   **`writer.add_page(page)`**: Adiciona uma página específica a um objeto de escrita [Source Program].
*   **Divisão de Arquivos**: O programa realiza um laço de repetição (`for`) para iterar por todas as páginas do PDF original e salvar cada uma delas como um novo arquivo individual (ex: `page0.pdf`, `page1.pdf`, etc.) [Source Program].

### 4. União de Arquivos (`PdfMerger`)
*   **`PdfMerger()`**: Classe dedicada à fusão (merge) de múltiplos arquivos PDF [Source Program].
*   **`merger.append(file)`**: Adiciona um arquivo completo à fila de fusão. O programa demonstra como unir arquivos específicos em uma ordem determinada [Source Program].
*   **`merger.write(caminho)`**: Gera o arquivo final consolidado (neste caso, `MERGED.pdf`) [Source Program].

## 🚀 Instalação e Requisitos
Para executar o programa, é necessário instalar a biblioteca no seu ambiente virtual:
```bash
pip install pypdf2
```

## 📖 Documentação Oficial
Para aprofundar seus conhecimentos, consulte a [Documentação do PyPDF2](https://pypdf2.readthedocs.io/en/3.0.0/) [Source Program].

---

**Dica técnica:** Ao lidar com arquivos binários (como PDFs e imagens extraídas), lembre-se sempre de abrir os arquivos no modo de escrita binária (**`'wb'`**) para garantir a integridade dos dados [Source Program].