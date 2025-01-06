import pandas as pd

df = pd.read_csv('ALL.csv')
def categorizar_impacto(score):
    if score >= 1.4 and score <= 3:
        return 'Baixo'
    elif score > 3 and score <= 4.5:
        return 'Médio'
    elif score > 4.5 and score <= 6:
        return 'Alto'
    else:
        return 'Desconhecido'

def obter_tipo_linguagem(linguagem):
    linguagens_compiladas = ["C#", "C++", "C", "CSS", "Go", "Haskell", "Java", "Rust", "TeX"]
    if linguagem in linguagens_compiladas:
        return "Compilada"
    else:
        return "Interpretada"

# Aplicar a função para categorizar o impacto_score
df['impacto_categoria'] = df['impact_score'].apply(categorizar_impacto)

# Aplicar a função para classificar a linguagem
df['tipo_linguagem'] = df['programming_language'].apply(obter_tipo_linguagem)

# Contar as ocorrências de cada categoria de impacto por tipo de linguagem
contagem_impacto = df.groupby(['tipo_linguagem', 'impacto_categoria']).size().reset_index(name='Quantidade')

print(contagem_impacto)
