# proyecto_ai
Proyecto de Curso Inteligencia Artificial - Perceptron Simple - Sistema de Recomendación - Python

# Sistema de Recomendación Básico con Perceptrón

## Descripción
Este proyecto implementa un sistema de recomendación básico utilizando un perceptrón simple. Se recomienda un producto basándose en si el usuario ha comprado antes y si ha visto el producto.

## Estructura del Proyecto
- `model/`: Contiene el modelo de perceptrón y los datos de entrenamiento.
  - `perceptron.py`: Define la clase Perceptrón.
  - `data.py`: Contiene los datos de entrenamiento.
- `view/`: Contiene la interfaz gráfica y la visualización de resultados.
  - `gui.py`: Define la interfaz gráfica con Tkinter.
  - `plots.py`: Maneja la visualización de resultados con Matplotlib.
- `controller/`: Controla la lógica de la aplicación.
  - `controller.py`: Interactúa con el modelo y actualiza la vista.
- `main.py`: Punto de entrada de la aplicación.

## Instalación
1. Clona este repositorio.
2. Instala las dependencias necesarias:
   ```bash
  - pip install numpy
  - pip install matplotlib 
  - pip install tkinter

# tomar en cuenta las versiones para el buen funcionamiento