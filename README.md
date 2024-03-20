# ETL Project from Netflix Dataset

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/samuelsonbmg/ETL_Dataset_Excel_Files/blob/main/LICENSE)

# Sobre o Projeto
Trata-se de um projeto que tem por objetivo, realizar a análise de arquivos em formato excel, que foram disponibilizados em formato bruto, onde há a necessidade de realizar o agrupamento das informações contidas em todas as planilhas em apenas uma planilha final, que será utilizada para carga em um dashboard. (Ex. Power BI).

## About the Project
This is a project aimed at analyzing Excel files provided in raw format. The objective is to group the information from all sheets into a single final sheet, which will be used for loading into a dashboard (e.g., Power BI).

## Problemas a serem resolvidos
- Agrupamento dos arquivos em apenas uma planilha consolidada;
- Inclusão de uma nova coluna nesse arquivo final identificando o país de origem dos dados (pois essa informação está apenas no nome do arquivo e quando agruparmos, essa informações será perdida);
- Inclusão de uma nova coluna identificando a campanha de marketing;

## Tecnologias Utilizadas
- Python
- Pandas
- Virtual Enviroment (venv)

## Conhecimentos Aplicados
- Leitura de arquivos/pastas em diretório local
- Manipulação de dados extraídos de planilha xlsx
- Escrita de dados de saída em arquivo xlsx

## Bibliotecas Utilizadas
- Pandas
- Openpyxl
- XlsxWriter
