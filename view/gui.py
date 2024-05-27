import sys
import os

# Añadir la ruta del proyecto al sistema de rutas de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller.controller import Controller
import tkinter as tk

def create_interface():
    window = tk.Tk()
    window.title("Sistema de Recomendación")

    def train_and_display():
        controller.train_perceptron()
        display_results()

    def display_results():
        result_text = controller.get_results()
        result_label.config(text=result_text)

    controller = Controller()

    train_button = tk.Button(window, text="Entrenar y Mostrar Resultados", command=train_and_display)
    train_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    window.mainloop()

if __name__ == "__main__":
    create_interface()
