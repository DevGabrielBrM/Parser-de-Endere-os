# Parser de Endereços

## Visão Geral

O **Parser de Endereços** é um script em Python que utiliza expressões regulares (regex) para analisar e extrair componentes de diferentes formatos de endereços fornecidos pelo usuário. O objetivo é facilitar a organização e manipulação de informações de endereço em aplicações.

## Funcionalidades

- **Suporte a Múltiplos Formatos de Endereço**:
  - **Formato Nacional:** "Rua, Número"
  - **Formato Nacional com Letra:** "Rua, Número Letra"
  - **Formato Internacional:** "Número Rua"
  - **Formato Internacional com Prefixo:** "Rua Número No X"

## Instalação

1. **Pré-requisitos**: Verifique se você possui o Python instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).
   
2. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu_usuario/parser_enderecos.git
   cd parser_enderecos
   ```

3. **Execute o Script**:
   Certifique-se de estar no diretório do projeto e execute:
   ```bash
   python parser_endereco.py
   ```

## Uso

1. **Entrada de Dados**:
   - Quando solicitado, insira um endereço em um dos formatos suportados. Exemplos:
     - `"Rua das Flores, 123"`
     - `"Calle 22, No 22"`
     - `"123, Rua Principal"`
     - `"Rua da Paz 44 N° 5"`

2. **Saída**:
   - O script irá gerar um dicionário com o endereço analisado. Exemplo de saída:
   ```json
   {"Rua": "Rua das Flores", "Número": "123"}
   ```

## Padrões de Regex Utilizados

1. **Formato Nacional**: Captura endereços no formato "Rua, Número".
   ```regex
   ^[A-Za-zÀ-ÿ]+(?:[\s\.][A-Za-zÀ-ÿ]+)*\s*,?\s*\d+\s*$
   ```

2. **Formato Nacional com Letra**: Captura endereços que incluem letras após o número.
   ```regex
   ^[A-Za-zÀ-ÿ]+(?:[\s\.][A-Za-zÀ-ÿ]+)*,?\s*\d+\s*[A-Za-zÀ-ÿ]*\s*([A-Za-zÀ-ÿ]+\s*)*$
   ```

3. **Formato Internacional**: Captura endereços iniciando com um número.
   ```regex
   ^[0-9]+,?\s*(?:[\s\.'-][A-Za-zÀ-ÿ]+)+$
   ```

4. **Formato Internacional com Prefixo**: Captura endereços com um prefixo específico.
   ```regex
   ^([A-Za-zÀ-ÿ\s\.'-]+\s+\d+)\s*,?\s+((No|no|NO|N°|Nº|Núm\.|nr|número|numero)\s+\d+)$
   ```
