import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.learning_rate = learning_rate
        self.weights = np.random.uniform(-0.5, 0.5, size=input_size + 1)  # +1 for bias

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return 1 if summation > 0 else 0

    def train(self, training_inputs, labels, epochs):
        for epoch in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)
                print("Predicción:", prediction)
            print("Pesos después del epoch", epoch + 1, ":", self.weights)
