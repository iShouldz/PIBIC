"""Função script: Obter o top 3 linguagens para classe não familiar e familiar"""

import pandas as pd

df = pd.read_csv('../csv/FINALSemNulos.csv')

df_familiar = df[df['Classificacao'] == 'FAMILIAR']
top3_familiar = df_familiar['linguagem_programacao'].value_counts().head(3)
print(f'Top 3 linguagens de programação para linhas FAMILIAR:\n{top3_familiar}')

df_nao_familiar = df[df['Classificacao'] == 'NÃO FAMILIAR']
top3_nao_familiar = df_nao_familiar['linguagem_programacao'].value_counts().head(3)
print(f'Top 3 linguagens de programação para linhas NÃO FAMILIAR:\n{top3_nao_familiar}')
