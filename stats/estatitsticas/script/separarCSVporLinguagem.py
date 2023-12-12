"""Função script: Gerar um arquivo csv para cada linguagem para facilitar o tratamento dos dados"""

import pandas as pd

df = pd.read_csv('../../csv/linguagemSemDupHashStatsLimpo.csv')

linguagens = df['linguagem_programacao'].unique()

for linguagem in linguagens:
    # Filtrar para obter apenas as linhas correspondentes à linguagem atual
    df_linguagem = df[df['linguagem_programacao'] == linguagem]

    nome_arquivo = f'{linguagem}_commits.csv'
    df_linguagem.to_csv(nome_arquivo, index=False)
    print(f'Arquivo {nome_arquivo} criado.')

print('Processo concluído.')
