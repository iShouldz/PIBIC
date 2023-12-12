import pandas as pd
from datetime import datetime, timedelta, timezone

df = pd.read_csv('../csv/criacaoNãoFamiliar.csv')

data_atual = datetime.now(timezone.utc)
inexperiente = []
experiente = []

for index, row in df.iterrows():
    tempo_criacao = pd.to_datetime(row['tempo_criacao'])
    diferenca_anos = (data_atual - tempo_criacao).days // 365

    if diferenca_anos < 4:
        inexperiente.append(index)
    else:
        experiente.append(index)

print(f"Quantidade de inexperientes: {len(inexperiente)}")
print(f"Quantidade de experientes: {len(experiente)}")