''' EN ESTE ARCHIVO ESTAN LAS DISTINTAS FUNCIONES DE ACTIVACION QUE SE UTILIZAN'''
import numpy as np

def step_func(inputs):

    '''Devuelve una salida binaria segun un umbral
    Sirve para decisiones simples; no es diferenciable.
    '''

    output = []

    for i in inputs:
        if i > 0:
            output.append(1)
        else:
            output.append(0)

    return output


def lineal_func(inputs): # y = m*x + b

    '''Transforma la entrada con una recta
    No introduce no-linealidad; varias funciones lineales seguidas equivalen a una sola.
    '''

    m = 1 # pendiente
    b = 0 # sesgo

    output = []

    for x in inputs:
        y = m*x +b
        output.append(y)
    
    return output


def sigmoide_func(inputs): # r = 1 / (1+np.e**(-x))

    '''Comprime los valores en un rango entre 0 y 1
    Se usa para interpretar salidas como probabilidades.
    '''

    output = []

    for x in inputs: 
        r = 1 / (1+np.e**(-x))
        output.append(r)

    return output


def ReLu_simplificada_func(inputs):

    '''Función de activación que devuelve el valor de entrada si es positivo y 0 si es negativo;
    introduce no linealidad y evita saturación en valores positivos.
    '''

    output = []

    for i in inputs:
        if i > 0:
            output.append(i)
        else:
            output.append(0)

    return output


class Activation_ReLu:

    def forward(self,inputs):
        # Maximum compara cada uno de los valores con un 0 y devuelve el mayor 
        # como en la funcion anterior, relu simplificada 
        self.output = np.maximum(0,inputs)

        return self.output
