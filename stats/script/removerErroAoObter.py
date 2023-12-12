"""Função script: Remove do CSV o username 'erro ao obter' que indica erro"""

import pandas as pd

caminho_arquivo = '../csv/linguagemSemDupHashStats.csv'
df = pd.read_csv(caminho_arquivo)

# Remova as linhas onde 'username' é igual a 'error ao obter'
df_filtrado = df[df['username'] != 'error ao obter']

df_filtrado.to_csv('../csv/linguagemSemDupHashStatsLimpo.csv', index=False)
