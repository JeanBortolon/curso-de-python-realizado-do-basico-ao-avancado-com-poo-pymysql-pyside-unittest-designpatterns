# 🖥️ Aula 187: Argumentos de Linha de Comando com sys.argv e ArgumentParser

## A Estrutura da Pasta aula187 📁

```
aula187-sys.argv-exec-arquivos-com-args-no-sistema/
├── aula187-sys.argv.py                          # 🐍 Forma simples de ler argumentos
└── aula188-argparse.ArgumentParser.py           # 🐍 Forma profissional de ler argumentos
```

---

## Os Arquivos da Pasta 📄

### 1. **aula187-sys.argv.py** (Forma Simples)
Este arquivo mostra a forma **básica** de receber argumentos.

```python
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça outra coisa com {argumentos[2]}')
    except IndexError:
        print('Faltam argumentos')
```

**O que faz:**
- ✅ Verifica se você passou argumentos
- ✅ Mostra quais argumentos foram passados
- ✅ Usa os argumentos para fazer coisas diferentes
- ✅ Trata erros se faltar argumentos

**Como usar:**
```
python aula187-sys.argv.py valor1 valor2
```

### 2. **aula188-argparse.ArgumentParser.py** (Forma Profissional)
Este arquivo mostra a forma **avançada e profissional** de processar argumentos.

```python
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela',
    metavar='STRING',
    required=False,
    action='append',  # Recebe mais de uma vez
)
parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs',
    action='store_true'
)

args = parser.parse_args()
```

**O que faz:**
- ✅ Define argumentos com nomes claros (`-b`, `--basic`)
- ✅ Cada argumento tem uma descrição (help)
- ✅ Muito mais profissional e organizado
- ✅ Fácil para usuários entenderem como usar

---

## Temas Abordados 📚

### 1. **sys.argv** 🔤

```python
import sys
argumentos = sys.argv
```

- **sys** = módulo especial do Python que acessa informações do sistema
- **argv** = lista de argumentos passados na linha de comando
- **Importante:** `argv[0]` = nome do arquivo, `argv[1]` em diante = seus argumentos

**Exemplo:**
```
python programa.py João 25

# sys.argv será:
# ['programa.py', 'João', '25']
```

| Índice | Valor |
|--------|-------|
| argv[0] | 'programa.py' (nome do programa) |
| argv[1] | 'João' (primeiro argumento) |
| argv[2] | '25' (segundo argumento) |

### 2. **ArgumentParser** 🎯
```python
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-b', '--basic', help='Descrição')
args = parser.parse_args()
```

**Vantagens do ArgumentParser:**
- 📋 Argumentos com **nomes claros** (`-b` ou `--basic`)
- 💬 Mensagem de **ajuda automática** (`python arquivo.py -h`)
- 🔒 **Validação** de argumentos
- 🏷️ Argumentos **opcionais** vs **obrigatórios**

### 3. **Tipos de Argumentos** 🏷️

#### ✅ Argumento Obrigatório
```python
parser.add_argument('nome', help='Seu nome')  # Precisa passar!
# python arquivo.py João
```

#### ⚙️ Argumento Opcional (com padrão `-`)
```python
parser.add_argument('-n', '--nome', required=False)
# python arquivo.py -n João
# ou
# python arquivo.py --nome João
```

#### 🔢 Argumento com Tipo
```python
parser.add_argument('-idade', type=int)  # Precisa ser número!
```

#### 📚 Argumento que Pode Ser Repetido
```python
parser.add_argument('-i', '--item', action='append')
# python arquivo.py -i livro -i caneta -i caderno
```

#### ✔️ Argumento Verdadeiro/Falso (Flag)
```python
parser.add_argument('-v', '--verbose', action='store_true')
# python arquivo.py -v  # verbose = True
# python arquivo.py     # verbose = False
```

### 4. **Tratamento de Erros** ⚠️
```python
if qtd_argumentos <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
    except IndexError:
        print('Faltam argumentos')
```

- ✅ Verifica se argumentos foram passados
- ✅ Trata erros quando faltam argumentos
- ✅ Evita que o programa quebre

### 5. **Slicing de Lista** ✂️
```python
argumentos[1:]  # Todos exceto o primeiro (programa.py)
```

- `[0]` = primeiro elemento
- `[1:]` = do segundo em diante (pula o nome do programa)
- `[1:3]` = do segundo até o terceiro

---

## Exemplos Práticos 💡

### Exemplo 1: sys.argv Simples
```python
# arquivo: saudacao.py
import sys

if len(sys.argv) < 2:
    print("Olá, estranho!")
else:
    nome = sys.argv[1]
    print(f"Olá, {nome}!")
```

**Executar:**
```
python saudacao.py João
# Resultado: Olá, João!
```

### Exemplo 2: ArgumentParser Profissional
```python
# arquivo: calculadora.py
from argparse import ArgumentParser

parser = ArgumentParser(description='Calculadora simples')
parser.add_argument('numero1', type=float)
parser.add_argument('numero2', type=float)
parser.add_argument('-op', '--operacao', default='soma', 
                    choices=['soma', 'subtração', 'multiplicação'])

args = parser.parse_args()

if args.operacao == 'soma':
    print(f"{args.numero1} + {args.numero2} = {args.numero1 + args.numero2}")
```

**Executar:**
```
python calculadora.py 10 5 -op soma
# Resultado: 10.0 + 5.0 = 15.0
```

---

## Passo a Passo de Execução ⚙️

### Com sys.argv:
```
1. Você executa: python aula187-sys.argv.py João 25
   ↓
2. Python cria:  sys.argv = ['aula187-sys.argv.py', 'João', '25']
   ↓
3. len(sys.argv) = 3 (maior que 1 ✓)
   ↓
4. Programa entra no else
   ↓
5. Mostra na tela os argumentos: ['João', '25']
   ↓
6. Faz algo com argumentos[1] = 'João'
   ↓
7. Faz outra coisa com argumentos[2] = '25'
```

### Com ArgumentParser:
```
1. Você executa: python aula188-argparse.ArgumentParser.py -b "Olá" -v
   ↓
2. ArgumentParser processa os argumentos
   ↓
3. Valida se estão corretos
   ↓
4. Coloca em um objeto 'args'
   ↓
5. Você acessa: args.basic = "Olá"
   ↓
6. Você acessa: args.verbose = True
```

---

## Recursos Utilizados 🔧

| Recurso | O que faz |
|---------|-----------|
| **sys.argv** | Lista de argumentos passados na linha de comando |
| **len()** | Conta quantos argumentos foram passados |
| **ArgumentParser** | Processa argumentos de forma profissional |
| **add_argument()** | Define um novo argumento |
| **parse_args()** | Processa os argumentos recebidos |
| **required** | Define se um argumento é obrigatório |
| **action** | Define como o argumento se comporta (append, store_true, etc) |
| **type** | Define o tipo do argumento (int, float, str) |
| **choices** | Lista de valores permitidos |
| **default** | Valor padrão se não for passado |
| **help** | Mensagem de ajuda para o usuário |
| **metavar** | Nome da variável na mensagem de ajuda |

---

## Palavras Novas 🔤

| Palavra | Significado |
|---------|------------|
| **Argumento** | Informação que você passa ao programa |
| **sys.argv** | Lista com todos os argumentos |
| **Linha de comando** | Terminal/Prompt de comando |
| **Parser** | Máquina que "quebra" e entende argumentos |
| **Flag** | Argumento do tipo verdadeiro/falso (ativa algo) |
| **Obrigatório** | Precisa passar, senão dá erro |
| **Opcional** | Pode passar ou não |
| **Índice** | Posição de um item em uma lista |
| **Slicing** | Pegar uma parte de uma lista |
| **Action** | O que fazer com o argumento recebido |

---

## Quando Usar Cada Um? 🎯

### Use **sys.argv** quando:
- ✅ O programa é muito simples
- ✅ Poucos argumentos (1-2)
- ✅ Quer código rápido

### Use **ArgumentParser** quando:
- ✅ O programa é mais complexo
- ✅ Muitos argumentos
- ✅ Quer uma interface profissional
- ✅ Precisa de validação
- ✅ Quer mensagem de ajuda automática

---

## Exemplos de Programas Reais 🌍

**Git** (controle de versão):
```
git commit -m "Meu commit"
git push -u origin main
```

**Python (ajuda)**:
```
python -h
python --version
```

**npm (JavaScript)**:
```
npm install express
npm start --prefix ./src
```

---

## Resuminho em uma Frase 🎯

> "Argumentos de linha de comando permitem passar instruções para o programa antes dele executar, como um garçom que escuta seu pedido!" 🖥️➡️📋

---

## Dica Final ⚠️

Sempre use **-h** ou **--help** para ver como usar qualquer programa:

```
python aula188-argparse.ArgumentParser.py -h
```

Isso mostra automaticamente **todos os argumentos disponíveis** que você pode usar! 📖
