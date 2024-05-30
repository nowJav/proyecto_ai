import numpy as np

# Datos de entrenamiento: combinaciones de opiniones de 5 personas (0 = no recomienda, 1 = recomienda)
training_inputs = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    # Añade más combinaciones según sea necesario
])

# Etiquetas (salidas) esperadas: 0 = no comprar, 1 = comprar
labels = np.array([0, 0, 0, 0, 0, 1, 1])
