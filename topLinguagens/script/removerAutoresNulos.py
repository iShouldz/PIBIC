import pandas as pd

df2 = pd.read_csv('linhas_autor_nulo.csv')
df1 = pd.read_csv('../csv/FINALcommitsUnicosSemDuplicatas.csv')

# Remover linhas de df1 que estão em df2
df1 = df1[~df1.isin(df2.to_dict('list')).all(axis=1)]

df1.to_csv('FINALSemNulos.csv', index=False)
