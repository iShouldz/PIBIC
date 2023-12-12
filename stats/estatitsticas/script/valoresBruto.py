"""Função script: Obtem os valores brutos de quantidade de linhas"""

import os
import pandas as pd

def calcular_totais(diretorio):
    total_linhas = 0
    total_linhas_adicionadas = 0
    total_linhas_removidas = 0

    # Listar todos os arquivos no diretório
    arquivos = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.csv')]

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(diretorio, arquivo)
        df = pd.read_csv(caminho_arquivo)

        total_linhas += df['LinhasTotais'].sum()
        total_linhas_adicionadas += df['LinhasAdicionadas'].sum()
        total_linhas_removidas += df['LinhasRemovidas'].sum()

    print(f"Total de Linhas Totais: {total_linhas}")
    print(f"Total de Linhas Adicionadas: {total_linhas_adicionadas}")
    print(f"Total de Linhas Removidas: {total_linhas_removidas}")

diretorio_alvo = '../csvLinguage'
calcular_totais(diretorio_alvo)
