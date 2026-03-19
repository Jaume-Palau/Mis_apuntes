'''COMO CONECTAR LAS CAPAS ENTRE SÍ'''

import numpy as np

class Capa_densa:
    # Inicializacion de la capa

    def __init__(self,n_inputs,n_neuronas,weight_regularizer_l1 = 0,weight_regularizer_l2 = 0,bias_regularizer_l1 = 0,bias_regularizer_l2 = 0):

        # inicio los pesos aleatorios
        self.weights = 0.01 * np.random.randn(n_inputs,n_neuronas)

        # inicio los sesgos de la capa en 0
        self.bias = np.zeros((1,n_neuronas))

        self.weight_regularizer_l1 = weight_regularizer_l1
        self.weight_regularizer_l2 = weight_regularizer_l2
        self.bias_regularizer_l1 = bias_regularizer_l1
        self.bias_regularizer_l2 = bias_regularizer_l2


    def forward(self, inputs):
        # Calcula los outputs de la capa a traves del producto escalar
        self.output = np.dot(inputs,self.weights) + self.bias  
        # Recordar los inputs para el backpropagation
        self.inputs = inputs

        return self.output
    

def backwards(self,dvalues):

    # Gradiente de los parametros
    self.dweights = np.dot(self.inputs.T,dvalues)
    self.dbias = np.sum(dvalues,axis=0,keepdims=True)

    # Regularizacion L1 weights
    if self.weight_regularizer_l1 > 0:
        d_l1 = np.ones_like(self.weights)
        d_l1[self.weights < 0] = -1
        self.dweights += self.weight_regularizer_l1 * d_l1

    # Regularizacion L2 weights
    if self.weight_regularizer_l2 > 0:
        self.dweights += 2 * self.weight_regularizer_l2 * self.weights

    # Regularizacion L1 bias
    if self.bias_regularizer_l1 > 0:
        d_l1 = np.ones_like(self.bias)
        d_l1[self.bias < 0] = -1
        self.dbias += self.bias_regularizer_l1 * d_l1

    # Regularizacion L2 bias
    if self.bias_regularizer_l2 > 0:
        self.dbias += 2 * self.bias_regularizer_l2 * self.bias

    # Gradiente de los valores
    self.dinputs = np.dot(dvalues,self.weights.T)



# Creamos dos vectores
# VECTOR X: lista de n=100 entre 0 y 2*pi 
x = np.linspace(0, 2 * np.pi, num=100)
# VECTOR Y: lista de cosenos del vector x
y = np.cos(x)

# Creamos un array con lso inputs:
x = np.array(x)
y = np.array(y)

# Creamosuna matriz con nuestros datos:
Data = np.vstack((x,y)).T #(100,2) (muestras,inputs*entrada)

# las columnas del data deben coincidir con el input de la capa

capa1 = Capa_densa(2,3)
capa2 = Capa_densa(3,6)

'''
CONEXION ENTRE CAPAS:
    A LA CAPA1 LE ENTRA EL DATA INICIAL, A LA CAPA 2 LE ENTRA EL OUTPUT DE LA CAPA1
    Y LA CAPA 2 DA UN OUTPUT FINAL
'''
#Forward:   
# data.shape | wheights.shape | bias.shape → capa1.shape
#    (100×2) · (2×3) + (1×3) → (100×3)
capa1.forward(Data) # 

# capa1.shape | wheigths.shape | bias.shape → capa2.shape
#   (100x3) · (3x6) + (1x6) → (100x6)
capa2.forward(capa1.output)

#print(capa2.output)