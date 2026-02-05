'''Softmax transforma un conjunto de puntuaciones en probabilidades, 
asignando mayor peso a los valores más altos y normalizando el resultado para que la suma sea 1.'''

import numpy as np
import matplotlib.pyplot as plt

class Activation_softmax:

    def forward(self,inputs):
        # Calculo los valores exponenciales restandoles el valor maximo
        exp_values = np.exp(inputs-np.max(inputs, axis=1, keepdims=True))
        # Normaliza las probabilidades
        probabilidades = exp_values /np.sum(exp_values, axis=1, keepdims=True)

        self.output = probabilidades

        return self.output

