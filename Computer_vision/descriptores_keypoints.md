# OpenCV - Descriptores y Keypoints

Resumen simple sobre descriptores visuales, puntos clave y métodos como `SIFT`, `SURF` y `AKAZE`.

---

## 1. Idea general

En Computer Vision, muchas veces no basta con mirar todos los píxeles directamente. Queremos encontrar zonas importantes de una imagen y describirlas numéricamente para poder comparar imágenes.

Flujo típico:

```text
imagen → detectar keypoints → calcular descriptores → comparar descriptores
```

| Concepto | Qué significa |
|---|---|
| `Keypoint` | Punto/zona interesante de una imagen. |
| `Descriptor` | Vector numérico que describe cómo es la zona alrededor del keypoint. |
| `Matching` | Comparar descriptores entre imágenes para encontrar correspondencias. |

---

## 2. Keypoints

Un `keypoint` es una zona de la imagen que el algoritmo considera distintiva.

Suelen aparecer en:

```text
esquinas
bordes con textura
zonas con mucho contraste
patrones repetibles
detalles locales
```

No son puntos importantes para una persona necesariamente. Son puntos útiles matemáticamente.

Un keypoint puede guardar:

| Atributo | Significado |
|---|---|
| `pt` | Coordenadas `(x, y)` del punto. |
| `size` | Tamaño de la región analizada. |
| `angle` | Orientación principal del punto. |
| `response` | Fuerza/importancia del keypoint. |
| `octave` | Escala donde se detectó. |

Ejemplo:

```python
import cv2 as cv

image = cv.imread("imagen.jpg", cv.IMREAD_GRAYSCALE)

sift = cv.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(image, None)

print(len(keypoints))
print(keypoints[0].pt)
print(keypoints[0].size)
print(keypoints[0].angle)
```

Dibujar keypoints:

```python
image_kp = cv.drawKeypoints(
    image,
    keypoints,
    None,
    flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

cv.imshow("Keypoints", image_kp)
cv.waitKey(0)
cv.destroyAllWindows()
```

---

## 3. Descriptores

Un descriptor es una representación numérica de una zona de la imagen.

Ejemplo conceptual:

```text
keypoint    → aquí hay una esquina interesante
descriptor → vector que describe el patrón alrededor de esa esquina
```

El descriptor permite comparar puntos entre imágenes distintas.

Ejemplo:

```text
imagen 1: keypoint A → descriptor A
imagen 2: keypoint B → descriptor B

si descriptor A y B son parecidos → probablemente representan la misma zona/objeto
```

---

## 4. Descriptores locales

Los descriptores locales describen zonas pequeñas de la imagen.

Se calculan alrededor de keypoints.

| Ejemplo | Característica |
|---|---|
| `SIFT` | Robusto a escala y rotación. |
| `SURF` | Similar a SIFT, más rápido en algunos casos. |
| `ORB` | Alternativa rápida y libre, usa descriptores binarios. |
| `AKAZE` | Bueno para puntos no lineales, también usa descriptores binarios. |

Uso típico:

```text
detectar puntos clave
calcular descriptor de cada punto
comparar descriptores entre imágenes
```

Aplicaciones:

```text
reconocimiento de objetos
unión de panoramas
matching entre imágenes
seguimiento visual
estimación de movimiento
reconstrucción 3D
```

---

## 5. Descriptores globales

Los descriptores globales describen la imagen completa con un solo vector.

No se centran en keypoints concretos.

Ejemplos:

| Descriptor global | Qué resume |
|---|---|
| Histograma de color | Distribución de colores de toda la imagen. |
| HOG | Distribución de gradientes/bordes. |
| LBP global | Texturas de la imagen. |
| Embeddings CNN | Representación aprendida por una red neuronal. |

Ejemplo: histograma de color con OpenCV.

```python
import cv2 as cv

image = cv.imread("imagen.jpg")

hist_b = cv.calcHist([image], [0], None, [256], [0, 256])
hist_g = cv.calcHist([image], [1], None, [256], [0, 256])
hist_r = cv.calcHist([image], [2], None, [256], [0, 256])

print(hist_b.shape)
```

Idea:

```text
una imagen completa → un vector resumen
```

---

## 6. Comparativa: descriptor local vs global

| Tipo | Qué describe | Ventaja | Limitación |
|---|---|---|---|
| Local | Zonas concretas alrededor de keypoints. | Bueno para encontrar objetos aunque cambie escala, rotación o posición. | Genera muchos puntos/descriptores. |
| Global | Imagen completa. | Simple y rápido para comparar imágenes completas. | Pierde detalle local y puede fallar si cambia el encuadre. |

Ejemplo práctico:

| Situación | Mejor opción |
|---|---|
| Buscar si un objeto aparece dentro de otra imagen | Descriptor local |
| Comparar si dos imágenes completas tienen colores parecidos | Descriptor global |
| Unir fotos para crear un panorama | Descriptor local |
| Clasificar imágenes por estilo/color general | Descriptor global |

---

## 7. Método de extracción de puntos clave

El proceso general es:

```text
1. Cargar imagen
2. Convertir a escala de grises
3. Crear detector
4. Detectar keypoints
5. Calcular descriptores
6. Dibujar o comparar resultados
```

Ejemplo general:

```python
import cv2 as cv

image = cv.imread("imagen.jpg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

detector = cv.SIFT_create()

keypoints, descriptors = detector.detectAndCompute(gray, None)

print("Número de keypoints:", len(keypoints))
print("Forma de descriptores:", descriptors.shape)
```

Si `descriptors.shape` devuelve:

```text
(500, 128)
```

significa:

```text
500 keypoints detectados
cada descriptor tiene 128 valores
```

---

## 8. SIFT

`SIFT` significa `Scale-Invariant Feature Transform`.

Busca puntos clave robustos a:

```text
cambios de escala
rotación
cambios moderados de iluminación
```

Código básico:

```python
import cv2 as cv

image = cv.imread("imagen.jpg", cv.IMREAD_GRAYSCALE)

sift = cv.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(image, None)

print(len(keypoints))
print(descriptors.shape)
```

Dibujar:

```python
image_sift = cv.drawKeypoints(
    image,
    keypoints,
    None,
    flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

cv.imshow("SIFT", image_sift)
cv.waitKey(0)
cv.destroyAllWindows()
```

Características:

| Punto | Detalle |
|---|---|
| Tipo | Detector + descriptor local. |
| Descriptor | Vector de 128 valores. |
| Ventaja | Muy robusto. |
| Coste | Más pesado que ORB/AKAZE. |

---

## 9. SURF

`SURF` significa `Speeded-Up Robust Features`.

Es parecido a SIFT, pero diseñado para ser más rápido.

En OpenCV puede requerir `opencv-contrib-python` y el módulo `xfeatures2d`.

Código típico:

```python
import cv2 as cv

image = cv.imread("imagen.jpg", cv.IMREAD_GRAYSCALE)

surf = cv.xfeatures2d.SURF_create()
keypoints, descriptors = surf.detectAndCompute(image, None)
```

Si da error, suele ser porque tu instalación de OpenCV no incluye `xfeatures2d`.

Instalación habitual:

```bash
pip install opencv-contrib-python
```

Características:

| Punto | Detalle |
|---|---|
| Tipo | Detector + descriptor local. |
| Ventaja | Rápido y robusto. |
| Limitación | Puede no estar disponible en todas las instalaciones. |
| Uso actual | Menos usado que antes; SIFT/ORB/AKAZE suelen ser más prácticos. |

---

## 10. AKAZE

`AKAZE` detecta y describe puntos clave usando un enfoque no lineal.

Código básico:

```python
import cv2 as cv

image = cv.imread("imagen.jpg", cv.IMREAD_GRAYSCALE)

akaze = cv.AKAZE_create()
keypoints, descriptors = akaze.detectAndCompute(image, None)

print(len(keypoints))
print(descriptors.shape)
```

Dibujar:

```python
image_akaze = cv.drawKeypoints(
    image,
    keypoints,
    None,
    flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

cv.imshow("AKAZE", image_akaze)
cv.waitKey(0)
cv.destroyAllWindows()
```

Características:

| Punto | Detalle |
|---|---|
| Tipo | Detector + descriptor local. |
| Descriptor | Normalmente binario. |
| Ventaja | Buena alternativa moderna y eficiente. |
| Uso | Matching, detección de objetos, comparación de imágenes. |

---

## 11. Comparar descriptores entre dos imágenes

El objetivo es encontrar puntos similares en dos imágenes.

Flujo:

```text
imagen 1 → keypoints + descriptors
imagen 2 → keypoints + descriptors
comparar descriptors
dibujar matches
```

Ejemplo con SIFT:

```python
import cv2 as cv

img1 = cv.imread("imagen1.jpg", cv.IMREAD_GRAYSCALE)
img2 = cv.imread("imagen2.jpg", cv.IMREAD_GRAYSCALE)

sift = cv.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

bf = cv.BFMatcher(cv.NORM_L2, crossCheck=True)
matches = bf.match(des1, des2)

matches = sorted(matches, key=lambda x: x.distance)

resultado = cv.drawMatches(
    img1, kp1,
    img2, kp2,
    matches[:30],
    None,
    flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

cv.imshow("Matches", resultado)
cv.waitKey(0)
cv.destroyAllWindows()
```

En SIFT se usa normalmente:

```python
cv.NORM_L2
```

porque sus descriptores son vectores numéricos de tipo float.

---

## 12. Matching con AKAZE

AKAZE suele generar descriptores binarios, así que normalmente se usa distancia de Hamming.

```python
import cv2 as cv

img1 = cv.imread("imagen1.jpg", cv.IMREAD_GRAYSCALE)
img2 = cv.imread("imagen2.jpg", cv.IMREAD_GRAYSCALE)

akaze = cv.AKAZE_create()

kp1, des1 = akaze.detectAndCompute(img1, None)
kp2, des2 = akaze.detectAndCompute(img2, None)

bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

matches = sorted(matches, key=lambda x: x.distance)

resultado = cv.drawMatches(
    img1, kp1,
    img2, kp2,
    matches[:30],
    None,
    flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

cv.imshow("Matches AKAZE", resultado)
cv.waitKey(0)
cv.destroyAllWindows()
```

---

## 13. Interpretación de matches

Un match significa:

```text
este descriptor de la imagen 1 se parece a este descriptor de la imagen 2
```

La distancia mide cuánto se parecen:

```text
distancia baja → descriptores parecidos
distancia alta → descriptores poco parecidos
```

Pero no todos los matches son correctos. Puede haber falsos positivos.

Por eso normalmente se filtran matches malos.

---

## 14. Resumen ultracorto

| Concepto | Idea principal |
|---|---|
| Keypoint | Punto/zona interesante de una imagen. |
| Descriptor | Vector que describe visualmente la zona del keypoint. |
| Descriptor local | Describe zonas concretas. |
| Descriptor global | Resume toda la imagen. |
| SIFT | Muy robusto, descriptor local de 128 valores. |
| SURF | Similar a SIFT, más rápido, puede requerir contrib. |
| AKAZE | Alternativa eficiente, descriptores binarios. |
| Matching | Comparar descriptores para encontrar correspondencias. |

---

## 15. Vocabulario técnico correcto

| Forma informal | Mejor término |
|---|---|
| Puntos marcados | Keypoints o puntos clave. |
| Círculos de colores | Visualización de keypoints. |
| Características de una imagen | Features o características visuales. |
| Comparar puntos | Matching de descriptores. |
| Zonas importantes | Regiones distintivas. |
| Describir una imagen | Extraer descriptores. |
| Agrupar puntos parecidos | Matching o clustering, según el contexto. |

---

## 16. Idea clave final

Los keypoints indican:

```text
dónde mirar
```

Los descriptores indican:

```text
cómo es esa zona
```

El matching permite:

```text
comparar zonas entre imágenes
```

Esa es la base de muchos sistemas clásicos de visión artificial.
