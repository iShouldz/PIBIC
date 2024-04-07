"""Função script: Obter os stats das linhas do commit"""
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = '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'

def getLinhasTotais(repository_url, commit_hash):
    user, repo = repository_url.split('/')[-2:]
    api_url = f"https://api.github.com/repos/{user}/{repo}/commits/{commit_hash}"
    print(api_url)

    headers = {
        'Authorization': f'token {token}',
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        linhasTotais = data['stats']['total']
        linhasAdicionas = data['stats']['additions']
        linhasRemovidas = data['stats']['deletions']
        return linhasTotais, linhasAdicionas, linhasRemovidas
    else:
        print(f"Erro {response.status_code}")
    return None

def processar_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    df[['LinhasTotais', 'LinhasAdicionadas', 'LinhasRemovidas']] = df.apply(lambda row: pd.Series(getLinhasTotais(row['repositorio'], row['hash'])), axis=1)
    df.to_csv(output_csv, index=False)

input_csv_path = '../../utils/split/csv/CommitsUnicos.csv_2.csv'
output_csv_path = '../csv/statsPt2.csv'

processar_csv(input_csv_path, output_csv_path)


