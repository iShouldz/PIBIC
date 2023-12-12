"""Função script: Concatena varios CSV em um"""

import os
import pandas as pd

def combinar_csvs(diretorio, arquivo_saida):
    arquivos_csv = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.csv')]

    if not arquivos_csv:
        print('Não foram encontrados arquivos CSV no diretório.')
        return

    dataframes = []

    for arquivo_csv in arquivos_csv:
        caminho_arquivo = os.path.join(diretorio, arquivo_csv)
        dados_csv = pd.read_csv(caminho_arquivo)
        dataframes.append(dados_csv)

    dados_combinados_final = pd.concat(dataframes, ignore_index=True)

    caminho_saida = os.path.join(diretorio, arquivo_saida)
    dados_combinados_final.to_csv(caminho_saida, index=False)

    print(f'Arquivos CSV combinados com sucesso. O resultado foi salvo em {caminho_saida}.')

diretorio_dados = '../../../stats/csv'
arquivo_saida_combinado = 'linguagemSemDupHashStats.csv'
combinar_csvs(diretorio_dados, arquivo_saida_combinado)
