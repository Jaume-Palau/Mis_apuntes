# Ejercicio práctico: predicción de abandono de clientes

## Contexto

Imagina que trabajas como desarrollador junior de machine learning en una empresa de telecomunicaciones.

El equipo de negocio quiere anticipar qué clientes tienen más probabilidad de darse de baja para poder lanzar campañas de retención antes de que abandonen la compañía.

Tu tarea es construir un modelo de clasificación binaria capaz de predecir si un cliente abandonará o no la empresa.

La variable objetivo será:

```text
Churn
```

Donde:

```text
No  -> el cliente no abandona
Yes -> el cliente abandona
```

---

## Dataset

Se utilizará el dataset:

```text
Telco Customer Churn
```

Cada fila representa un cliente.

Cada columna contiene información relacionada con:

* Datos del cliente.
* Tipo de contrato.
* Servicios contratados.
* Método de pago.
* Facturación mensual.
* Facturación total.
* Abandono o permanencia del cliente.

---

## Objetivo general

Construir un proyecto completo de machine learning tabular que incluya:

```text
carga de datos
-> inspección inicial
-> limpieza de datos
-> preprocesado
-> creación del modelo
-> entrenamiento
-> evaluación
-> hyperparameter tuning
-> registro de experimentos en W&B
-> fine-tuning del mejor modelo
-> evaluación final
```

La prioridad no es conseguir el mejor resultado posible, sino practicar correctamente el flujo completo de trabajo.

---

## Rol del alumno

Actúas como un desarrollador junior.

No se espera que tomes decisiones perfectas desde el principio, pero sí que justifiques cada paso:

* Qué columnas limpias.
* Qué columnas eliminas.
* Cómo transformas las variables.
* Qué métrica usas.
* Qué hiperparámetros pruebas.
* Qué modelo eliges.
* Por qué consideras que un resultado es mejor que otro.

---

## Requisitos técnicos

El ejercicio debe realizarse usando:

```text
Python
pandas
numpy
scikit-learn
PyTorch
Weights & Biases
```

No se deben usar modelos avanzados como:

```text
XGBoost
LightGBM
CatBoost
Random Forest como modelo principal
```

El modelo principal debe ser una red neuronal densa simple con PyTorch.

---

## Modelo esperado

Debes construir una red neuronal tipo MLP para clasificación binaria.

Estructura orientativa:

```text
input_size
-> Linear
-> ReLU
-> Dropout
-> Linear
-> ReLU
-> Linear
-> output_size = 1
```

La función de pérdida esperada es:

```python
BCEWithLogitsLoss
```

El optimizador inicial recomendado es:

```python
Adam
```

---

## Parte 1: inspección del dataset

Antes de limpiar o modificar datos, debes inspeccionar el dataset.

Debes responder preguntas como:

* ¿Cuántas filas y columnas tiene?
* ¿Qué representa cada fila?
* ¿Qué columnas son numéricas?
* ¿Qué columnas son categóricas?
* ¿Hay valores nulos?
* ¿Hay columnas que parecen numéricas pero realmente son texto?
* ¿Está balanceada la variable objetivo?
* ¿Hay columnas que no deberían usarse para entrenar?

Comandos sugeridos:

```python
df.shape
df.head()
df.info()
df.dtypes
df["Churn"].value_counts()
df["Churn"].value_counts(normalize=True)
```

---

## Parte 2: limpieza de datos

Debes limpiar el dataset de forma razonada.

Columnas que debes revisar especialmente:

```text
customerID
TotalCharges
Churn
```

Preguntas guía:

* ¿`customerID` aporta información útil o es solo un identificador?
* ¿`TotalCharges` está realmente en formato numérico?
* ¿Hay valores vacíos escondidos como texto?
* ¿Cómo convierto la variable objetivo en una variable binaria?
* ¿Qué hago con los valores inválidos o nulos?
* ¿Estoy eliminando columnas por análisis o por intuición?

No elimines columnas como `PaperlessBilling` o `PaymentMethod` sin comprobar antes si pueden aportar información.

---

## Parte 3: preparación de datos

Debes separar las variables predictoras y la variable objetivo.

```text
X -> variables predictoras
y -> variable objetivo
```

Después debes dividir los datos en:

```text
train
validation
test
```

Uso de cada conjunto:

| Conjunto   | Uso                                |
| ---------- | ---------------------------------- |
| train      | Entrenar el modelo                 |
| validation | Comparar modelos e hiperparámetros |
| test       | Evaluación final                   |

Debes evitar usar el conjunto de test durante el entrenamiento o durante el tuning.

---

## Parte 4: preprocesado

Debes preparar los datos para que puedan entrar en una red neuronal.

Variables numéricas:

* Escalado con `StandardScaler`.

Variables categóricas:

* Encoding, preferiblemente `OneHotEncoder`.

Punto importante:

```text
El scaler y los encoders deben ajustarse solo con train.
```

No debes ajustar transformadores usando todo el dataset, porque eso provocaría data leakage.

---

## Parte 5: modelo base

Debes crear un primer modelo funcional en PyTorch.

Este primer modelo no tiene que ser el mejor.

Su objetivo es comprobar que todo el pipeline funciona:

* Datos correctamente procesados.
* Tensores con shapes correctos.
* DataLoader funcionando.
* Modelo entrenando sin errores.
* Loss bajando razonablemente.
* Métricas calculadas correctamente.

Métricas mínimas:

```text
train_loss
val_loss
val_accuracy
val_precision
val_recall
val_f1
val_auc
```

| Métrica     | Qué responde                                                            |
| ----------- | ----------------------------------------------------------------------- |
| `accuracy`  | ¿Cuántas predicciones totales he acertado?                              |
| `precision` | De los clientes que predije que se irían, ¿cuántos realmente se fueron? |
| `recall`    | De todos los clientes que realmente se fueron, ¿cuántos detecté?        |
| `f1`        | Equilibrio entre `precision` y `recall`                                 |
| `auc`       | Qué tan bien separa el modelo clientes que se van y que no se van       |


---

## Parte 6: registro en W&B

Debes registrar los experimentos en Weights & Biases.

Cada run debe guardar:

* Hiperparámetros.
* Loss de entrenamiento.
* Loss de validación.
* Métricas de validación.
* Nombre descriptivo del experimento.

Ejemplo de hiperparámetros a registrar:

```text
learning_rate
batch_size
hidden_size
dropout
weight_decay
epochs
```

---

## Parte 7: hyperparameter tuning

Debes crear un sweep en W&B para probar distintas combinaciones de hiperparámetros.

Parámetros sugeridos:

| Hiperparámetro | Valores posibles    |
| -------------- | ------------------- |
| learning_rate  | 0.01, 0.001, 0.0001 |
| batch_size     | 16, 32, 64          |
| hidden_size    | 16, 32, 64, 128     |
| dropout        | 0.0, 0.2, 0.4       |
| weight_decay   | 0.0, 0.0001, 0.001  |

Debes elegir una métrica principal para seleccionar el mejor modelo.

Métrica recomendada:

```text
val_f1
```

También puedes valorar:

```text
val_auc
```

Pero debes justificar tu elección.

---

## Parte 8: fine-tuning

En este ejercicio, fine-tuning significa:

```text
cargar el mejor modelo encontrado en el sweep
bajar el learning rate
entrenar unas pocas épocas más
comparar los resultados antes y después
```

Ejemplo:

```text
learning_rate inicial: 0.001
learning_rate fine-tuning: 0.0001
```

Objetivo:

* Ajustar mejor el modelo.
* Comprobar si mejora la métrica principal.
* Evitar entrenar de más y provocar sobreajuste.

---

## Parte 9: evaluación final

Cuando hayas elegido el mejor modelo, debes evaluarlo una sola vez en el conjunto de test.

Métricas finales:

```text
test_accuracy
test_precision
test_recall
test_f1
test_auc
matriz de confusión
```

Importante:

```text
No se debe modificar el modelo después de mirar el resultado en test.
```

El test representa datos no vistos.

---

## Preguntas que debes hacerte durante el ejercicio

* ¿Estoy entendiendo los datos antes de limpiarlos?
* ¿Hay columnas que parecen numéricas pero son texto?
* ¿Hay valores vacíos escondidos?
* ¿Estoy eliminando columnas con criterio?
* ¿Está desbalanceada la variable objetivo?
* ¿Accuracy es suficiente para este problema?
* ¿Estoy usando `train`, `validation` y `test` correctamente?
* ¿Estoy evitando data leakage?
* ¿Estoy registrando bien los experimentos?
* ¿Puedo comparar claramente un run contra otro?
* ¿El fine-tuning mejora el modelo o solo añade complejidad?
* ¿Qué limitaciones tiene mi modelo?

---

## Criterio de evaluación

El ejercicio se considerará correcto si consigues:

| Nivel     | Resultado                                                 |
| --------- | --------------------------------------------------------- |
| Mínimo    | Dataset cargado, limpiado y modelo entrenando             |
| Correcto  | Split limpio, preprocesado correcto y métricas calculadas |
| Bueno     | Experimentos registrados en W&B                           |
| Muy bueno | Sweep funcional y comparación de runs                     |
| Excelente | Fine-tuning justificado y evaluación final limpia         |

---

## Entrega esperada

Al finalizar el ejercicio deberías tener:

```text
notebook o scripts con el proceso completo
modelo base entrenado
experimentos en W&B
sweep ejecutado
fine-tuning del mejor modelo
evaluación final en test
conclusiones escritas
```

El objetivo principal es coger soltura trabajando con datos tabulares, limpieza, métricas, parámetros de entrenamiento y comparación de modelos.
