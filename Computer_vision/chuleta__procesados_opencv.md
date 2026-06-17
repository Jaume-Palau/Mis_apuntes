# Chuleta rápida de Computer Vision con OpenCV (`cv2`)

Resumen simple de los conceptos vistos en clase. En general, una imagen se puede entender como una matriz de píxeles. En escala de grises cada píxel tiene un valor de intensidad entre `0` y `255`. En color suele tener 3 canales: `BGR` en OpenCV o `RGB` en Matplotlib.

---

## 1. Conceptos básicos de imágenes digitales

| Concepto | Qué significa |
|---|---|
| `Píxel` | Unidad mínima de una imagen. En gris tiene una intensidad; en color tiene varios canales. |
| `Resolución` | Número de píxeles de ancho y alto. Ejemplo: `1920x1080`. |
| `Densidad de píxeles` | Cantidad de píxeles por unidad física, normalmente `ppi` o `dpi`. Afecta a impresión/pantallas, no siempre al procesamiento. |
| `Intensidad` | Valor de brillo de un píxel en escala de grises. `0 = negro`, `255 = blanco`. |
| `Canales` | Componentes de color. OpenCV lee normalmente en `BGR`, no en `RGB`. |

```python
import cv2

imagen = cv2.imread("imagen.jpg")  # BGR por defecto
gris = cv2.imread("imagen.jpg", cv2.IMREAD_GRAYSCALE)

print(imagen.shape)  # alto, ancho, canales
print(gris.shape)    # alto, ancho
```

---

## 2. Formatos de imagen

| Formato | Características básicas |
|---|---|
| `JPG/JPEG` | Comprimido con pérdida. Bueno para fotos. Puede perder calidad. |
| `PNG` | Comprimido sin pérdida. Puede tener transparencia. |
| `BMP` | Sin compresión o poca compresión. Archivos grandes. |
| `TIFF` | Usado en calidad alta, escáneres, medicina, etc. |
| `WEBP` | Formato moderno, buena compresión. |

---

## 3. Preprocesamiento de imágenes

El preprocesamiento prepara una imagen antes de analizarla o usarla en un modelo.

| Objetivo | Qué busca |
|---|---|
| Reducción de ruido | Quitar puntos o variaciones no deseadas. |
| Mejora de contraste | Hacer más visibles las diferencias entre zonas claras y oscuras. |
| Ajuste de brillo/saturación | Modificar iluminación o intensidad de color. |
| Balance de blancos | Corregir dominantes de color. |
| Transformaciones geométricas | Redimensionar, rotar, trasladar o recortar. |

```python
import cv2

imagen = cv2.imread("imagen.jpg")
imagen_redimensionada = cv2.resize(imagen, (224, 224))
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
```

---

## 4. Reducción de ruido

### Filtro gaussiano

Suaviza la imagen usando una distribución gaussiana. El píxel central pesa más que los vecinos.

```python
gauss = cv2.GaussianBlur(gris, (5, 5), 0)
```

| Parámetro | Significado |
|---|---|
| `gris` | Imagen de entrada. |
| `(5,5)` | Tamaño del kernel. Debe ser impar. |
| `0` | Sigma automático calculado por OpenCV. |

---

### Filtro mediano

Sustituye cada píxel por la mediana de sus vecinos. Es bueno para ruido tipo "sal y pimienta".

```python
mediana = cv2.medianBlur(gris, 5)
```

---

### Filtro bilateral

Suaviza ruido pero intenta conservar bordes.

```python
bilateral = cv2.bilateralFilter(gris, 9, 75, 75)
```

| Parámetro | Significado |
|---|---|
| `9` | Diámetro del vecindario. |
| `75` | Influencia de diferencia de color/intensidad. |
| `75` | Influencia de distancia espacial. |

---

## 5. Filtros lineales y no lineales

| Tipo | Idea |
|---|---|
| Filtro lineal | Calcula el nuevo píxel mediante suma ponderada de vecinos. Ejemplo: promedio, gaussiano, Sobel. |
| Filtro no lineal | No usa una simple suma ponderada. Ejemplo: mediana, máximo, mínimo. |

### Filtro promedio

Todos los vecinos pesan igual.

```python
import numpy as np

kernel = np.ones((3, 3), np.float32) / 9
promedio = cv2.filter2D(gris, -1, kernel)
```

`-1` significa que la imagen de salida conserva el mismo tipo/profundidad que la original.

---

### Filtro Sobel

Detecta cambios de intensidad. Se usa para encontrar bordes.

```python
sobel_x = cv2.Sobel(gris, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gris, cv2.CV_64F, 0, 1, ksize=3)

magnitud = np.sqrt(sobel_x**2 + sobel_y**2)
magnitud = cv2.normalize(magnitud, None, 0, 255, cv2.NORM_MINMAX)
magnitud = np.uint8(magnitud)
```

| Variable | Significado |
|---|---|
| `sobel_x` | Cambios en eje X. Detecta principalmente bordes verticales. |
| `sobel_y` | Cambios en eje Y. Detecta principalmente bordes horizontales. |
| `magnitud` | Fuerza total del borde combinando X e Y. |

---

### Filtro máximo y mínimo

Usan el valor máximo o mínimo dentro de una vecindad.

```python
kernel = np.ones((3, 3), np.uint8)

maximo = cv2.dilate(gris, kernel)
minimo = cv2.erode(gris, kernel)
```

---

## 6. Operaciones morfológicas

Trabajan sobre la forma de los objetos. Se usan mucho con imágenes binarias.

Primero suele hacerse una umbralización:

```python
_, binaria = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((3, 3), np.uint8)
```

| Operación | Qué hace |
|---|---|
| Erosión | Reduce zonas blancas. Elimina detalles pequeños. |
| Dilatación | Expande zonas blancas. Une zonas cercanas. |
| Apertura | Erosión + dilatación. Elimina ruido blanco pequeño. |
| Cierre | Dilatación + erosión. Rellena huecos pequeños. |

```python
erosion = cv2.erode(binaria, kernel, iterations=1)
dilatacion = cv2.dilate(binaria, kernel, iterations=1)

apertura = cv2.morphologyEx(binaria, cv2.MORPH_OPEN, kernel)
cierre = cv2.morphologyEx(binaria, cv2.MORPH_CLOSE, kernel)
```

---

## 7. Corrección de contraste, suavizado y realce

### Corrección de contraste

```python
ecualizada = cv2.equalizeHist(gris)
```

Sirve para repartir mejor las intensidades y mejorar el contraste en imágenes grises.

Para color, suele usarse el canal de luminosidad, no directamente BGR completo.

---

### Suavizado

Reduce ruido o detalles finos.

```python
suavizada = cv2.GaussianBlur(gris, (5, 5), 0)
```

---

### Realce

Busca destacar detalles o bordes.

```python
kernel_realce = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

realzada = cv2.filter2D(gris, -1, kernel_realce)
```

---

## 8. Transformada de Fourier

La transformada de Fourier cambia la imagen del dominio espacial al dominio frecuencial.

| Dominio | Pregunta que responde |
|---|---|
| Espacial | ¿Qué intensidad tiene cada píxel y dónde está? |
| Frecuencial | ¿Qué cambios lentos o rápidos forman la imagen? |

| Frecuencia | Representa |
|---|---|
| Bajas frecuencias | Zonas suaves, iluminación, formas generales. |
| Altas frecuencias | Bordes, detalles finos, textura, ruido. |

```python
f = np.fft.fft2(gris)
fshift = np.fft.fftshift(f)

magnitud = 20 * np.log(np.abs(fshift) + 1)
```

Idea clave:

```text
Imagen = combinación de patrones/frecuencias.
```

---

## 9. Operadores de detección de bordes

La detección de bordes busca cambios bruscos de intensidad.

### Sobel

```python
sobel_x = cv2.Sobel(gris, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gris, cv2.CV_64F, 0, 1, ksize=3)
```

---

### Prewitt

OpenCV no tiene una función directa estándar como `cv2.Prewitt`, pero se puede hacer con kernels.

```python
kernel_x = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

kernel_y = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])

prewitt_x = cv2.filter2D(gris, -1, kernel_x)
prewitt_y = cv2.filter2D(gris, -1, kernel_y)
```

---

### Canny

Es un detector de bordes más completo. Usa suavizado, gradientes y umbrales.

```python
bordes = cv2.Canny(gris, 100, 200)
```

| Parámetro | Significado |
|---|---|
| `100` | Umbral bajo. |
| `200` | Umbral alto. |

---

## 10. Bordes vs contornos

| Concepto | Qué significa |
|---|---|
| Borde | Cambio brusco de intensidad entre píxeles. |
| Contorno | Límite cerrado o abierto que delimita un objeto. |

Ejemplo:

```text
Detección de bordes → resalta cambios.
Detección de contornos → extrae límites de objetos.
```

---

## 11. Detección de contornos

Normalmente se parte de una imagen binaria o de bordes.

```python
_, binaria = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)

contornos, jerarquia = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
```

Dibujar contornos:

```python
imagen_color = cv2.cvtColor(gris, cv2.COLOR_GRAY2BGR)
cv2.drawContours(imagen_color, contornos, -1, (0, 255, 0), 2)
```

| Parámetro | Significado |
|---|---|
| `cv2.RETR_EXTERNAL` | Recupera solo contornos externos. |
| `cv2.CHAIN_APPROX_SIMPLE` | Comprime puntos innecesarios del contorno. |
| `-1` en `drawContours` | Dibuja todos los contornos. |

---

## 12. Contornos basados en gradiente y morfología

| Método | Idea |
|---|---|
| Basado en gradiente | Usa cambios de intensidad: Sobel, Prewitt, Canny. |
| Basado en morfología | Usa erosión, dilatación, apertura, cierre para limpiar o separar regiones. |

Ejemplo típico:

```python
bordes = cv2.Canny(gris, 100, 200)
contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```

---

## 13. Segmentación de imágenes

Segmentar significa separar una imagen en regiones u objetos.

| Método | Idea |
|---|---|
| Umbralización | Separar por intensidad. |
| Regiones | Agrupar píxeles similares. |
| Contornos | Usar límites de objetos. |

---

### Umbralización simple

```python
_, binaria = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)
```

---

### Umbralización automática con Otsu

OpenCV calcula automáticamente el umbral.

```python
_, otsu = cv2.threshold(
    gris,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
```

---

### Segmentación por contornos

```python
bordes = cv2.Canny(gris, 100, 200)
contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```

---

## 14. Evaluación de segmentación

Si tienes una máscara real y una máscara predicha, puedes comparar.

| Métrica | Qué mide |
|---|---|
| Accuracy píxel a píxel | Porcentaje de píxeles correctamente clasificados. |
| IoU | Intersección sobre unión entre máscara real y predicha. |
| Dice | Similaridad entre dos máscaras. Muy usada en segmentación. |

Concepto de IoU:

```text
IoU = zona común / zona total ocupada por ambas máscaras
```

Ejemplo básico:

```python
import numpy as np

mascara_real = np.array([[1, 1, 0], [0, 1, 0]])
mascara_pred = np.array([[1, 0, 0], [0, 1, 1]])

interseccion = np.logical_and(mascara_real, mascara_pred).sum()
union = np.logical_or(mascara_real, mascara_pred).sum()

iou = interseccion / union
print(iou)
```

---

## 15. Flujo típico con OpenCV

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. Cargar imagen
imagen = cv2.imread("imagen.jpg")

# 2. Convertir a gris
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# 3. Suavizar
blur = cv2.GaussianBlur(gris, (5, 5), 0)

# 4. Detectar bordes
bordes = cv2.Canny(blur, 100, 200)

# 5. Buscar contornos
contornos, _ = cv2.findContours(
    bordes,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# 6. Dibujar contornos
resultado = imagen.copy()
cv2.drawContours(resultado, contornos, -1, (0, 255, 0), 2)

# 7. Mostrar con Matplotlib
resultado_rgb = cv2.cvtColor(resultado, cv2.COLOR_BGR2RGB)
plt.imshow(resultado_rgb)
plt.axis("off")
plt.show()
```

---

## 16. Resumen ultracorto

| Tema | Idea principal |
|---|---|
| Imagen digital | Matriz de píxeles. |
| Gris | 1 valor por píxel: intensidad. |
| Color | 3 canales: BGR en OpenCV. |
| Filtro promedio | Suaviza haciendo medias. |
| Gaussiano | Suaviza dando más peso al centro. |
| Mediano | Quita ruido extremo. |
| Bilateral | Suaviza conservando bordes. |
| Sobel/Prewitt | Detectan cambios de intensidad. |
| Canny | Detector de bordes más completo. |
| Morfología | Modifica formas en imágenes binarias. |
| Fourier | Analiza frecuencias de la imagen. |
| Contornos | Límites de objetos. |
| Segmentación | Separar objetos o regiones. |

---

## 17. Vocabulario técnico correcto

| Término informal | Mejor término técnico |
|---|---|
| Imagen en blanco y negro | Imagen en escala de grises, si tiene valores 0-255. |
| Pasar un filtro | Convolucionar con un kernel. |
| Borrar ruido | Reducir ruido. |
| Marcar líneas | Detectar bordes o contornos, según el caso. |
| Colores cambiados | Problema de conversión BGR/RGB. |
| Hacer más clara la imagen | Ajustar brillo o contraste. |
| Sacar objetos | Segmentar o extraer contornos. |
