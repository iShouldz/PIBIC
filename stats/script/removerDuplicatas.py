"""Função script: Remover duplicatas de hash do csv"""

import pandas as pd

caminho_arquivo = '../../topLinguagens/csv/linguagensTop3PerAuthor.csv'
df = pd.read_csv(caminho_arquivo)

# Remove as duplicatascom base no 'hash'
df_sem_duplicatas = df.drop_duplicates(subset='hash', keep='first')
df_sem_duplicatas.to_csv('../../topLinguagens/csv/linguagensTop3PerAuthorHU.csv', index=False)
