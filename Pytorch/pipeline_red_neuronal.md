# 🧠 Pipeline Red Neuronal (Clasificación Binaria)

---

## 🔴 BLOQUE 1 — DATOS

1. Importar datos
2. Identificar variable objetivo (y)
3. Limpiar datos
   - eliminar columnas irrelevantes
   - tratar valores nulos
4. Convertir variables categóricas a numéricas (one-hot encoding)
5. Normalizar datos (si es necesario)
6. Separar dataset (train / test)
7. Convertir datos a tensores

👉 Si este bloque falla → todo falla

---

## 🔵 BLOQUE 2 — RED NEURONAL

1. Definir modelo
   - nº de entradas = nº de features
   - salida = 1 (clasificación binaria)

2. Definir hiperparámetros
   - learning rate
   - epochs
   - batch size

3. Crear objetos
   - modelo
   - función de pérdida (loss)
   - optimizador

---

## 🟢 BLOQUE 3 — ENTRENAMIENTO

Bucle de entrenamiento:

1. Forward (predicción)
2. Calcular pérdida (loss)
3. Backward (gradientes)
4. Actualizar pesos (optimizer step)
5. Limpiar gradientes (optimizer.zero_grad)

---

## 🟡 BLOQUE 4 — EVALUACIÓN

1. Convertir salida del modelo a 0 o 1
2. Comparar con valores reales
3. Calcular métricas (accuracy, etc.)

---

## 🔁 RESUMEN

DATOS → MODELO → ENTRENAMIENTO → RESULTADO

| Importación                                            | ¿Para qué sirve?                                                     | Ejemplo de uso                             |
| ------------------------------------------------------ | -------------------------------------------------------------------- | ------------------------------------------ |
| `import torch`                                         | Librería principal de PyTorch. Se usa para crear y manejar tensores. | `torch.tensor([1, 2, 3])`                  |
| `import torch.nn as nn`                                | Módulo donde están las capas y estructuras de redes neuronales.      | `nn.Linear(4, 8)`                          |
| `import torch.optim as optim`                          | Módulo con los optimizadores que actualizan los pesos del modelo.    | `optim.Adam(model.parameters(), lr=0.001)` |
| `from sklearn.model_selection import train_test_split` | Sirve para separar los datos en entrenamiento y prueba.              | `train_test_split(X, y, test_size=0.2)`    |
| `from sklearn.preprocessing import StandardScaler`     | Sirve para escalar las variables de entrada.                         | `scaler = StandardScaler()`                |
| `import pandas as pd`                                  | Sirve para cargar y manipular datasets en tablas (`DataFrame`).      | `pd.read_csv("datos.csv")`                 |
| `import numpy as np`                                   | Sirve para trabajar con arrays numéricos y operaciones matemáticas.  | `np.array([1, 2, 3])`                      |
