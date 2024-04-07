import pandas as pd

# Carregando os dados dos CSVs
compilado = pd.read_csv('compilado.csv').iloc[:, 1:]
interpretado = pd.read_csv('interpretado.csv').iloc[:, 1:]

# Calculando a média de cada conjunto de dados
media_compilado = compilado.mean()
media_interpretado = interpretado.mean()

# Calculando a diferença absoluta entre cada valor e a média do respectivo conjunto
diferencas_absolutas_compilado = compilado.sub(media_compilado).abs()
diferencas_absolutas_interpretado = interpretado.sub(media_interpretado).abs()

# Calculando a média das diferenças absolutas
DMA_compilado = diferencas_absolutas_compilado.mean()
DMA_interpretado = diferencas_absolutas_interpretado.mean()

print("Diferença Média Absoluta para compilado:", DMA_compilado)
print("Diferença Média Absoluta para interpretado:", DMA_interpretado)
