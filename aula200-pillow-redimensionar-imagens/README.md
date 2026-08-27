
# Aula 200 — Redimensionamento de Imagens com Pillow

Este diretório contém um exemplo prático de como utilizar a biblioteca **Pillow (PIL)**, considerada uma ferramenta essencial para o processamento de imagens e visão computacional em Python.

## 📌 Visão Geral
A biblioteca Pillow permite que desenvolvedores manipulem, filtrem e apliquem transformações geométricas em arquivos de imagem de forma eficiente. Neste exercício, o foco é o **redimensionamento proporcional**, garantindo que a imagem mude de tamanho sem perder sua proporção original (aspect ratio).

## 🛠️ Recursos e Métodos Abordados

### 1. Gerenciamento de Caminhos (`pathlib`)
O programa utiliza a biblioteca `pathlib` para localizar os arquivos `original.JPG` e definir o destino da nova imagem. O uso de `Path(__file__).parent` garante que o script funcione corretamente independentemente da pasta onde for executado [Source Program].

### 2. Manipulação de Imagens com `PIL.Image`
*   **`Image.open(caminho)`**: Abre o arquivo de imagem e cria um objeto de imagem para processamento [Source Program].
*   **`pil_image.size`**: Atributo que retorna uma tupla contendo a **largura (width)** e a **altura (height)** da imagem em pixels [Source Program].
*   **`pil_image.info['exif']`**: Acessa os metadados **EXIF** da imagem, que contêm informações técnicas como modelo da câmera e data da captura [Source Program].

### 3. Lógica de Redimensionamento Proporcional
Para evitar distorções, o programa calcula a nova altura de forma dinâmica baseada na largura desejada ($640px$):
$$nova\_altura = \frac{altura\_original \times nova\_largura}{largura\_original}$$
O resultado é arredondado com a função `round()` para garantir valores inteiros de pixels [Source Program].

### 4. Execução e Exportação
*   **`resize(size)`**: Cria uma nova versão da imagem com as dimensões calculadas [Source Program].
*   **`save(caminho, optimize, quality)`**: Salva a imagem processada no disco. 
    *   `optimize=True`: Tenta reduzir o tamanho do arquivo final.
    *   `quality=70`: Ajusta o nível de compressão (escala de 0 a 100) para equilibrar qualidade visual e espaço em disco [Source Program].

## 🚀 Exemplo de Código
```python
from PIL import Image
from pathlib import Path

# Configuração de caminhos
ROOT = Path(__file__).parent
original = Image.open(ROOT / 'original.JPG')

# Redimensionamento
new_width = 640
w, h = original.size
new_height = round(h * new_width / w)

# Salvando com otimização
new_img = original.resize((new_width, new_height))
new_img.save(ROOT / 'new.JPG', optimize=True, quality=70)
```

## 📖 Referências Úteis
*   [Pillow Documentation (PIL)](https://pillow.readthedocs.io/en/stable/)
*   Processamento de Imagens e Visão Computacional com Python.

---