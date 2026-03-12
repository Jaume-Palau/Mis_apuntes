import pandas as pd
from sklearn.model_selection import KFold

df = pd.read_csv('/home/jaume/ConquerX/Mis_apuntes/Machine_learning/Titanic-Dataset.csv')

def split_df(df,n_splits):

    '''Funcion que separa en partes iguales un df para usarlo en un entrenamiento'''

    kf = KFold(n_splits=n_splits,shuffle=True,random_state=42)


    for train_index,test_index in kf.split(df):
        
        train_df = df.iloc[train_index]
        test_df = df.iloc[test_index]
        
        print('Tamaño del conjunto de entrenamiento:', train_df.shape)
        print('Tamaño del conjunto de test:', test_df.shape)