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

    # Combina todos os valores em uma única lista
    all_values = []
    for col in data_transposed:
        try:
            col = list(map(float, col))
            all_values.extend(col)
        except ValueError:
            pass  # Ignora colunas que não podem ser convertidas para float

    # Calcula a variância para todos os valores
    var_all = variance(all_values)

    return var_all

def main():
    # Ler CSVs
    compilado = read_csv('compilado.csv')
    interpretado = read_csv('interpretado.csv')

    # Calcular variâncias
    var_compilado = calculate_variance(compilado)
    var_interpretado = calculate_variance(interpretado)

    # Exibir resultados
    print('Variância para linguagens compiladas:')
    print(f'{var_compilado}')

    print('\nVariância para linguagens interpretadas:')
    print(f'{var_interpretado}')

if __name__ == '__main__':
    main()
