import pandas as pd

# Carregando os dados dos CSVs
compilado = pd.read_csv('compilado.csv').iloc[:, 1:]
interpretado = pd.read_csv('interpretado.csv').iloc[:, 1:]

# Calculando a média de cada coluna
media_compilado = compilado.mean()
media_interpretado = interpretado.mean()

# Calculando a diferença absoluta entre cada valor e a média do respectivo conjunto
diferencas_absolutas_compilado = compilado.sub(media_compilado).abs()
diferencas_absolutas_interpretado = interpretado.sub(media_interpretado).abs()

# Calculando a média das diferenças absolutas para cada coluna
DMA_compilado_por_coluna = diferencas_absolutas_compilado.mean(axis=0)
DMA_interpretado_por_coluna = diferencas_absolutas_interpretado.mean(axis=0)

# Calculando a média das médias das diferenças absolutas para cada conjunto
DMA_media_compilado = DMA_compilado_por_coluna.mean()
DMA_media_interpretado = DMA_interpretado_por_coluna.mean()

print("Diferença Média Absoluta para compilado:", DMA_media_compilado)
print("Diferença Média Absoluta para interpretado:", DMA_media_interpretado)
