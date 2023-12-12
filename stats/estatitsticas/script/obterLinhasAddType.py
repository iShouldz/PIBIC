"""Função script: Obtem a quantidade de linhas adicionadas para o tipo: linguagem compilada ou executada"""

import os
import pandas as pd

def obter_tipo_linguagem(linguagem):
    linguagens_compiladas = ["C#", "C++", "C", "Go", "Haskell", "Java", "Rust", "TeX"]

    if linguagem in linguagens_compiladas:
        return "Compilada"
    else:
        return "Executada"

def calcular_linhas_adicionadas_cvs(caminho_pasta):
    total_adicionadas_compiladas = 0
    total_adicionadas_executadas = 0

    for arquivo in os.listdir(caminho_pasta):
        if arquivo.endswith(".csv"):
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)

            df = pd.read_csv(caminho_arquivo)

            # Adicionar coluna 'TipoLinguagem' ao DataFrame
            df['TipoLinguagem'] = df['linguagem_programacao'].apply(obter_tipo_linguagem)

            total_adicionadas_compiladas += df[df['TipoLinguagem'] == 'Compilada']['LinhasAdicionadas'].sum()
            total_adicionadas_executadas += df[df['TipoLinguagem'] == 'Executada']['LinhasAdicionadas'].sum()

    return total_adicionadas_compiladas, total_adicionadas_executadas


caminho_da_sua_pasta = '../csvLinguage'
total_adicionadas_compiladas, total_adicionadas_executadas = calcular_linhas_adicionadas_cvs(caminho_da_sua_pasta)

print(f'Total de Linhas Adicionadas para Linguagens Compiladas: {total_adicionadas_compiladas}')
print(f'Total de Linhas Adicionadas para Linguagens Executadas: {total_adicionadas_executadas}')
