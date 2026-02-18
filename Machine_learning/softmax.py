'''Softmax:
- Convierte un vector de logits en probabilidades.
- Las probabilidades suman 1.
- Las clases compiten entre sí.
- Se usa en clasificación multiclase exclusiva.'''

import numpy as np
import matplotlib.pyplot as plt

class Activation_softmax:

    def forward(self,inputs):
        # Recordar los inputs para la optimizacion
        self.inputs = inputs
        # Calculo los valores exponenciales restandoles el valor maximo
        exp_values = np.exp(inputs-np.max(inputs, axis=1, keepdims=True))
        # Normaliza las probabilidades
        probabilidades = exp_values /np.sum(exp_values, axis=1, keepdims=True)

        self.output = probabilidades

        return self.output
    
    def backward(self,dvalues):

        #Creoun array vacio de las mismas dimensiones que el de entrada
        self.dinputs = np.empty_like(dvalues)
        
        for index,(single_output,single_values) in enumerate(zip(self.output,dvalues)):

            # Para operar con la fila debemos "aplanarlo"
            single_output = single_output.reshape(-1,1)

            # Calculamos la matriz jacobiana del output
            matrix_jacobiana = np.diagflat(single_output) - np.dot(single_output, single_output.T)

            # Calculamos el gradiente del output
            self.dinputs[index] = np.dot(matrix_jacobiana, single_values)

