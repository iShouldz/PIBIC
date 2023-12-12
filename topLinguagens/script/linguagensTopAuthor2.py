import time

import pandas as pd
import requests

import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN02')

def obter_linguagens_mais_utilizadas(username):
    url = f'https://api.github.com/users/{username[1]}/repos'
    headers = {'Accept': 'application/vnd.github.v3+json', 'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    print(url)
    if response.status_code == 200:
        repositorios = response.json()

        linguagens = {}
        for repositorio in repositorios:
            stats_url = f'https://api.github.com/repos/{username[1]}/{repositorio["name"]}/languages'
            stats_response = requests.get(stats_url, headers=headers)
            print(stats_url)

            x = stats_response.headers.get('x-ratelimit-remaining')
            print(int(x))
            y = response.headers.get('x-ratelimit-remaining')
            print("API = RESTA: " + str(x) + "/" + str(y))
            if x == '50' or y == '50':
                print("Recarregando API = RESTA: " + str(stats_response.headers.get('x-ratelimit-remaining')))
                """Recarregar API"""
                time.sleep(1800)
                print("APOS RECARGA DE 30 MINUTOS: " + str(stats_response.headers.get('x-ratelimit-remaining')))

            if stats_response.status_code == 200:
                stats = stats_response.json()
                for linguagem, contagem in stats.items():
                    linguagens[linguagem] = linguagens.get(linguagem, 0) + contagem
        linguagens_mais_utilizadas = sorted(linguagens.items(), key=lambda x: x[1], reverse=True)[:3]

        return linguagens_mais_utilizadas
    else:
        print(f'Erro ao obter repositórios. Código de resposta: {response.status_code}')
        return None

def verificar_linguagem(usuario, linguagem):
    linguagens_mais_utilizadas = obter_linguagens_mais_utilizadas(usuario)
    print(linguagens_mais_utilizadas)

    if linguagens_mais_utilizadas is not None:
        return linguagem in [lang[0] for lang in linguagens_mais_utilizadas]
    else:
        return False


def processar_csv(input_csv):
    df = pd.read_csv(input_csv)

    df['Classificacao'] = df.apply(
        lambda row: 'FAMILIAR' if verificar_linguagem((row['repositorio'], row['username'], row['hash']), row['linguagem_programacao']) else 'NÃO FAMILIAR', axis=1)

    df.to_csv('../csv/restanteParte2.csv', index=False)

input_csv_path = 'parte2.csv'
processar_csv(input_csv_path)

