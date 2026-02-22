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

# print(df_limpio['Sex']) --> ok

# Extraer la variable independiente en un array
Y = np.array(df_limpio['Survived'])

# Eliminar la columna que hemos extraido en Y del df
df_limpio = df_limpio.drop(columns='Survived')

X = np.array(df_limpio)

#print(df_limpio) #--> OK
'''Creacion de la red neuronal: 
- Capa de entrada 6 neuronas (porque hay 6 columnas del df)
- Capa oculta 
- Capa oculta
- Capa de salida
'''

# Importamos las funciones que hemos creado anteriormente de las capas
from neural_network import Capa_densa # Para las capas ocultas
from activation_functions import Activation_ReLu # Para las capas ocultas
from softmax import Activation_softmax, Activation_Softmax_Loss_CategoricalCrossentropy # Para la capa de salida
from SDG_optimizador import Optimizer_SDG

# Creacion de la primera capa oculta y su activacion
capa1 = Capa_densa(6,10)
activacion1 = Activation_ReLu()

# Creacion de la segunda capa oculta y su activacion
capa2 = Capa_densa(10,2)
activacion2 = Activation_softmax()

# Creacion de la funcion de perdida
loss_activation = Activation_Softmax_Loss_CategoricalCrossentropy()

# Creamos el optimizador
optimizador = Optimizer_SDG(learning_rate=0.01,decay=1e-3,momentum=0)

'''INICIO DE LA RED NEURONAL'''

for epoch in range(1000):

    capa1.forward(X)
    # Funcion de activacion sobre los outputs de la capa 1
    activacion1.forward(capa1.output)

    # Pasamos los datos a la siguiente capa(2) ya procesados con la funcion de activacion
    capa2.forward(activacion1.output)
    # Procesamos esos datos con la funcion softmax 
    activacion2.forward(capa2.output)

    # El resultado final sera un set de 2 columnas con las probabilidades de positivo o negativo
    # print('----- PRE ENTRENAMIENTO -----')
    # print(activacion2.output[:3])
    # print('-----')

    # Calculamos la perdida --> Cuanto de grande es el error
    loss = loss_activation.forward(activacion2.output,Y)
    # print(f'Perdida = {loss}')

    # Obtenemos la clase predicha (índice con mayor probabilidad)
    predicciones = np.argmax(loss_activation.output, axis=1)

    # Si Y es one-hot lo transformamos a indices de clases
    if len(Y.shape)==2:
        Y = np.argmax(Y,axis=1)

    # Calculamos la precision --> porcentaje de aciertos
    precision = np.mean(predicciones==Y)
    # print(f'Precision = {precision}')


    '''EN ESTE PUNTO EMPIEZAN LOS BACKWARDS PARA CALCULAR LOS GRADIENTES'''
    ## El proceso es justo la inversa del forward!!
    ## Tener en cuenta que activacion2.forward(capa2.output) ya no sirve porque esta dentro
    ## de la combinada loss_activation = Activation_Softmax_Loss_CategoricalCrossentropy()

    loss_activation.backwards(loss_activation.output,Y)
    capa2.backwards(loss_activation.dinputs)
    activacion1.backward(capa2.dinputs)
    capa1.backwards(activacion1.dinputs)

    # Actualizamos los parametros de cada capa densa
    optimizador.pre_update_params()
    optimizador.update_params(capa1)
    optimizador.update_params(capa2)
    optimizador.post_update_params()

    # Print cada 10 epoch:
    if not epoch % 10:
        print(f'epoch: {epoch}, '+
              f'precision: {precision:.3f}, '+
              f'perdida: {loss:.3f}')
        
        # print("pred0:", np.sum(predicciones==0), "pred1:", np.sum(predicciones==1))
        # print("true0:", np.sum(Y==0), "true1:", np.sum(Y==1))
