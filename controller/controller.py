import numpy as np
from model.perceptron import Perceptron
from model.data import training_inputs, labels
from view.plots import plot_results

class Controller:
    def __init__(self):
        self.perceptron = Perceptron(input_size=5)  # 5 entradas

    def train_perceptron(self):
        print("Datos de entrenamiento:")
        print("Entradas:", training_inputs)
        print("Etiquetas:", labels)
        print("Pesos después del entrenamiento:", self.perceptron.weights)
        self.perceptron.train(training_inputs, labels, epochs=10)

    def get_results(self):
        result_text = ""
        for inputs in training_inputs:
            result_text += f"Entradas {inputs} -> Recomendar: {self.perceptron.predict(inputs)}\n"
        plot_results(training_inputs, labels, self.perceptron)
        return result_text

    def predict(self, inputs):
        print("Entradas para la predicción:", inputs)
        return self.perceptron.predict(np.array(inputs))

