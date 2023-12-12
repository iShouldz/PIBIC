import pandas as pd
import requests
from datetime import datetime

df = pd.read_csv('../csv/FINALSemNulos.csv')

# Filtrar linhas classificadas como 'NÃO FAMILIAR'
df_nao_familiar = df[df['Classificacao'] == 'NÃO FAMILIAR']
token = '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'

# Função para obter o tempo de criação do GitHub do autor
def obter_tempo_criacao(username):
    url = f'https://api.github.com/users/{username}'
    headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        created_at = data['created_at']
        print(created_at)
        return created_at
    else:
        return None

# Aplicar a função para obter o tempo de criação
df_nao_familiar['tempo_criacao'] = df_nao_familiar['username'].apply(obter_tempo_criacao)

df_nao_familiar['tempo_criacao'] = pd.to_datetime(df_nao_familiar['tempo_criacao'])
df_nao_familiar.to_csv('criacaoNãoFamiliar.csv', index=False)
