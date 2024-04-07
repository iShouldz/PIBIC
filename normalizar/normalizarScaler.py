import pandas as pd
from sklearn.preprocessing import StandardScaler

# Ler o CSV
df = pd.read_csv('../csvGeral/linguagens-para-normalizar.csv')

# Selecionar as colunas que serão normalizadas
colunas_para_normalizar = ['Media linhas totais', 'Mediana linhas totais', 'Primeiro Quartil Total', 'Terceiro Quartil Total',
                           'Média Adicionadas', 'Mediana Adicionadas', 'Primeiro Quartil Adicionadas',
                           'Terceiro Quartil Adicionadas', 'Media Removidas', 'Mediana Removidas',
                           'Primeiro Quartil Removidas', 'Terceiro Quartil Removidas', 'MEDIA AJUSTADA', 'Ocorrencia']

# Normalizar os dados usando StandardScaler
scaler = StandardScaler()
df[colunas_para_normalizar] = scaler.fit_transform(df[colunas_para_normalizar])

# Salvar o DataFrame modificado de volta ao CSV
df.to_csv('normalizado2.csv', index=False)
