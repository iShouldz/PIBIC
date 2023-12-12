"""Função script: Obter a quantidade de duplicatas"""

# import pandas as pd
#
# df = pd.read_csv('../csv/CommitsUnicosUnidos.csv')
#
# # Verificar duplicatas com base na coluna 'hash'
# duplicatas = df[df.duplicated(subset='hash', keep=False)]
#
# print("Linhas duplicadas:")
# print(duplicatas)
#
# duplicatas.to_csv('duplicatas.csv', index=False)
import pandas as pd

df = pd.read_csv('../csv/FINALcommitsUnicosSemDuplicatas.csv')

# Filtrar linhas com username igual a 'autor nulo'
linhas_autor_nulo = df[df['username'] == 'autor nulo']

linhas_autor_nulo.to_csv('linhas_autor_nulo.csv', index=False)
