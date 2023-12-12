import pandas as pd

df_top3 = pd.read_csv('../csv/linguagensTop3PerAuthorHU.csv')

# Separar linguagens familiares e não familiares
df_familiares = df_top3[df_top3['Classificacao'] == 'LINGUAGEM FAMILIAR']
df_nao_familiares = df_top3[df_top3['Classificacao'] == 'LINGUAGEM NÃO FAMILIAR']

df_familiares.to_csv('linguagens_familiares.csv', index=False)
df_nao_familiares.to_csv('linguagens_nao_familiares.csv', index=False)