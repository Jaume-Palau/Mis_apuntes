import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/home/jaume/ConquerX/Mis_apuntes/Machine_learning/ejercicio/apple_quality_sp.csv')

# Limpiar el df:

## columnas no numericas ->ok
## columnas inutiles -> ok
## outliers
## datos Nan -> ok

def graficar_datos(df:pd.DataFrame):

    for columna in df:

        plt.figure(figsize=(10,6))
        plt.hist(df[columna],bins=10)

        plt.title('Histograma de '+columna)
        plt.xlabel('Valor del intervalo')
        plt.ylabel('frecuencia')

        plt.show()

def eliminar_outliers(df:pd.DataFrame) -> pd.DataFrame:


    pass

df_clean = df.drop(columns=['A_id'])
df_clean = df_clean.dropna()

df_clean['Calidad'] = df_clean['Calidad'].map({'good':1,'bad':0})

print(len(df_clean))

df_clean = df_clean[(df_clean <= 10).all(axis=1)]
print(len(df_clean))



 



