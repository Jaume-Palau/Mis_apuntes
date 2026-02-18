'''EN ESTE ARCHIVO, LIMPIAMOS EL DATASET DEL TITANIC PARA USARLO EN UNA RED NEURONAL'''
'''LA RED NEURONAL HARÁ UNA PREDICCION DE SUPERVIVENCIA'''

import numpy as np
import pandas as pd

# importar el dataset
df = pd.read_csv('/home/jaume/ConquerX/Mis_apuntes/Machine_learning/Titanic-Dataset.csv')

# limpiar el df de columnas no numericas que no nos van a servir
df_limpio = df.drop(columns=
                    ['PassengerId',
                     'Name',
                     'Ticket',
                     'Cabin',
                     'Embarked',
                     ])

# Limpiar los Nan
df_limpio = df_limpio.dropna()

# Mapear los valores no numericos a numericos 
df_limpio['Sex'] = df_limpio['Sex'].map({'male':0, 'female':1})

#print(df_limpio['Sex']) --> ok

# Extraer la variable independiente en un array
Y = np.array(df_limpio['Survived'])

# Eliminar la columna que hemos extraido en Y del df
df_limpio = df_limpio.drop(columns='Survived')

X = np.array(df_limpio)


'''Creacion de la red neuronal: 
- Capa de entrada 6 neuronas (porque hay 6 columnas del df)
- Capa oculta 
- Capa oculta
- Capa de salida
'''

# Importamos las funciones que hemos creado anteriormente de las capas
from neural_network import Capa_densa # Para las capas ocultas
from activation_functions import Activation_ReLu # Para las capas ocultas
from softmax import Activation_softmax # Para la capa de salida

# Creacion de la primera capa oculta y su activacion
capa1 = Capa_densa(6,10)
activacion1 = Activation_ReLu()

# Creacion de la segubnda capa oculta y su activacion
capa2 = Capa_densa(10,2)
activacion2 = Activation_softmax()

# Iniciamos la red con los valores limpios del df
capa1.forward(X)
# Funcion de activacion sobre los outputs de la capa 1
activacion1.forward(capa1.output)

# Pasamos los datos a la siguiente capa(2) ya procesados con la funcion de activacion
capa2.forward(activacion1.output)
# Procesamos esos datos con la funcion softmax 
activacion2.forward(capa2.output)

# El resultado final sera un set de 2 columnas con las probabilidades de positivo o negativo
print('-----')
print(activacion2.output[:])


