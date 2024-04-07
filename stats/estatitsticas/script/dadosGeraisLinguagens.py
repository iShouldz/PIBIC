"""Função script: Exibe no terminal as estatisticas para cada linguagem"""

import os
import pandas as pd


def obter_estatisticas_linguagem(csv_path):
    df = pd.read_csv(csv_path)

    linhas_totais = df['LinhasTotais']

    media_linhas_totais = df['LinhasTotais'].mean()
    mediana_linhas_totais = df['LinhasTotais'].median()
    q1_linhas_totais = df['LinhasTotais'].quantile(0.25)
    q3_linhas_totais = df['LinhasTotais'].quantile(0.75)
    linhas_totais_ajustadas = linhas_totais.loc[
        (linhas_totais >= linhas_totais.quantile(0.1)) & (linhas_totais <= linhas_totais.quantile(0.9))]
    media_ajustada_linhas_totais = linhas_totais_ajustadas.mean()

    media_linhas_adicionadas = df['LinhasAdicionadas'].mean()
    mediana_linhas_adicionadas = df['LinhasAdicionadas'].median()
    q1_linhas_adicionadas = df['LinhasAdicionadas'].quantile(0.25)
    q3_linhas_adicionadas = df['LinhasAdicionadas'].quantile(0.75)

    media_linhas_removidas = df['LinhasRemovidas'].mean()
    mediana_linhas_removidas = df['LinhasRemovidas'].median()
    q1_linhas_removidas = df['LinhasRemovidas'].quantile(0.25)
    q3_linhas_removidas = df['LinhasRemovidas'].quantile(0.75)

    total_ocorrencias = len(df)

    print(f'\nEstatísticas para a linguagem: {csv_path}')

    # Linhas Totais
    print(f'Média de Linhas Totais: {media_linhas_totais:.2f}')
    print(f'Mediana de Linhas Totais: {mediana_linhas_totais:.2f}')
    print(f'Primeiro Quartil (Q1) de Linhas Totais: {q1_linhas_totais:.2f}')
    print(f'Terceiro Quartil (Q3) de Linhas Totais: {q3_linhas_totais:.2f} \n')

    # Linhas Adicionadas
    print(f'Média de Linhas Adicionadas: {media_linhas_adicionadas:.2f}')
    print(f'Mediana de Linhas Adicionadas: {mediana_linhas_adicionadas:.2f}')
    print(f'Primeiro Quartil (Q1) de Linhas Adicionadas: {q1_linhas_adicionadas:.2f}')
    print(f'Terceiro Quartil (Q3) de Linhas Adicionadas: {q3_linhas_adicionadas:.2f}\n')

    # Linhas Removidas
    print(f'Média de Linhas Removidas: {media_linhas_removidas:.2f}')
    print(f'Mediana de Linhas Removidas: {mediana_linhas_removidas:.2f}')
    print(f'Primeiro Quartil (Q1) de Linhas Removidas: {q1_linhas_removidas:.2f}')
    print(f'Terceiro Quartil (Q3) de Linhas Removidas: {q3_linhas_removidas:.2f}\n')

    print(f'Total de Ocorrências: {total_ocorrencias}\n')
    print(f'Média Ajustada de Linhas Totais: {media_ajustada_linhas_totais:.2f}')


def analisar_pasta(pasta):
    contador = 0
    for arquivo in os.listdir(pasta):
        contador += 1
        print(f'Arquivo nº {contador}')
        if arquivo.endswith('.csv'):
            caminho_arquivo = os.path.join(pasta, arquivo)
            obter_estatisticas_linguagem(caminho_arquivo)

pasta_com_csvs = 'csvLimpoComStats'
analisar_pasta(pasta_com_csvs)
