''' La pérdida (loss) es una función que mide cuánto se alejan las predicciones del modelo
de los valores reales.
Es un número que cuantifica el error del modelo.'''

import numpy as np

class Loss:

    def calculate(self,output,y):

        perdida_muestra = self.forward(output,y)        

        perdida_media = np.mean(perdida_muestra) 

        return perdida_media
    
def regularization_loss(self, layer):
    regularization_loss = 0

    # L1 weights
    if layer.weight_regularizer_l1 > 0:
        regularization_loss += layer.weight_regularizer_l1 * np.sum(np.abs(layer.weights))

    # L2 weights
    if layer.weight_regularizer_l2 > 0:
        regularization_loss += layer.weight_regularizer_l2 * np.sum(layer.weights * layer.weights)

    # L1 bias
    if layer.bias_regularizer_l1 > 0:
        regularization_loss += layer.bias_regularizer_l1 * np.sum(np.abs(layer.biases))

    # L2 bias
    if layer.bias_regularizer_l2 > 0:
        regularization_loss += layer.bias_regularizer_l2 * np.sum(layer.biases * layer.biases)

    return regularization_loss

class Loss_CategoriclalCrossEntropy(Loss):

    def forward(self,y_pred,y_true):

        # Calculo del numero de datos
        n_datos = len(y_pred)

        y_pred_limite = np.clip(y_pred,1e-7,1-1e-7)


        if len(y_true.shape) == 1:

            confianza= y_pred_limite[range(n_datos),y_true]
        
        elif len(y_true.shape) == 2:
            confianza = np.sum(y_pred_limite*y_true,axis=1)

        perdida = -np.log(confianza)

        return perdida
    

    def backwards(self,dvalues,y_true):

        muestras = len(dvalues)
        etiquetas = len(dvalues[0])

        if len(y_true.shape) == 1:
            y_true = np.eye(etiquetas)[y_true]

        # Calculo el gradiente
        self.dinputs = -y_true/dvalues

        # Normalizo el vectorgradiente con el numero de muestras
        self.dinputs = self.dinputs/muestras

