"""Função script: Obtem dados com base no tipo: linguagem compilada ou executada"""

import os
import pandas as pd

def obter_tipo_linguagem(linguagem):
    linguagens_compiladas = ["C#", "C++", "C", "CSS", "Go", "Haskell", "Java", "Rust", "TeX"]
    if linguagem in linguagens_compiladas:
        return "Compilada"
    else:
        return "Executada"

def obter_estatisticas_gerais(csv_path):
    df = pd.read_csv(csv_path)

    # Adicionar uma coluna para o tipo de linguagem
    df['TipoLinguagem'] = df['linguagem_programacao'].apply(obter_tipo_linguagem)
    return df

pasta_com_csvs = '../csvLinguage'

# Inicializar DataFrames para armazenar dados compilados e executados
df_compiladas = pd.DataFrame()
df_executadas = pd.DataFrame()

for arquivo in os.listdir(pasta_com_csvs):
    if arquivo.endswith('.csv'):
        caminho_arquivo = os.path.join(pasta_com_csvs, arquivo)
        df = obter_estatisticas_gerais(caminho_arquivo)

        # Dividir entre compiladas e executadas
        df_compiladas = pd.concat([df_compiladas, df[df['TipoLinguagem'] == 'Compilada']])
        df_executadas = pd.concat([df_executadas, df[df['TipoLinguagem'] == 'Executada']])

media_geral_compiladas = df_compiladas.agg({
    'LinhasTotais': 'mean',
    'LinhasAdicionadas': 'mean',
    'LinhasRemovidas': 'mean',
}).reset_index()

media_geral_executadas = df_executadas.agg({
    'LinhasTotais': 'mean',
    'LinhasAdicionadas': 'mean',
    'LinhasRemovidas': 'mean',
}).reset_index()

media_geral_compiladas['TipoLinguagem'] = 'Compilada'
media_geral_executadas['TipoLinguagem'] = 'Executada'

print(f'\nMédia geral para linguagens compiladas:')
print(media_geral_compiladas)

print(f'\nMédia geral para linguagens executadas:')
print(media_geral_executadas)
