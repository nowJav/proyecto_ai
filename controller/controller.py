from model.perceptron import Perceptron
from model.data import training_inputs, labels
from view.plots import plot_results

class Controller:
    def __init__(self):
        self.perceptron = Perceptron(input_size=2)

    def train_perceptron(self):
        self.perceptron.train(training_inputs, labels, epochs=10)

    def get_results(self):
        result_text = ""
        for inputs in training_inputs:
            result_text += f"Entradas {inputs} -> Recomendar: {self.perceptron.predict(inputs)}\n"
        plot_results(training_inputs, labels, self.perceptron)
        return result_text
