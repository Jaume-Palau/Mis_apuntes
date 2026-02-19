'''Softmax:
- Convierte un vector de logits en probabilidades.
- Las probabilidades suman 1.
- Las clases compiten entre sí.
- Se usa en clasificación multiclase exclusiva.'''

import numpy as np
import matplotlib.pyplot as plt
from network_loss import Loss_CategoriclalCrossEntropy


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


class Activation_Softmax_Loss_CategoricalCrossentropy():

    def __init__(self):

        self.activation = Activation_softmax()
        self.loss = Loss_CategoriclalCrossEntropy()

    def forward(self,inputs,y_true):

        # Funcion de activacion de la capa de salida
        self.activation.forward(inputs)

        # Fijamos el output como el resultado de la funcion de activacion
        self.output = self.activation.output

        # Calculamos y devolvemos el valor de perdida
        return self.loss.calculate(self.output,y_true)
    
    def backwards(self,dvalues,y_true):

        # Numero de muestras
        muestras = len(dvalues)

        # Transormar los valores de one-hot a indices
        if len(y_true.shape) == 2:
            y_true = np.argmax(y_true, axis=1)

        # Copiar los valores para porder actualizarlos sin modificar los previos
        self.dinputs = dvalues.copy()

        # Calculamos el gradiente
        self.dinputs[range(muestras),y_true] -= 1

        # Normalizamos el gradiente
        self.dinputs = self.dinputs / muestras