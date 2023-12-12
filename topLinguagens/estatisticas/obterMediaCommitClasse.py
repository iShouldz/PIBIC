"""Função script: Obter a quantidade media dos commits referentes a não familiar e familiar"""

import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN01')

def obter_tamanho_total_commits(username, repositorio, hash):
    user, repo = repositorio.split('/')[-2:]
    repositorio = repositorio.split('/')
    url = f'https://api.github.com/repos/{user}/{repo}/commits/{hash}'

    headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    print(url)

    if response.status_code == 200:
        commit_info = response.json()
        if 'stats' in commit_info:
            print(f'{user} tem {commit_info["stats"]["total"]} onde {url}')
            return commit_info['stats']['total']
        else:
            return None
        print('Não possui')
    else:
        print('404')
        return None

df = pd.read_csv('../csv/FINALSemNulos.csv')

df_familiar = df[df['Classificacao'] == 'NÃO FAMILIAR']
df_familiar['TamanhoTotalCommits'] = df_familiar.apply(
    lambda row: obter_tamanho_total_commits(row['username'], row['repositorio'], row['hash']), axis=1)

tamanho_medio_total_commits = df_familiar['TamanhoTotalCommits'].mean()

print(f'A média do tamanho total dos commits para linhas FAMILIAR é: {tamanho_medio_total_commits}')
