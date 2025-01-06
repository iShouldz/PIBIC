import pandas as pd

# Função para classificar a linguagem como compilada ou executada
def obter_tipo_linguagem(linguagem):
    linguagens_compiladas = ["C#", "C++", "C", "CSS", "Go", "Haskell", "Java", "Rust", "TeX"]
    if linguagem in linguagens_compiladas:
        return "Compilada"
    else:
        return "Executada"

df = pd.read_csv('ALL.csv')

# Aplicar a função para classificar a linguagem
df['tipo_linguagem'] = df['programming_language'].apply(obter_tipo_linguagem)

# Filtrar os valores HIGH, LOW e NONE na coluna cvss3_integrity_impact
df_high = df[df['cvss3_integrity_impact'] == 'HIGH']
df_low = df[df['cvss3_integrity_impact'] == 'LOW']
df_none = df[df['cvss3_integrity_impact'] == 'NONE']

# Contar os valores HIGH por tipo de linguagem
contagem_high = df_high.groupby('tipo_linguagem').size().reset_index(name='count_high')

# Contar os valores LOW por tipo de linguagem
contagem_low = df_low.groupby('tipo_linguagem').size().reset_index(name='count_low')

# Contar os valores NONE por tipo de linguagem
contagem_none = df_none.groupby('tipo_linguagem').size().reset_index(name='count_none')

# Juntar as contagens em um único DataFrame
contagem_total = contagem_high.merge(contagem_low, on='tipo_linguagem', how='outer').merge(contagem_none, on='tipo_linguagem', how='outer')

# Preencher os valores NaN com 0
contagem_total = contagem_total.fillna(0)

print(contagem_total)
