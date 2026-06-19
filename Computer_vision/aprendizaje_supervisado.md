# Aprendizaje supervisado en visión artificial

Resumen simple de técnicas usadas en clasificación de imágenes:

- Máquinas de vectores de soporte (`SVM`)
- Redes neuronales convolucionales (`CNN`)
- Árboles de decisión
- Evaluación de modelos

---

## 1. Idea general

En aprendizaje supervisado tienes:

```text
imágenes + etiquetas reales → entrenamiento → modelo capaz de clasificar nuevas imágenes
```

Ejemplo con dígitos:

```text
imagen de un 0 → etiqueta 0
imagen de un 1 → etiqueta 1
imagen de un 2 → etiqueta 2
...
```

El modelo aprende a relacionar patrones visuales con clases.

---

## 2. Flujo típico en clasificación de imágenes

```text
1. Cargar dataset
2. Separar train/validation/test
3. Preprocesar imágenes
4. Entrenar modelo
5. Predecir con datos nuevos
6. Evaluar resultados
```

En modelos clásicos como `SVM` o `DecisionTree`, normalmente hay que convertir cada imagen en un vector.

Ejemplo:

```text
imagen 8x8 → 64 valores
imagen 28x28 → 784 valores
```

En una `CNN`, normalmente se mantiene la forma espacial:

```text
imagen → alto, ancho, canales
```

---

# 3. SVM - Máquinas de vectores de soporte

## Qué es

Una `SVM` intenta encontrar una frontera que separe las clases lo mejor posible.

En clasificación de imágenes, suele trabajar con imágenes convertidas a vectores.

```text
imagen 8x8 → vector de 64 características → SVM → clase predicha
```

## Cuándo usar SVM

| Caso | Uso |
|---|---|
| Dataset pequeño o mediano | Puede funcionar bien |
| Features ya preparadas | Muy útil |
| Clasificación clásica | Buena opción |
| Imágenes grandes/crudas | Menos práctico que CNN |

---

## Ejemplo SVM con `digits`

```python
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Cargar dataset de dígitos
digits = datasets.load_digits()

X = digits.data      # imágenes ya aplanadas: (n_muestras, 64)
y = digits.target    # etiquetas: 0-9

# Separar train/test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Escalar datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Crear y entrenar SVM
model = SVC(kernel="linear", random_state=42)
model.fit(X_train, y_train)

# Predecir
y_pred = model.predict(X_test)

# Evaluar
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

---

# 4. CNN - Redes neuronales convolucionales

## Qué es

Una `CNN` es una red neuronal diseñada para trabajar con imágenes.

La CNN aprende filtros para detectar:

```text
bordes
texturas
formas simples
formas complejas
partes de objetos
```

## Flujo interno básico

```text
imagen → convoluciones → pooling → flatten → capas densas → predicción
```

| Capa | Función |
|---|---|
| `Conv2D` | Extrae patrones visuales |
| `MaxPooling2D` | Reduce tamaño y conserva activaciones fuertes |
| `Flatten` | Convierte mapas 2D/3D en vector |
| `Dense` | Clasifica usando las características aprendidas |

---

## Ejemplo CNN con MNIST

```python
import tensorflow as tf
from tensorflow.keras import layers, models, datasets
import matplotlib.pyplot as plt

# Cargar MNIST
(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

# Normalizar píxeles a rango [0, 1]
train_images = train_images / 255.0
test_images = test_images / 255.0

# Añadir canal: (n, 28, 28) → (n, 28, 28, 1)
train_images = train_images[..., tf.newaxis]
test_images = test_images[..., tf.newaxis]

# Crear modelo CNN
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),

    layers.Flatten(),
    layers.Dense(64, activation="relu"),
    layers.Dense(10, activation="softmax")
])

# Configurar entrenamiento
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Entrenar
model.fit(
    train_images,
    train_labels,
    epochs=5,
    validation_split=0.2
)

# Evaluar
test_loss, test_accuracy = model.evaluate(test_images, test_labels)
print("Test accuracy:", test_accuracy)
```

Predicción de varias imágenes:

```python
predicciones = model.predict(test_images[:5])

for i in range(5):
    pred = predicciones[i].argmax()
    real = test_labels[i]

    plt.imshow(test_images[i].squeeze(), cmap="gray")
    plt.title(f"Real: {real} | Pred: {pred}")
    plt.axis("off")
    plt.show()
```

---

# 5. Árboles de decisión

## Qué es

Un árbol de decisión clasifica tomando decisiones sucesivas.

Ejemplo conceptual:

```text
si píxel_12 > cierto valor → ve a la derecha
si no → ve a la izquierda
...
clase final
```

En imágenes, normalmente se usan con datos aplanados o con features extraídas.

## Cuándo usar árboles

| Caso | Uso |
|---|---|
| Explicabilidad | Son fáciles de interpretar |
| Datasets pequeños | Pueden servir |
| Baseline rápido | Útiles para comparar |
| Imágenes complejas | Suelen quedarse cortos frente a CNN |

---

## Ejemplo árbol de decisión con `digits`

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Cargar dataset
digits = datasets.load_digits()

X = digits.data
y = digits.target

# Separar train/test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Crear modelo
tree = DecisionTreeClassifier(
    max_depth=10,
    random_state=42
)

# Entrenar
tree.fit(X_train, y_train)

# Predecir
y_pred = tree.predict(X_test)

# Evaluar
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

---

# 6. Evaluación de modelos

## ¿En qué consiste?

Evaluar un modelo consiste en medir su rendimiento con datos que no ha usado para aprender directamente.

La evaluación responde preguntas como:

```text
¿cuántas imágenes clasifica bien?
¿en qué clases se equivoca?
¿confunde unos objetos con otros?
¿generaliza bien a datos nuevos?
```

---

## 6.1 Train, validation y test

| Conjunto | Para qué sirve |
|---|---|
| `train` | El modelo aprende de estos datos |
| `validation` | Sirve para revisar rendimiento y ajustar decisiones |
| `test` | Evaluación final con datos no usados para decidir cambios |

Diferencia clave:

```text
train      → ajusta los pesos/parámetros
validation → ajusta decisiones del desarrollador
test       → mide el rendimiento final
```

---

## 6.2 Accuracy

`Accuracy` mide el porcentaje total de aciertos.

```text
accuracy = aciertos / total de muestras
```

Ejemplo:

```text
80 aciertos de 100 imágenes → accuracy = 0.80
```

Código:

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```

En español a veces se traduce como `precisión`, pero técnicamente es mejor llamarlo `accuracy` o `exactitud`.

---

## 6.3 Matriz de confusión

La matriz de confusión muestra qué clases acierta y qué clases confunde el modelo.

Ejemplo binario:

| | Predice positivo | Predice negativo |
|---|---:|---:|
| Real positivo | `TP` | `FN` |
| Real negativo | `FP` | `TN` |

| Término | Significado |
|---|---|
| `TP` | Verdadero positivo |
| `TN` | Verdadero negativo |
| `FP` | Falso positivo |
| `FN` | Falso negativo |

Código:

```python
from sklearn.metrics import confusion_matrix

matriz = confusion_matrix(y_test, y_pred)
print(matriz)
```

Visualización:

```python
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()
```

Para clasificación multiclase, como MNIST, la matriz muestra qué dígitos se confunden entre sí.

Ejemplo:

```text
muchos 9 clasificados como 4 → el modelo confunde esas dos clases
```

---

## 6.4 Precision

`Precision` mide de todo lo que el modelo predijo como positivo, cuánto era realmente positivo.

```text
precision = TP / (TP + FP)
```

Pregunta que responde:

```text
cuando el modelo dice "positivo", ¿cuántas veces acierta?
```

Código:

```python
from sklearn.metrics import precision_score

precision = precision_score(y_test, y_pred, average="macro")
print("Precision:", precision)
```

En multiclase se suele usar:

```python
average="macro"
```

para calcular la media entre clases.

---

## 6.5 Recall

`Recall` mide de todos los positivos reales, cuántos encontró el modelo.

```text
recall = TP / (TP + FN)
```

Pregunta que responde:

```text
de todos los casos positivos reales, ¿cuántos detecta?
```

Código:

```python
from sklearn.metrics import recall_score

recall = recall_score(y_test, y_pred, average="macro")
print("Recall:", recall)
```

---

## 6.6 F1-score

`F1-score` combina `precision` y `recall`.

Sirve cuando quieres una métrica equilibrada.

```text
F1 alto → buena precision y buen recall
```

Código:

```python
from sklearn.metrics import f1_score

f1 = f1_score(y_test, y_pred, average="macro")
print("F1-score:", f1)
```

---

## 6.7 Classification report

`classification_report` resume varias métricas por clase.

Código:

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

Suele mostrar:

```text
precision
recall
f1-score
support
```

| Campo | Significado |
|---|---|
| `precision` | Calidad de las predicciones positivas |
| `recall` | Capacidad para encontrar los positivos reales |
| `f1-score` | Equilibrio entre precision y recall |
| `support` | Número de muestras reales de cada clase |

---

## 6.8 Validación cruzada

La validación cruzada entrena y evalúa varias veces usando particiones distintas del dataset.

Sirve para obtener una estimación más estable del rendimiento.

Ejemplo:

```text
fold 1 → entrenar/evaluar
fold 2 → entrenar/evaluar
fold 3 → entrenar/evaluar
...
media final
```

Código:

```python
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn import datasets

digits = datasets.load_digits()

X = digits.data
y = digits.target

model = SVC(kernel="linear")

scores = cross_val_score(model, X, y, cv=5)

print(scores)
print("Media:", scores.mean())
```

---

## 6.9 Evaluación en CNN con TensorFlow

En Keras, la evaluación básica se hace con:

```python
test_loss, test_accuracy = model.evaluate(test_images, test_labels)

print("Test loss:", test_loss)
print("Test accuracy:", test_accuracy)
```

Para obtener matriz de confusión:

```python
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

predicciones = model.predict(test_images)
y_pred = np.argmax(predicciones, axis=1)

print(confusion_matrix(test_labels, y_pred))
print(classification_report(test_labels, y_pred))
```

---

## 6.10 Qué técnica usar según el caso

| Caso | Técnica útil |
|---|---|
| Quiero saber porcentaje total de aciertos | `accuracy` |
| Quiero ver qué clases confunde | matriz de confusión |
| Tengo clases desbalanceadas | `precision`, `recall`, `f1-score` |
| Quiero comparar modelos clásicos | cross-validation |
| Quiero evaluación final limpia | test set |
| Quiero revisar evolución durante entrenamiento | validation set |

---

# 7. Comparativa rápida de modelos

| Modelo | Entrada habitual | Ventaja | Limitación |
|---|---|---|---|
| `SVM` | Imagen aplanada o features | Buena en datasets pequeños/medianos | No aprende filtros visuales |
| `CNN` | Imagen con forma espacial | Aprende patrones visuales automáticamente | Requiere más datos/cómputo |
| `Árbol de decisión` | Imagen aplanada o features | Fácil de interpretar | Puede sobreajustar y ser débil en imágenes complejas |

---

# 8. Cuándo usar cada uno

| Situación | Modelo razonable |
|---|---|
| Quiero un baseline rápido | Árbol de decisión o SVM |
| Dataset pequeño y features buenas | SVM |
| Clasificación real de imágenes | CNN |
| Necesito interpretar decisiones | Árbol de decisión |
| Imágenes complejas | CNN |
| Quiero comparar métodos clásicos vs deep learning | SVM/árbol vs CNN |

---

# 9. Resumen ultracorto

| Concepto | Idea |
|---|---|
| Aprendizaje supervisado | Entrena con imágenes y etiquetas |
| SVM | Busca una frontera entre clases |
| CNN | Aprende filtros visuales directamente desde imágenes |
| Árbol de decisión | Clasifica mediante reglas sucesivas |
| Train | Datos para aprender |
| Validation | Datos para ajustar decisiones |
| Test | Datos para evaluar al final |
| Accuracy | Porcentaje total de aciertos |
| Matriz de confusión | Tabla de aciertos y errores por clase |
| Precision | De lo predicho como positivo, cuánto era correcto |
| Recall | De lo positivo real, cuánto encontró |
| F1-score | Equilibrio entre precision y recall |
| Cross-validation | Evaluación con varias particiones |

---

# 10. Vocabulario técnico correcto

| Forma informal | Mejor término |
|---|---|
| Datos de imágenes | Dataset de imágenes |
| Solución del modelo | Predicción |
| Entrenar con imágenes | Ajustar pesos/parámetros |
| Comprobar si va bien | Evaluar rendimiento |
| Fallos por clase | Matriz de confusión |
| Imagen convertida en lista | Imagen aplanada o vectorizada |
| Capas que detectan cosas | Capas convolucionales |
| Precisión total de aciertos | Accuracy o exactitud |
| Datos que mira para mejorar decisiones | Validation set |
