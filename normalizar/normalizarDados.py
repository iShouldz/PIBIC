import pandas as pd

# Ler o CSV
df = pd.read_csv('../csvGeral/linguagens-para-normalizar.csv')

# Normalizar métricas pela ocorrência da linguagem
df['Media_linhas_totais_normalizada'] = df['Media linhas totais'] * df['Ocorrencia'] / df['Ocorrencia'].sum()
df['Mediana_linhas_totais_normalizada'] = df['Mediana linhas totais'] * df['Ocorrencia'] / df['Ocorrencia'].sum()
df['Primeiro_quartil_normalizado'] = df['Primeiro Quartil Total'] * df['Ocorrencia'] / df['Ocorrencia'].sum()
df['Terceiro_quartil_normalizado'] = df['Terceiro Quartil Total'] * df['Ocorrencia'] / df['Ocorrencia'].sum()
df['Media_adicionadas_normalizada'] = df['Média Adicionadas'] * df['Ocorrencia'] / df['Ocorrencia'].sum()
df['Mediana_adicionadas_normalizada'] = df['Mediana Adicionadas'] * df['Ocorrencia'] / df['Ocorrencia'].sum()
df['Primeiro_quartil_adicionadas_normalizado'] = df['Primeiro Quartil Adicionadas'] * df['Ocorrencia'] / df['Ocorrencia'].sum()
df['Terceiro_quartil_adicionadas_normalizado'] = df['Terceiro Quartil Adicionadas'] * df['Ocorrencia'] / df['Ocorrencia'].sum()
df['Media_removidas_normalizada'] = df['Media Removidas'] * df['Ocorrencia'] / df['Ocorrencia'].sum()
df['Mediana_removidas_normalizada'] = df['Mediana Removidas'] * df['Ocorrencia'] / df['Ocorrencia'].sum()
df['Primeiro_quartil_removidas_normalizado'] = df['Primeiro Quartil Removidas'] * df['Ocorrencia'] / df['Ocorrencia'].sum()
df['Terceiro_quartil_removidas_normalizado'] = df['Terceiro Quartil Removidas'] * df['Ocorrencia'] / df['Ocorrencia'].sum()
df['Media_ajustada_normalizada'] = df['MEDIA AJUSTADA'] * df['Ocorrencia'] / df['Ocorrencia'].sum()

# Salvar o DataFrame modificado de volta ao CSV
df.to_csv('normalizado.csv', index=False)
