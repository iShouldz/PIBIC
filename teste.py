import pandas as pd

# Carregue o arquivo CSV em um DataFrame do pandas
df = pd.read_csv('education.csv')

# Verifique se há duplicatas em todo o DataFrame
duplicatas = df.duplicated()

# Se houver duplicatas, elas serão marcadas como True na série duplicatas
# Você pode contar o número de duplicatas encontradas
num_duplicatas = duplicatas.sum()

if num_duplicatas > 0:
    print(f"A base de dados contém {num_duplicatas} registros duplicados.")
else:
    print("A base de dados não contém registros duplicados.")