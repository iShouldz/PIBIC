"""Função script: Exibe no terminal as estatisticas para cada linguagem"""

import os
import pandas as pd

def obter_estatisticas_linguagem(csv_path):
    df = pd.read_csv(csv_path)

    media_linhas_totais = df['LinhasTotais'].mean()
    media_linhas_adicionadas = df['LinhasAdicionadas'].mean()
    media_linhas_removidas = df['LinhasRemovidas'].mean()

    total_ocorrencias = len(df)

    print(f'\nEstatísticas para a linguagem: {csv_path}')
    print(f'Média de Linhas Totais: {media_linhas_totais:.2f}')
    print(f'Média de Linhas Adicionadas: {media_linhas_adicionadas:.2f}')
    print(f'Média de Linhas Removidas: {media_linhas_removidas:.2f}')
    print(f'Total de Ocorrências: {total_ocorrencias}\n')

def analisar_pasta(pasta):
    contador = 0
    for arquivo in os.listdir(pasta):
        contador += 1
        print(f'Arquivo nº {contador}')
        if arquivo.endswith('.csv'):
            caminho_arquivo = os.path.join(pasta, arquivo)
            obter_estatisticas_linguagem(caminho_arquivo)

pasta_com_csvs = '../csvLinguage'
analisar_pasta(pasta_com_csvs)
