"""Função script: Obter a quantidade de linhas referentes a não familiar e familiar"""

import pandas as pd

def contar_classificacoes(csv_path):
    df = pd.read_csv(csv_path)
    contagem_familiar = df[df['Classificacao'] == 'FAMILIAR'].shape[0]
    contagem_nulo = df[df['Classificacao'] == 'NÃO FAMILIAR'].shape[0]

    return contagem_familiar, contagem_nulo

caminho_csv = '../csv/FINALSemNulos.csv'
familiar, nulo = contar_classificacoes(caminho_csv)

print(f"Quantidade de linhas com 'LINGUAGEM FAMILIAR': {familiar}")
print(f"Quantidade de linhas com 'NÃO FAMILIAR': {nulo}")
