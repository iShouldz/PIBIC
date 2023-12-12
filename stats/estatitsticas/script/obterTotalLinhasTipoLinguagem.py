"""Função script: Obtem quantidade de linhas para cada tipo de linguagem"""

import os
import pandas as pd

def obter_tipo_linguagem(linguagem):
    linguagens_compiladas = ["C#", "C++", "C", "CSS", "Go", "Haskell", "Java", "Rust", "TeX"]
    return "Compilada" if linguagem in linguagens_compiladas else "Executada"

def calcular_totais_por_tipo(diretorio):
    total_compiladas = 0
    total_executadas = 0

    arquivos = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.csv')]

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(diretorio, arquivo)
        df = pd.read_csv(caminho_arquivo)

        df['Tipo'] = df['linguagem_programacao'].apply(obter_tipo_linguagem)

        total_compiladas += df[df['Tipo'] == 'Compilada'].shape[0]
        total_executadas += df[df['Tipo'] == 'Executada'].shape[0]

    print(f"Total de Linhas de Linguagens Compiladas: {total_compiladas}")
    print(f"Total de Linhas de Linguagens Executadas: {total_executadas}")

diretorio_alvo = '../csvLinguage'
calcular_totais_por_tipo(diretorio_alvo)
