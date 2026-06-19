# Aprendizaje no supervisado en visión artificial

Resumen simple sobre clustering y algoritmos no supervisados aplicados a imágenes.

Temas:

- Clustering jerárquico
- K-Means
- DBSCAN
- Clustering espectral
- PCA
- t-SNE
- Autoencoders
- SOM

---

## 1. Idea general

En aprendizaje no supervisado tienes datos, pero no tienes etiquetas.

```text
imágenes sin etiqueta → algoritmo → estructura/grupos/representaciones
```

Ejemplo:

```text
imagen_001 → sin etiqueta
imagen_002 → sin etiqueta
imagen_003 → sin etiqueta
```

Después de aplicar clustering:

```text
imagen_001 → cluster 0
imagen_002 → cluster 2
imagen_003 → cluster 0
```

El algoritmo no sabe que un grupo significa `perro`, `coche` o `persona`.

Solo agrupa datos parecidos según las características que le das.

---

## 2. Clustering en visión artificial

En Computer Vision, clustering puede aplicarse a distintos niveles:

| Nivel | Qué agrupas | Para qué sirve |
|---|---|---|
| Píxeles | Colores/intensidades parecidas | Segmentación básica |
| Regiones | Zonas visuales parecidas | Separar partes de una imagen |
| Descriptores | Keypoints/descriptores similares | Vocabulario visual |
| Imágenes completas | Imágenes representadas por vectores | Organizar datasets |

Importante:

```text
clustering no trabaja con imágenes directamente
trabaja con vectores numéricos
```

Por eso normalmente antes haces:

```text
imagen → vector de características → clustering
```

---

## 3. Qué obtienes después de aplicar clustering

Normalmente obtienes una etiqueta de cluster por cada muestra.

Ejemplo:

```python
labels = [0, 0, 1, 2, 1, 0]
```

Significa:

```text
muestra 0 → cluster 0
muestra 1 → cluster 0
muestra 2 → cluster 1
muestra 3 → cluster 2
```

Las imágenes originales no se modifican automáticamente.

El resultado es una asignación de grupo.

---

## 4. Preparar imágenes para clustering

Muchos algoritmos necesitan una matriz:

```text
X = muestras x características
```

Ejemplo con imágenes de `digits` de `sklearn`:

```python
from sklearn import datasets

digits = datasets.load_digits()

X = digits.data      # imágenes aplanadas: (n_muestras, 64)
y = digits.target    # etiquetas reales, solo para comparar después

print(X.shape)
print(y.shape)
```

`X` contiene las imágenes convertidas en vectores.

`y` no se usa para entrenar el clustering. Solo puede usarse después para comprobar si los grupos se parecen a las clases reales.

---

# 5. K-Means

## Qué es

`K-Means` agrupa los datos en `K` clusters.

Tú decides cuántos grupos quieres.

Ejemplo:

```text
K = 10 → quiero 10 grupos
```

El algoritmo busca centros y asigna cada muestra al centro más cercano.

---

## Cuándo usar K-Means

| Caso | Tiene sentido |
|---|---|
| Sabes aproximadamente cuántos grupos quieres | Sí |
| Los grupos son compactos | Sí |
| Quieres algo simple y rápido | Sí |
| Hay mucho ruido/outliers | No es ideal |
| Los clusters tienen formas raras | No es ideal |

---

## Ejemplo K-Means con imágenes `digits`

```python
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Cargar dataset
digits = datasets.load_digits()

X = digits.data
y = digits.target

# Aplicar K-Means
kmeans = KMeans(n_clusters=10, random_state=42, n_init=10)
labels = kmeans.fit_predict(X)

print(labels[:20])
```

Visualizar con PCA:

```python
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X)

plt.scatter(X_2d[:, 0], X_2d[:, 1], c=labels, cmap="tab10")
plt.title("K-Means sobre digits")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
```

Ver ejemplos de un cluster:

```python
cluster_id = 0

indices = [i for i, label in enumerate(labels) if label == cluster_id]

fig, axes = plt.subplots(1, 5, figsize=(10, 3))

for ax, idx in zip(axes, indices[:5]):
    ax.imshow(digits.images[idx], cmap="gray")
    ax.axis("off")

plt.suptitle(f"Ejemplos del cluster {cluster_id}")
plt.show()
```

---

# 6. Clustering jerárquico

## Qué es

El clustering jerárquico crea una estructura en forma de árbol.

Ese árbol se llama `dendrograma`.

La idea es:

```text
muestras individuales → grupos pequeños → grupos grandes → grupo final
```

---

## Para qué sirve

| Uso | Explicación |
|---|---|
| Ver relaciones entre muestras | Qué imágenes se parecen más |
| Elegir número de clusters | Cortando el árbol a cierta altura |
| Detectar outliers | Muestras que se unen tarde al resto |
| Analizar estructura del dataset | Ver si hay ramas claras |

---

## Ejemplo con dendrograma

```python
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import linkage, dendrogram

# Cargar dataset
digits = datasets.load_digits()

# Usar pocas muestras para que el dendrograma sea legible
X = digits.data[:50]

# Escalar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Calcular clustering jerárquico
linked = linkage(X_scaled, method="ward")

# Dibujar dendrograma
plt.figure(figsize=(12, 6))
dendrogram(linked)
plt.title("Dendrograma de clustering jerárquico")
plt.xlabel("Muestras")
plt.ylabel("Distancia")
plt.show()
```

---

## Cortar el árbol para obtener clusters

```python
from scipy.cluster.hierarchy import fcluster

labels = fcluster(linked, t=5, criterion="maxclust")

print(labels)
```

Aquí:

```text
t=5 → queremos 5 clusters
```

---

# 7. DBSCAN

## Qué es

`DBSCAN` agrupa puntos según densidad.

No necesitas decir cuántos clusters quieres.

El algoritmo busca zonas densas de puntos y marca como ruido los puntos aislados.

---

## Conceptos importantes

| Parámetro | Significado |
|---|---|
| `eps` | Distancia máxima para considerar vecinos |
| `min_samples` | Número mínimo de vecinos para formar una zona densa |
| `label = -1` | Punto considerado ruido/outlier |

---

## Cuándo usar DBSCAN

| Caso | Tiene sentido |
|---|---|
| No sabes cuántos grupos hay | Sí |
| Quieres detectar outliers | Sí |
| Los clusters tienen formas irregulares | Sí |
| Los datos tienen densidades muy distintas | Puede fallar |
| Muchas dimensiones sin reducción previa | Puede fallar |

---

## Ejemplo DBSCAN con PCA

DBSCAN suele funcionar mejor si reduces dimensionalidad antes.

```python
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

# Cargar dataset
digits = datasets.load_digits()

X = digits.data

# Escalar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Reducir a 2D para clustering y visualización
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)

# Aplicar DBSCAN
dbscan = DBSCAN(eps=2.5, min_samples=5)
labels = dbscan.fit_predict(X_2d)

print(set(labels))
```

Visualizar:

```python
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=labels, cmap="tab10")
plt.title("DBSCAN sobre digits reducido con PCA")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
```

Interpretación:

```text
label -1 → ruido/outlier
label 0, 1, 2... → clusters encontrados
```

---

# 8. Clustering espectral

## Qué es

El clustering espectral usa una matriz de similitud entre muestras.

En vez de mirar solo distancias directas, analiza la estructura de relación entre los puntos.

Puede funcionar bien cuando los clusters no son separables de forma simple.

---

## Cuándo usar clustering espectral

| Caso | Tiene sentido |
|---|---|
| Clusters con formas complejas | Sí |
| Datos donde importa la similitud entre puntos | Sí |
| Dataset pequeño/mediano | Sí |
| Dataset muy grande | Puede ser costoso |
| Quieres algo rápido y simple | Mejor K-Means |

---

## Ejemplo con `SpectralClustering`

```python
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import SpectralClustering

# Cargar dataset
digits = datasets.load_digits()

X = digits.data

# Escalar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Reducir a 2D para visualizar
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)

# Aplicar clustering espectral
spectral = SpectralClustering(
    n_clusters=10,
    affinity="nearest_neighbors",
    random_state=42
)

labels = spectral.fit_predict(X_2d)

plt.scatter(X_2d[:, 0], X_2d[:, 1], c=labels, cmap="tab10")
plt.title("Clustering espectral sobre digits")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
```

---

# 9. Comparativa de tipos de clustering

| Algoritmo | Necesita número de clusters | Detecta outliers | Bueno para |
|---|---:|---:|---|
| `K-Means` | Sí | No | Grupos compactos |
| `Jerárquico` | No necesariamente | Limitado | Ver estructura en árbol |
| `DBSCAN` | No | Sí | Grupos por densidad y outliers |
| `Espectral` | Sí | No | Estructuras complejas |

---

# 10. PCA - Análisis de Componentes Principales

## Qué es

`PCA` reduce la dimensionalidad de los datos.

Dimensionalidad significa número de características.

Ejemplo:

```text
imagen 28x28 → 784 dimensiones
PCA → 2, 10, 50 dimensiones
```

PCA crea nuevas variables llamadas componentes principales.

No elige píxeles concretos. Crea combinaciones de las variables originales.

---

## Para qué sirve

| Uso | Explicación |
|---|---|
| Visualización | Pasar datos a 2D o 3D |
| Reducir ruido | Quedarse con componentes importantes |
| Acelerar modelos | Menos dimensiones |
| Preprocesar clustering | Mejorar K-Means, DBSCAN, etc. |

---

## Ejemplo PCA

```python
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

digits = datasets.load_digits()

X = digits.data
y = digits.target

# Escalar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Reducir a 2 dimensiones
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(X.shape)
print(X_pca.shape)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap="tab10")
plt.title("PCA sobre digits")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
```

---

## Varianza explicada

PCA permite ver cuánta información conserva cada componente.

```python
pca = PCA(n_components=10)
X_pca = pca.fit_transform(X_scaled)

print(pca.explained_variance_ratio_)
print(pca.explained_variance_ratio_.sum())
```

Si la suma da:

```text
0.80
```

significa:

```text
esas componentes conservan aproximadamente el 80% de la variabilidad de los datos
```

---

# 11. t-SNE

## Qué es

`t-SNE` es una técnica de reducción de dimensionalidad pensada sobre todo para visualización.

Intenta colocar puntos parecidos cerca y puntos diferentes lejos en 2D o 3D.

---

## Para qué sirve

| Uso | Explicación |
|---|---|
| Visualizar datasets complejos | Ver grupos en 2D |
| Explorar embeddings | Ver si las clases se separan |
| Analizar features de una CNN | Comprobar si las representaciones tienen estructura |

---

## Diferencia PCA vs t-SNE

| Técnica | Característica |
|---|---|
| `PCA` | Lineal, rápido, más interpretable |
| `t-SNE` | No lineal, muy útil para visualizar, menos interpretable |

t-SNE no suele usarse como preprocesamiento principal para entrenar modelos. Se usa mucho para visualizar.

---

## Ejemplo t-SNE

```python
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler

digits = datasets.load_digits()

X = digits.data
y = digits.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

tsne = TSNE(
    n_components=2,
    perplexity=30,
    learning_rate="auto",
    init="pca",
    random_state=42
)

X_tsne = tsne.fit_transform(X_scaled)

plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap="tab10")
plt.title("t-SNE sobre digits")
plt.xlabel("Dimensión 1")
plt.ylabel("Dimensión 2")
plt.show()
```

---

# 12. Autoencoders

## Qué es

Un autoencoder es una red neuronal que aprende a reconstruir su propia entrada.

Tiene dos partes:

```text
encoder → representación comprimida → decoder
```

Ejemplo:

```text
imagen 28x28 → vector latente de 32 valores → reconstrucción 28x28
```

---

## Para qué sirve

| Uso | Explicación |
|---|---|
| Reducir dimensionalidad | Comprimir datos en espacio latente |
| Eliminar ruido | Denoising autoencoder |
| Detectar anomalías | Si reconstruye mal, puede ser dato raro |
| Extraer features | Usar el encoder como extractor de características |

---

## Ejemplo autoencoder simple con MNIST

```python
import tensorflow as tf
from tensorflow.keras import layers, models, datasets
import matplotlib.pyplot as plt

# Cargar datos
(train_images, _), (test_images, _) = datasets.mnist.load_data()

# Normalizar
train_images = train_images / 255.0
test_images = test_images / 255.0

# Aplanar imágenes: 28x28 → 784
train_flat = train_images.reshape(-1, 784)
test_flat = test_images.reshape(-1, 784)

# Definir autoencoder
input_layer = layers.Input(shape=(784,))

encoded = layers.Dense(128, activation="relu")(input_layer)
encoded = layers.Dense(32, activation="relu")(encoded)

decoded = layers.Dense(128, activation="relu")(encoded)
decoded = layers.Dense(784, activation="sigmoid")(decoded)

autoencoder = models.Model(input_layer, decoded)

autoencoder.compile(
    optimizer="adam",
    loss="binary_crossentropy"
)

# Entrenar: entrada = salida esperada
autoencoder.fit(
    train_flat,
    train_flat,
    epochs=10,
    batch_size=256,
    validation_data=(test_flat, test_flat)
)
```

Reconstruir imágenes:

```python
reconstruidas = autoencoder.predict(test_flat[:5])

for i in range(5):
    plt.figure(figsize=(4, 2))

    plt.subplot(1, 2, 1)
    plt.imshow(test_flat[i].reshape(28, 28), cmap="gray")
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(reconstruidas[i].reshape(28, 28), cmap="gray")
    plt.title("Reconstruida")
    plt.axis("off")

    plt.show()
```

---

## Usar el encoder para extraer features

```python
encoder = models.Model(input_layer, encoded)

features = encoder.predict(test_flat)

print(features.shape)
```

Después podrías aplicar clustering sobre `features`:

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=10, random_state=42, n_init=10)
labels = kmeans.fit_predict(features)

print(labels[:20])
```

---

# 13. SOM - Self-Organizing Maps

## Qué es

`SOM` significa `Self-Organizing Map`.

Es una red no supervisada que organiza los datos en una cuadrícula 2D.

La idea es:

```text
datos de muchas dimensiones → mapa 2D organizado por similitud
```

Puntos parecidos acaban cerca en el mapa.

---

## Para qué sirve

| Uso | Explicación |
|---|---|
| Visualización | Representar datos complejos en una cuadrícula |
| Clustering | Agrupar datos parecidos |
| Exploración de datasets | Ver estructura general |
| Reducción de dimensionalidad | Pasar de muchas features a mapa 2D |

---

## Instalación

Una librería común es `MiniSom`.

```bash
pip install minisom
```

---

## Ejemplo SOM con `digits`

```python
import numpy as np
import matplotlib.pyplot as plt

from minisom import MiniSom
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler

# Cargar dataset
digits = datasets.load_digits()

X = digits.data
y = digits.target

# Escalar a [0, 1]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Crear SOM de 10x10
som = MiniSom(
    x=10,
    y=10,
    input_len=X_scaled.shape[1],
    sigma=1.0,
    learning_rate=0.5,
    random_seed=42
)

som.random_weights_init(X_scaled)
som.train_random(X_scaled, num_iteration=1000)

# Visualizar dónde cae cada muestra
plt.figure(figsize=(8, 8))

for i, x in enumerate(X_scaled):
    w = som.winner(x)
    plt.text(
        w[0],
        w[1],
        str(y[i]),
        color=plt.cm.tab10(y[i] / 10),
        fontdict={"size": 8}
    )

plt.xlim(-1, 10)
plt.ylim(-1, 10)
plt.title("SOM sobre digits")
plt.grid()
plt.show()
```

Interpretación:

```text
si dígitos iguales aparecen cerca entre sí,
el SOM ha organizado bien la estructura visual
```

---

# 14. Comparativa PCA, t-SNE, Autoencoder y SOM

| Técnica | Tipo | Uso principal |
|---|---|---|
| `PCA` | Reducción lineal | Reducir dimensiones y visualizar |
| `t-SNE` | Reducción no lineal | Visualizar grupos en 2D |
| `Autoencoder` | Red neuronal no supervisada | Comprimir, reconstruir y extraer features |
| `SOM` | Mapa autoorganizado | Visualizar y agrupar en cuadrícula |

---

## Diferencia clave

| Técnica | Aprende representación | Buena para visualizar | Buena para clustering posterior |
|---|---:|---:|---:|
| `PCA` | Sí, lineal | Sí | Sí |
| `t-SNE` | Sí, no lineal | Sí | No siempre |
| `Autoencoder` | Sí, no lineal | Indirectamente | Sí |
| `SOM` | Sí | Sí | Sí |

---

# 15. Flujo práctico recomendado

Para un dataset de imágenes sin etiquetas:

```text
1. Cargar imágenes
2. Preprocesar
3. Extraer features
4. Reducir dimensionalidad si hace falta
5. Aplicar clustering
6. Mirar ejemplos de cada cluster
7. Interpretar los grupos
```

Ejemplo típico:

```text
imágenes → CNN/Autoencoder/PCA → vectores → K-Means/DBSCAN → clusters
```

---

# 16. Qué técnica usar según el caso

| Objetivo | Técnica recomendable |
|---|---|
| Agrupar imágenes en K grupos | K-Means |
| Ver estructura tipo árbol | Clustering jerárquico |
| Detectar outliers | DBSCAN |
| Visualizar datos en 2D rápido | PCA |
| Visualizar grupos complejos | t-SNE |
| Aprender compresión no lineal | Autoencoder |
| Crear mapa visual organizado | SOM |
| Clusters con formas complejas | Clustering espectral |

---

# 17. Resumen ultracorto

| Concepto | Idea |
|---|---|
| Aprendizaje no supervisado | Aprender estructura sin etiquetas |
| Clustering | Agrupar muestras parecidas |
| K-Means | Agrupa en K grupos |
| Jerárquico | Crea árbol de similitud |
| DBSCAN | Agrupa por densidad y detecta ruido |
| Espectral | Usa similitud entre muestras |
| PCA | Reduce dimensiones linealmente |
| t-SNE | Visualiza datos complejos en 2D |
| Autoencoder | Red que aprende a comprimir y reconstruir |
| SOM | Mapa 2D autoorganizado |

---

# 18. Vocabulario técnico correcto

| Forma informal | Mejor término |
|---|---|
| Grupos automáticos | Clusters |
| Número de grupo | Etiqueta de cluster |
| Datos raros | Outliers o anomalías |
| Bajar dimensiones | Reducir dimensionalidad |
| Imagen convertida en lista | Imagen vectorizada o aplanada |
| Datos parecidos | Muestras cercanas en el espacio de características |
| Mirar si se separan | Visualizar embeddings o representaciones |
