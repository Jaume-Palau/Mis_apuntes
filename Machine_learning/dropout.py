'''DESACTIVACION DE NEURANAS DE FORMA ALEATORIA PARA EVITAR EL OVERFITING DE LA RED'''

import numpy as np

class Capa_Dropout:

    def __init__(self, rate):
        # rate = porcentaje que quieres apagar
        # guardamos la parte que sí se mantiene
        self.rate = 1 - rate

    def forward(self, inputs):
        self.inputs = inputs

        # mascara aleatoria
        self.binary_mask = np.random.binomial(1, self.rate, size=inputs.shape) / self.rate

        # aplicar dropout
        self.output = inputs * self.binary_mask

    def backwards(self, dvalues):
        self.dinputs = dvalues * self.binary_mask