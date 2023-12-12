"""Função script: Remover duplicatas e a hash origem de hash do csv"""

# import pandas as pd

# df = pd.read_csv('seu_arquivo_sem_duplicatas.csv')
#
# # Remover linhas duplicadas com base na coluna 'hash'
# df = df.drop_duplicates(subset=['hash'], keep=False)
#
# df.to_csv('linguagensCommitsUnicos.csv', index=False)

import pandas as pd

df = pd.read_csv('../csv/CommitsUnicosUnidos.csv')

# Remover linhas duplicadas com base na coluna 'hash'
df = df.drop_duplicates(subset=['hash'], keep='first')

df.to_csv('FINALcommitsUnicosSemDuplicatas.csv', index=False)
