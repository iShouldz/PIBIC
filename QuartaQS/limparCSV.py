import pandas as pd

# Ler os dois arquivos CSV
df1 = pd.read_csv('CommitsTodasLinguagens.csv')
df2 = pd.read_csv('listagem commits.csv')

# Filtrar df1 para manter apenas as linhas cujos hashes estão em df2
df_resultado = df1[df1['hash'].isin(df2['hash'])]

# Remover duplicatas baseadas na coluna 'hash'
df_resultado = df_resultado.drop_duplicates(subset=['hash'])

# Salvar o resultado em um novo arquivo CSV
df_resultado.to_csv('ALL.csv', index=False)

print("Linhas filtradas e sem duplicatas salvas em 'primeiro_arquivo_filtrado_sem_duplicatas.csv'")
