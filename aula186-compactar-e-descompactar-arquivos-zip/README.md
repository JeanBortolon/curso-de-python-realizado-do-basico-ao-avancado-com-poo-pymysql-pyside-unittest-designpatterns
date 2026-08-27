# 📦 Aula 186: Compactando e Descompactando Arquivos com Python

## A Estrutura da Pasta aula186 📁

```
aula186-compactar-e-descompactar-arquivos/
├── aula186.py                          # 🐍 O programa principal
├── aula186_compactado.zip              # 📦 Arquivo ZIP criado
├── aula_186_diretorio_zip/             # 📂 Pasta com os arquivos originais
│   ├── arquivo_0.txt
│   ├── arquivo_1.txt
│   ├── arquivo_2.txt
│   └── ... (até arquivo_9.txt)
└── aula186_descompactado/              # 📂 Pasta com arquivos extraídos
    ├── arquivo_0.txt
    ├── arquivo_1.txt
    └── ... (até arquivo_9.txt)
```

---

## Os Arquivos da Pasta 📄

### 1. **aula186.py** (O Programa Principal)
Este é o arquivo que contém toda a lógica do programa. Ele faz 3 coisas principais:

#### ✅ Cria arquivos originais
```python
criar_arquivos(10, CAMINHO_ZIP_DIR)
```
Cria 10 arquivos de texto (arquivo_0.txt até arquivo_9.txt) em uma pasta.

#### 📦 Compacta os arquivos em um ZIP
```python
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            zip.write(os.path.join(root, file), file)
```
Pega todos os arquivos e coloca em um único arquivo `.zip`.

#### 📖 Lê e lista os arquivos dentro do ZIP
```python
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)
```
Mostra na tela quais arquivos estão dentro do ZIP.

#### 🎁 Descompacta os arquivos
```python
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)
```
Tira todos os arquivos do ZIP e coloca em uma nova pasta.

---

### 2. **aula186_compactado.zip** 📦
- Este é o arquivo ZIP criado pelo programa
- Contém todos os 10 arquivos `.txt` em um formato comprimido
- Ocupa **MUITO MENOS ESPAÇO** do que os arquivos originais!
- Você pode enviar por e-mail facilmente 📧

### 3. **aula_186_diretorio_zip/** 📂
- Pasta que contém os **arquivos originais** antes de compactar
- Contém 10 arquivos: `arquivo_0.txt`, `arquivo_1.txt`, ..., `arquivo_9.txt`
- Após o programa executar, esta pasta é limpa/recriada

### 4. **aula186_descompactado/** 📂
- Pasta que contém os **arquivos extraídos** do ZIP
- Após descompactar, você terá os mesmos arquivos que estavam no ZIP
- É exatamente igual aos arquivos originais

---

## Temas Abordados 📚

### 1. **Módulo ZipFile** 🗜️
```python
from zipfile import ZipFile
```
É a ferramenta Python para trabalhar com arquivos ZIP.

#### Modos de operação:
- **'w'** = Write (Escrever/Criar um ZIP)
- **'r'** = Read (Ler um ZIP)
- **'a'** = Append (Adicionar ao ZIP)

### 2. **Compactação (Compress)** 📦
```python
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    zip.write(caminho_do_arquivo, nome_no_zip)
```
- Pega vários arquivos
- Coloca em um único arquivo `.zip`
- **Economiza espaço em disco** (até 90% menos!)

### 3. **Listagem de Arquivos** 📋
```python
zip.namelist()  # Lista todos os nomes dos arquivos
```
- Mostra quais arquivos estão dentro do ZIP
- Útil para saber o que tem lá dentro

### 4. **Descompactação (Extract)** 🎁
```python
zip.extractall(caminho_destino)
```
- Tira todos os arquivos do ZIP
- Coloca em uma pasta específica
- Os arquivos voltam ao seu tamanho original

### 5. **Context Manager (with statement)** 🔐
```python
with ZipFile(caminho, modo) as zip:
    # código aqui
    # O arquivo ZIP fecha automaticamente
```
- Garante que o arquivo ZIP seja **fechado corretamente**
- Evita corrupção de dados
- Automático e seguro! ✅

### 6. **os.walk()** 🚶
```python
for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
```
- **Varre** todos os arquivos em uma pasta e subpastas
- `root` = caminho atual
- `dirs` = subpastas encontradas  
- `files` = arquivos encontrados

### 7. **Limpeza de Pasta** 🧹
```python
shutil.rmtree(caminho, ignore_errors=True)
```
- Apaga uma pasta inteira (com tudo dentro)
- `ignore_errors=True` = não reclama se a pasta não existir

### 8. **Path (Pathlib)** 🛤️
```python
from pathlib import Path
CAMINHO_RAIZ = Path(__file__).parent
```
- Forma moderna de trabalhar com caminhos
- `__file__` = arquivo atual
- `.parent` = pasta que contém este arquivo

---

## Recursos Utilizados 🔧

| Recurso | O que faz |
|---------|-----------|
| **ZipFile** | Cria, lê e descompacta arquivos ZIP |
| **os.walk()** | Percorre todas as pastas e arquivos |
| **shutil.rmtree()** | Apaga pastas inteiras |
| **Path** | Trabalha com caminhos de forma moderna |
| **Context Manager (with)** | Abre e fecha arquivos com segurança |
| **zipfile.namelist()** | Lista nomes dos arquivos no ZIP |
| **zipfile.extractall()** | Descompacta tudo de uma vez |

---

## Passo a Passo do Programa ⚙️

```
1. Limpar pastas antigas
   └─ Remove pastas que possam já existir

2. Criar nova pasta para arquivos
   └─ mkdir aula_186_diretorio_zip/

3. Criar 10 arquivos de teste
   └─ arquivo_0.txt, arquivo_1.txt, ..., arquivo_9.txt

4. COMPACTAR
   ├─ Abre arquivo.zip em modo WRITE ('w')
   ├─ Varre pasta com os arquivos
   └─ Adiciona cada arquivo ao ZIP

5. LER CONTEÚDO DO ZIP
   ├─ Abre arquivo.zip em modo READ ('r')
   ├─ Lista todos os arquivos
   └─ Mostra na tela

6. DESCOMPACTAR
   ├─ Abre arquivo.zip em modo READ ('r')
   └─ Extrai tudo para a pasta aula186_descompactado/

7. Pronto! ✅
```

---

## Palavras Novas que Aprendemos 🔤

| Palavra | Significado |
|---------|------------|
| **Compactar** | Encolher/empacotar vários arquivos em um |
| **Descompactar** | Tirar os arquivos de dentro de um ZIP |
| **ZIP** | Formato de arquivo comprimido |
| **Compressão** | Diminuição do tamanho dos arquivos |
| **Arquivo** | Um arquivo individual (arquivo_0.txt) |
| **Diretório** | Uma pasta que contém arquivos |
| **Context Manager** | Forma segura de abrir e fechar arquivos |
| **Extract** | Descompactar/tirar de dentro |

---

## O que você pode fazer com isso? 💡

✅ Compactar fotos antes de enviar por e-mail  
✅ Fazer backup de vários arquivos em um ZIP  
✅ Organizar arquivos em grupos  
✅ Enviar projetos inteiros compactados  
✅ Fazer sistemas de download  
✅ Automatizar backup de documentos  

---

## Código Simplificado (Resumo) 📝

```python
# COMPACTAR
from zipfile import ZipFile

with ZipFile('meus_arquivos.zip', 'w') as zip:
    zip.write('foto1.jpg')
    zip.write('foto2.jpg')
    zip.write('documento.pdf')

# DESCOMPACTAR
with ZipFile('meus_arquivos.zip', 'r') as zip:
    zip.extractall('pasta_de_saida')
```

---

## Dica Importante ⚠️

📍 **ZIP vs Pasta Normal:**
- **Meu Documento.zip**: 50 MB (compactado) ✅ Fácil enviar!
- **Meu Documento (pasta)**: 500 MB (original) ❌ Difícil enviar!

**Comprimir economiza espaço e facilita compartilhamento!** 🚀

---

## Resuminho em uma frase 🎯

> "Com Python podemos empacotar muitos arquivos em um único ZIP para economizar espaço e facilitar o compartilhamento!" 📦➡️📬

