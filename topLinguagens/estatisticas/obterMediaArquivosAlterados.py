import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN02')

df = pd.read_csv('../csv/FINALcommitsUnicosSemDuplicatas.csv')

df['arquivos_modificados'] = 0

for index, row in df.iterrows():
    user, repo = row["repositorio"].split('/')[-2:]
    url = f'https://api.github.com/repos/{user}/{repo}/commits/{row["hash"]}'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    print(url)

    if response.status_code == 200:
        commit_data = response.json()
        # Adicionar a quantidade de arquivos modificados
        df.at[index, 'arquivos_modificados'] = len(commit_data['files'])
        print(len(commit_data['files']))
    else:
        print(f'Erro ao obter dados para o commit {row["hash"]}: {response.status_code}')

media_arquivos_modificados = df.groupby('Classificacao')['arquivos_modificados'].mean()

print(f'Média de arquivos modificados por autores FAMILIAR: {media_arquivos_modificados["FAMILIAR"]:.2f}')
print(f'Média de arquivos modificados por autores NÃO FAMILIAR: {media_arquivos_modificados["NÃO FAMILIAR"]:.2f}')
