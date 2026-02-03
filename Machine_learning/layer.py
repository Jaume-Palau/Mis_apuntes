'''COMO CREAR UNA CAPA DE NEURONAS'''

import numpy as np

'''El input de la capa anterior viene de 4 neuronas'''

inputs = [1.5, 3, 2, 1.6]

'''Vamos a crear una capa de 3 neuronas'''

# En los pesos cada array representa una neurona
weights = [
    [0.2,0.8,-0.5,1], # 1 neurona con 4 pesos
    [0.5,-0.91,0.26,-0.5], # 1 neurona con 4 pesos
    [-0.26,-0.27,0.17,0.87] # 1 neurona con 4 pesos
]

bias = [2, 3, 0.5]

'''SALIDA'''
# weights = matriz    |   inputs = vector
# matriz(3x4) * vector(4,) -->  4columnas * vector(n=4) CORRECTO
layer_output = np.dot(weights,inputs) + bias
print(layer_output)



