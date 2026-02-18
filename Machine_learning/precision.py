'''NOS DA UN PORCENTAJE DE PRECISION DE ACIERTOS DE LA RED NEURONAL'''

import numpy as np

# Valores de salida
softmax_output = np.array(
    [
     [0.7,0.3],
     [0.55,0.45],
     [0.02,0.98]
     ]
)

# Valores esperados
y_verdadera = np.array([0,1,1])


# Extraer el indice maximo de cada salida
predicciones = np.argmax(softmax_output,axis=1) #predicciones = np.array([0,0,1])

if len(y_verdadera.shape) == 2:

    y_verdadera = np.argmax(y_verdadera,axis=1)

precision = np.mean(predicciones == y_verdadera)

print('PRECISION:',precision)

