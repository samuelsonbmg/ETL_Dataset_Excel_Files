#########################################################################
#                                                                       #
#     Script for extract data from NETFLIX consumers datafiles          #
#                                                                       #
#########################################################################

# Bloco de importação das bibliotecas utilizadas
import pandas as pd         # Criação e manipulação de DataSet
import os                   # Manipulação de pastas dentro do Sistema Operacional
import glob                 # Utilizado para busca massiva de arquivos em pastas 

# Localização onde estão salvos os arquivos brutos
folder_path = 'src\\data\\raw'

# Localização onde será salvo o arquivo final
folder_ready = 'src\\data\\ready'

# Define o nome do arquivo de saída
output_file = os.path.join(folder_ready,'clean.xlsx')

# Listas todos os arquivos existes na pasta raw
excel_files = glob.glob(os.path.join(folder_path,'*.xlsx'))

if not excel_files:
    
    print("Nenhum arquivo foi encontrado!")

else:
    # Dataframe - tabela na memória para guardar o conteúdo dos arquivos
    dfs = []

    for excel_file in excel_files:
        
        try:
            # Cria um dataframe a partir da leitura dos arquivos em excel
            df_temp = pd.read_excel(excel_file)
            
            # Faz a leitura do nome dos arquivos e extrai o nome do país
            file_name = os.path.basename(excel_file)
            country_temp = file_name.split('_')
            country = str(country_temp[2][:-5]).title()

            # Cria uma nova coluna e insere o nome do país
            df_temp['Location'] = country

            # Cria uma nova coluna 'Campaign' e insere apenas no nome da campaign retirada do 'utm_link'
            df_temp['Campaign'] = df_temp['utm_link'].str.extract(r'utm_campaign=(.*)')
                
            # Cria uma nova coluna e insere o nome do arquivo que originou os dados
            df_temp['Origin file'] = file_name

            # Guarda dados tratados dentro de uma dataframe comum
            dfs.append(df_temp)

        except Exception as e:
            print(f"Erro ao ler aquivo: {excel_file} : {e}")

if dfs:
        
    # Concatena todas as tabelas salvas no dfs dentro de uma única tabela.
    result = pd.concat(dfs, ignore_index=True)

    # Cria uma instância do Excel com o nome do arquivo proposto
    writer = pd.ExcelWriter(output_file,engine='xlsxwriter')

    # Insere os dados do data frame dentro do Excel
    result.to_excel(writer, index=False)

    # Salva as alterações na planilha do Excel e encerra a instância.
    writer._save()

else:

    print("Nenhum dado para ser salvo!")
