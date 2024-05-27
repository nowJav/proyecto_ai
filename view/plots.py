import numpy as np
import matplotlib.pyplot as plt

def plot_results(inputs, labels, perceptron):
    x = np.array([inputs[:, 0]])
    y = np.array([inputs[:, 1]])
    plt.scatter(x, y, c=labels, cmap='bwr')
    plt.xlabel('Ha Comprado Antes')
    plt.ylabel('Ha Visto el Producto')
    plt.title('Recomendación de Producto')
    plt.show()
