"""Função script: Splitar csv"""
import pandas as pd

def split_csv(input_file, chunk_size, output_prefix):
    df = pd.read_csv(input_file)

    chunks = [df[i:i + chunk_size] for i in range(0, df.shape[0], chunk_size)]
    for i, chunk in enumerate(chunks):
        output_file = f"{output_prefix}_{i + 1}.csv"
        chunk.to_csv(output_file, index=False)
        print(f"Arquivo {output_file} criado com sucesso.")

input_csv = '../../../topLinguagens/csv/commitsUnicos.csv'
chunk_size = 3000
output_prefix = '../csv/CommitsUnicos.csv'

split_csv(input_csv, chunk_size, output_prefix)
