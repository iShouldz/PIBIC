import os

def contar_linhas_csv(diretorio):
    total_linhas = 0

    # Listar todos os arquivos no diretório
    arquivos = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.csv')]

    # Iterar sobre cada arquivo e contar as linhas
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(diretorio, arquivo)
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            linhas = sum(1 for linha in f)
            total_linhas += linhas
            print(f"{arquivo}: {linhas} linhas")

    print(f"\nTotal de linhas em todos os arquivos: {total_linhas}")

# Substitua 'caminho/do/seu/diretorio' pelo caminho real do seu diretório
diretorio_alvo = '../csvLinguage'
contar_linhas_csv(diretorio_alvo)
