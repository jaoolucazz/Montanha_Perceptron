def perceptron_input(inputs, weights, bias):
    """
    Calcula a entrada do perceptron.
    
    :param inputs: Lista de valores de entrada
    :param weights: Lista de pesos correspondentes às entradas
    :param bias: Valor do bias
    :return: Resultado da soma ponderada das entradas mais o bias
    """
    weighted_sum = sum(i * w for i, w in zip(inputs, weights))
    return weighted_sum + bias


def perceptron_output(inputs, weights, bias):
    """
    Calcula a saída do perceptron.
    
    :param inputs: Lista de valores de entrada
    :param weights: Lista de pesos correspondentes às entradas
    :param bias: Valor do bias
    :return: Saída do perceptron (0 ou 1)
    """
    return 1 if perceptron_input(inputs, weights, bias) >= 0 else 0


def main():
    print("Hello, World!")
    print("This is the main file.")
    
    inputs = [1, 2, 3]
    weights = [0.1, 0.2, 0.3]
    bias = 0.4
    
    print("The result of the perceptron input is:", perceptron_input(inputs, weights, bias))
    print("The result of the perceptron output is:", perceptron_output(inputs, weights, bias))


if __name__ == "__main__":
    main()
