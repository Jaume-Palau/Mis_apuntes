import numpy as np
import json
from neural_network import Capa_densa
from activation_functions import Activation_ReLu
from softmax import Activation_Softmax_Loss_CategoricalCrossentropy

## IMPORTAR NUESTRO MODELO

def cargar_datos_json(file_path):

    with open(file_path,"r") as file:
        parametros = json.load(file)

    capa1_datos = parametros['capa1']
    capa2_datos = parametros['capa2']

    export = {
        'capa1_weights' : np.array(capa1_datos['weights']), 
        'capa1_bias' : np.array(capa1_datos['bias']),
        'capa2_weights' : np.array(capa2_datos['weights']), 
        'capa2_bias' : np.array(capa2_datos['bias']),
    } 

    return export

# Parametros del modelo ya entrenado(pesos y sesgos de las capas)
params = cargar_datos_json('Machine_learning/model_parameters.json')

## RED NEURONAL

#CAPA1
capa1 = Capa_densa(6,10)
activacion1 = Activation_ReLu()

#CAPA2
capa2 = Capa_densa(10,2)
activacion2 = Activation_Softmax_Loss_CategoricalCrossentropy()

# SE FIJAN PESOS Y SESGOS:
capa1.weights = params['capa1_weights']
capa1.bias = params['capa1_bias']

capa2.weights = params['capa2_weights']
capa2.bias = params['capa2_bias']

# PARAMETROS DE ENTRADA

mis_datos = {
    'Pclass':1,
    'Sex':1,
    'Age':30,
    'SibSp':0,
    'Parch':0,
    'Fare':150,
}
x = np.array(list(mis_datos.values()))

# EJECUCION DE LOS FORWARDS
capa1.forward(x)
activacion1.forward(capa1.output)
capa2.forward(activacion1.output)
activacion2.forward(capa2.output,np.array([0]))

# RESULTADO
print('Hay un',round(activacion2.output[0][1]*100),'% de supervivencia')

    
