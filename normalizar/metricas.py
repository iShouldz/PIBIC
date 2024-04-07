import pandas as pd
import numpy as np

# Carregar dados normalizados do CSV
dados_normalizados = pd.read_csv('normalizado.csv')

# Remover a primeira coluna (rótulos das linhas)
dados_normalizados = dados_normalizados.drop(dados_normalizados.columns[0], axis=1)

# Converter colunas numéricas para float
colunas_numericas = dados_normalizados.columns[1:-1]
dados_normalizados[colunas_numericas] = dados_normalizados[colunas_numericas].astype(float)

# Calcular Diferença Média Absoluta (DMA)
dma = np.mean(np.abs(dados_normalizados[colunas_numericas] - np.mean(dados_normalizados[colunas_numericas], axis=0)), axis=0)

# Calcular Variância
variancia = np.var(dados_normalizados[colunas_numericas], axis=0)

# Calcular Desvio Padrão
desvio_padrao = np.std(dados_normalizados[colunas_numericas], axis=0)

print("Diferença Média Absoluta (DMA): \n", dma)
print("Variância: \n", variancia)
print("Desvio Padrão: \n", desvio_padrao)

