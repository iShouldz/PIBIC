import pandas as pd

def obter_tipo_linguagem(linguagem):
    linguagens_compiladas = ["C#", "C++", "C", "CSS", "Go", "Haskell", "Java", "Rust", "TeX"]
    if linguagem in linguagens_compiladas:
        return "Compilada"
    else:
        return "Executada"

df = pd.read_csv('ALL.csv')

df['tipo_linguagem'] = df['programming_language'].apply(obter_tipo_linguagem)

# Filtrar as severidades HIGH, LOW e MEDIUM
df_high = df[df['severity'] == 'HIGH']
df_low = df[df['severity'] == 'LOW']
df_medium = df[df['severity'] == 'MEDIUM']

contagem_high = df_high.groupby('tipo_linguagem').size().reset_index(name='count_high')
contagem_low = df_low.groupby('tipo_linguagem').size().reset_index(name='count_low')
contagem_medium = df_medium.groupby('tipo_linguagem').size().reset_index(name='count_medium')
contagem_total = contagem_high.merge(contagem_low, on='tipo_linguagem', how='outer').merge(contagem_medium, on='tipo_linguagem', how='outer')

contagem_total = contagem_total.fillna(0)

print(contagem_total)
