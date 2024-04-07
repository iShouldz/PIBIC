import pandas as pd

# Carregar o CSV original
df = pd.read_csv('normalizado2.csv')

# Definir listas vazias para armazenar as linhas de cada tipo
compiladas = []
interpretadas = []

# Iterar sobre as linhas do dataframe
for index, row in df.iterrows():
    linguagens_compiladas = ["C#", "C++", "C", "CSS", "Go", "Haskell", "Java",
                             "Rust", "TeX", "CoffeeScript", "JavaScript", ""]
    if row['Linguagem'] in linguagens_compiladas:
        compiladas.append(row)
    else:
        interpretadas.append(row)

# Converter as listas em dataframes
df_compiladas = pd.DataFrame(compiladas)
df_interpretadas = pd.DataFrame(interpretadas)

# Salvar os dataframes como arquivos CSV
df_compiladas.to_csv('linguagens_compiladas.csv', index=False)
df_interpretadas.to_csv('linguagens_interpretadas.csv', index=False)
