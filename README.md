# Projeto de Extração de Dados de PDF com Tabula

Este projeto tem como objetivo extrair dados de tabelas presentes em um arquivo PDF utilizando a biblioteca Tabula em Python. Ele é especialmente útil quando há a necessidade de obter dados estruturados a partir de tabelas complexas em um PDF.

## Bibliotecas Utilizadas

O projeto utiliza as seguintes bibliotecas:

- Tabula: Uma biblioteca Python para extração de tabelas de PDFs. Ela permite ler as tabelas em formato tabular e convertê-las em DataFrames do pandas.
- Pandas: Uma biblioteca Python para manipulação e análise de dados. Ela é utilizada para trabalhar com os dados extraídos do PDF, realizar transformações e salvá-los em um arquivo CSV.
- Zipfile: Uma biblioteca Python para manipulação de arquivos ZIP. É usada para compactar o arquivo CSV em um arquivo ZIP no final do processo.

## Instalação das Bibliotecas

Para instalar as bibliotecas necessárias, utilize o gerenciador de pacotes do Python, pip, executando os seguintes comandos:

```bash
pip install tabula-py
```
```bash
pip install pandas
```
```bash
pip install zipfile
```


## Como Utilizar

Para clonar este projeto e obter uma cópia local em sua máquina, siga os passos abaixo:

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde deseja clonar o projeto.
3. Execute o seguinte comando para clonar o repositório:
```bash
git clone https://github.com/NicolasBastos027/TransformacaoDeDados.git
```
4. Execute o script Python e aguarde a conclusão:
```bash
python codigo.py
```
5. O PDF será lido, convertido para CSV e será salvo na pasta atual. Logo após será zipado com o nome especificado.

Após clonar o projeto, você terá acesso aos arquivos e poderá executar o código em sua própria máquina. Certifique-se de instalar as bibliotecas necessárias antes de executar o projeto.
