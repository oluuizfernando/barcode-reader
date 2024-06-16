# Leitor de Código de Barras de PDF
Este projeto implementa um leitor de código de barras para PDFs utilizando Python. Ele é capaz de extrair imagens das páginas do PDF, identificar e decodificar códigos de barras presentes nas imagens utilizando a biblioteca pyzbar, e organizar os dados em um arquivo Excel utilizando pandas e openpyxl.

## Funcionalidades
Extração de Imagens: Utiliza a biblioteca pdf2image para converter páginas de PDF em imagens.

Decodificação de Código de Barras: Utiliza a biblioteca pyzbar para identificar e decodificar códigos de barras nas imagens extraídas.

Exportação de Dados: Organiza os dados dos códigos de barras decodificados em um arquivo Excel (.xlsx) utilizando pandas e openpyxl.

## Pré-requisitos

Python 3.x instalado
Instalação das bibliotecas necessárias:

```bash
pip install pyzbar pdf2image pandas openpyxl
```

### Como Usar
Clone o repositório:

```bash
git clone https://github.com/oluuizfernando/barcode-reader.git
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execute o script:

```bash
python leitor_codigo_barras_pdf.py --arquivo caminho/do/arquivo.pdf
```

Substitua caminho/do/arquivo.pdf pelo caminho do seu PDF de entrada.

Resultados:

O script irá processar o PDF, extrair as imagens das páginas, decodificar os códigos de barras encontrados e gerar um arquivo Excel (output.xlsx) com os resultados.

## Contribuições
Contribuições são bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Contato
Email: euluizfernando2001@gmail.com
LinkedIn: [Meu Perfil do Linkedin](https://www.linkedin.com/in/luizfernandotr/)
