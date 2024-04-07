import csv
from statistics import variance

def read_csv(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def calculate_variance(data):
    # Remove o cabeçalho
    header = data[0]
    data = data[1:]

    # Transpõe a matriz para que as colunas se tornem linhas
    data_transposed = list(zip(*data))

    # Calcula a variância para cada coluna
    variances = {}
    for i, col in enumerate(data_transposed):
        try:
            col = list(map(float, col))
            variances[header[i]] = variance(col)
        except ValueError:
            pass  # Ignora colunas que não podem ser convertidas para float

    return variances

def main():
    # Ler CSVs
    compilado = read_csv('compilado.csv')
    interpretado = read_csv('interpretado.csv')

    # Calcular variâncias
    var_compilado = calculate_variance(compilado)
    var_interpretado = calculate_variance(interpretado)

    # Exibir resultados
    print('Variância para linguagens compiladas:')
    for key, value in var_compilado.items():
        print(f'{key}: {value}')

    print('\nVariância para linguagens interpretadas:')
    for key, value in var_interpretado.items():
        print(f'{key}: {value}')

if __name__ == '__main__':
    main()
