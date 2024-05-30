import sys
import os

# Añadir la ruta del proyecto al sistema de rutas de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller.controller import Controller
import tkinter as tk

def create_interface():
    window = tk.Tk()
    window.title("Sistema de Recomendación de Zapatos")

    def train_and_display():
        controller.train_perceptron()
        display_results()

    def display_results():
        result_text = controller.get_results()
        result_label.config(text=result_text)

    controller = Controller()

    # Entradas para las opiniones de 5 personas
    input_labels = []
    input_entries = []
    for i in range(5):
        label = tk.Label(window, text=f"Opinión Persona {i+1} (0 o 1):")
        label.pack()
        entry = tk.Entry(window)
        entry.pack()
        input_labels.append(label)
        input_entries.append(entry)

    def predict():
        inputs = [int(entry.get()) for entry in input_entries]
        print("Entradas:", inputs)  # Añadir esta línea para verificar las entradas
        recommendation = controller.predict(inputs)
        result_label.config(text=f"Recomendación: {'Comprar' if recommendation else 'No Comprar'}")

    predict_button = tk.Button(window, text="¿Debería comprar?", command=predict)
    predict_button.pack()

    train_button = tk.Button(window, text="Entrenar y Mostrar Resultados", command=train_and_display)
    train_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    window.mainloop()

if __name__ == "__main__":
    create_interface()
