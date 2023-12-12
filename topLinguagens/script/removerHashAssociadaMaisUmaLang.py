import pandas as pd

df = pd.read_csv('../../csvGeral/ListagemUsernames.csv')

# Verificar se há hashes com mais de uma linguagem associada
hashes_com_mais_de_uma_linguagem = df.groupby('hash')['linguagem_programacao'].nunique()
hashes_com_mais_de_uma_linguagem = hashes_com_mais_de_uma_linguagem[hashes_com_mais_de_uma_linguagem > 1].index

# Filtrar as linhas em que a hash não tem mais de uma linguagem associada
df_resultado = df[~df['hash'].isin(hashes_com_mais_de_uma_linguagem)]

df_resultado.to_csv('seu_arquivo_sem_duplicatas.csv', index=False)
