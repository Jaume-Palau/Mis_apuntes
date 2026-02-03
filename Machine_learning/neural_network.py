
## Clase 2 min 35
import numpy as np


class Capa_densa:
    # Inicializacion de la capa

    def __init__(self,n_neuronas,n_inputs):

        # inicio los pesos aleatorios
        self.weights = 0.01 * np.random.rand(n_inputs,n_neuronas)

        # inicio los sesgos de la capa en 0
        self.bias = np.zeros((1,n_neuronas))


    def forward(self, inputs):

        self.output = np.dot(inputs,self.weights) + self.bias  

capa1 = Capa_densa(4,3)
print(capa1.weights)
print(capa1.bias)