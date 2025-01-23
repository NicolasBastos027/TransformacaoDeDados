import tabula  # Importa a biblioteca tabula para ler tabelas de arquivos PDF
import zipfile  # Importa a biblioteca zipfile para manipulação de arquivos ZIP
import pandas as pd  # Importa a biblioteca pandas para manipulação de DataFrames

# Função para juntar as tabelas em um único DataFrame
def juntar_tabela(lista_tabelas):
    tabela_completa = pd.concat(lista_tabelas, ignore_index=True)  # Concatena todas as tabelas da lista em um único DataFrame
    return tabela_completa  # Retorna o DataFrame completo

# Caminho do arquivo PDF
caminho = 'Anexo_I_Rol_2021RN_465.2021_RN624_RN625.2024.pdf'  # Define o caminho do arquivo PDF

# Nome do arquivo CSV de destino
nome_do_arquivo_csv_destino = 'Anexo_I_Rol_2021RN_465.2021_RN624_RN625.2024.csv'  # Define o nome do arquivo CSV de destino

# Nome do arquivo ZIP de destino
nome_do_arquivo_zip_destino = 'Teste_Nicolas_Bastos.zip'  # Define o nome do arquivo ZIP de destino

# Lendo as tabelas do PDF (elas começam na página 3)
lista_tabelas = tabula.read_pdf(caminho, pages='3-180', lattice=True)  # Lê as tabelas do PDF das páginas 3 a 180

# Juntando as tabelas em um único DataFrame
tabela_completa = juntar_tabela(lista_tabelas)  # Junta todas as tabelas lidas em um único DataFrame

# Renomeando a coluna "RN\r(alteração)" para remover a quebra de linha
tabela_completa = tabela_completa.rename(columns={"RN\r(alteração)": "RN (alteração)"})  # Renomeia a coluna para remover a quebra de linha

# Alterando as colunas "OD" e "AMB" por suas respectivas legendas informadas no PDF
tabela_completa = tabela_completa.rename(columns={"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"})  # Renomeia as colunas "OD" e "AMB"

# Substituindo as quebras de linha ('\r') das linhas do DataFrame
tabela_completa = tabela_completa.replace('\r', ' ', regex=True)  # Substitui as quebras de linha nas células do DataFrame

# Salvando o DataFrame em um arquivo CSV
tabela_completa.to_csv(nome_do_arquivo_csv_destino, index=False)  # Salva o DataFrame em um arquivo CSV

# Criando um arquivo ZIP contendo o arquivo CSV
with zipfile.ZipFile(nome_do_arquivo_zip_destino, 'w', zipfile.ZIP_DEFLATED) as arquivozip:
    arquivozip.write(nome_do_arquivo_csv_destino)  # Adiciona o arquivo CSV ao arquivo ZIP
