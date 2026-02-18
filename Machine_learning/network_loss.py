''' La pérdida (loss) es una función que mide cuánto se alejan las predicciones del modelo
de los valores reales.
Es un número que cuantifica el error del modelo.'''

import numpy as np

class Loss:

    def calculate(self,output,y):

        perdida_muestra = self.forward(output,y)        

        perdida_media = np.mean(perdida_muestra) 

        return perdida_media
    

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