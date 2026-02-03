'''COMO CREAR UNA NEURONA'''

import numpy as np

# w = weigh / peso
# b = bias / sesgo
# neurona = w * input + w * input w * input + b

# Los inputs seran una lista
inputs = [1.5, 3, 2, 1.6]

# n weights = n inputs
weights = [0.5, -0.3, 0.5, 1]

bias = 1.05


def neurona(inputs,weights,bias):
    '''Forma mas basica de programar una neurona para entender su funcionamiento'''
    # utilizamos la formula de la neurona
    output = (
        weights[0] * inputs[0] +
        weights[1] * inputs[1] +
        weights[2] * inputs[2] +
        weights[3] * inputs[3] + bias
    )
    print(output)


'''PARA NO TENER QUE INTRODUCIR TODOS LOS DATOS UNO POR UNO COMO EN EL CASO ANTERIOR UTILIZAMOS NUMPY'''
def neurona_numpy(weights,inputs,bias):
    # Es sumamente importante el orden de los vectores
    output = np.dot(weights,inputs) + bias
    print(output)

# Creacion del vector:
a = np.array([1,2,3]) # pesos
b = np.array([4,5,6]) # inputs


# Creacion de matrices
A = np.array([[5,6], 
              [7,8], 
              [4,3]]) # 3filas 2columnas 3x2

B = np.array([[1,2], 
              [3,4]]) # 2fials 2columnas 2x2

'''Para poder multiplicar dos matrices, el numero de columnas de la primera,
debe ser igual al numero de filas de la segunda'''

# Correcto
producto_matrix = np.dot(A,B)
print(producto_matrix)

# Error
producto_matrix = np.dot(B,A)
print(producto_matrix)




