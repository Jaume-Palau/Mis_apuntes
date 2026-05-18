# Chuleta: Autoencoders

## ¿Qué es un autoencoder?

Un **autoencoder** es una red neuronal que aprende a copiar su entrada en la salida, pero pasando antes por una representación comprimida o transformada llamada **espacio latente**.

Estructura básica:

| Parte | Función |
|---|---|
| **Encoder** | Reduce la entrada a una representación más pequeña o más útil |
| **Espacio latente** | Resumen interno de la información importante |
| **Decoder** | Reconstruye la entrada original a partir del espacio latente |
| **Función de pérdida** | Mide cuánto se parece la reconstrucción a la entrada original |

Flujo:

`entrada → encoder → espacio latente → decoder → reconstrucción`

## ¿Para qué sirven?

| Uso | Qué resuelve |
|---|---|
| **Reducción de dimensionalidad** | Convertir datos con muchas variables en una representación más pequeña |
| **Compresión** | Guardar la información importante usando menos valores |
| **Eliminación de ruido** | Reconstruir una versión más limpia de los datos |
| **Detección de anomalías** | Detectar datos raros por alto error de reconstrucción |
| **Extracción de características** | Aprender representaciones útiles sin etiquetas |
| **Generación de datos** | Crear nuevas muestras parecidas a las aprendidas |

---

# Tipos de autoencoders

| Tipo | Idea básica | Característica clave | Uso típico | Método de uso |
|---|---|---|---|---|
| **Autoencoder estrecho** | Tiene un cuello de botella más pequeño que la entrada | Obliga a comprimir la información | Reducción de dimensionalidad y compresión | Elegir un espacio latente pequeño, por ejemplo `784 → 32 → 784` |
| **Autoencoder profundo** | Tiene varias capas en encoder y decoder | Aprende patrones más complejos | Datos no lineales, imágenes, señales complejas | Usar varias capas: `entrada → 256 → 64 → 16 → 64 → 256 → salida` |
| **Autoencoder convolucional** | Usa capas convolucionales en vez de capas densas | Mantiene estructura espacial de imágenes | Imágenes, visión artificial, reconstrucción visual | Usar `Conv2D`, `Pooling`, `ConvTranspose2D` o `Upsampling` |
| **Denoising Autoencoder** | Recibe una entrada con ruido y aprende a reconstruir la versión limpia | Aprende representaciones robustas | Quitar ruido de imágenes, audio o señales | Entrenar con `entrada_ruidosa → salida_limpia` |
| **Sparse Autoencoder** | Fuerza a que pocas neuronas se activen mucho | Representación más selectiva y menos redundante | Extracción de características importantes | Añadir penalización de sparsity, por ejemplo L1 o KL divergence |
| **Contractive Autoencoder** | Penaliza que pequeñas variaciones en la entrada cambien mucho el espacio latente | Representación estable y robusta | Manifold learning y reducción robusta | Añadir una penalización sobre la sensibilidad del encoder |
| **Stacked Autoencoder** | Combina varios autoencoders apilados | Aprende representaciones por niveles | Preentrenamiento y extracción progresiva de features | Entrenar capas sucesivas o usar una arquitectura profunda apilada |
| **Variational Autoencoder** | Aprende una distribución latente, no solo un vector fijo | Permite generar datos nuevos | Generación de imágenes, datos sintéticos, modelos generativos | El encoder produce `media` y `varianza`; se muestrea un vector latente y el decoder genera la salida |

---

# Comparación rápida

| Tipo | Principal ventaja | Principal riesgo |
|---|---|---|
| **Estrecho** | Simple y fácil de entender | Puede perder demasiada información |
| **Profundo** | Aprende relaciones complejas | Puede sobreajustar |
| **Convolucional** | Muy bueno para imágenes | Más costoso de entrenar |
| **Denoising** | Robusto al ruido | Si el ruido es excesivo, aprende mal |
| **Sparse** | Extrae características importantes | Requiere ajustar bien la penalización |
| **Contractive** | Latente más estable | Más complejo matemáticamente |
| **Stacked** | Aprende features jerárquicas | Puede ser más difícil de entrenar |
| **VAE** | Genera datos nuevos | Las reconstrucciones pueden ser más borrosas |

---

# Conceptos clave

| Concepto | Significado |
|---|---|
| **Dimensión** | Cada variable, píxel o feature que describe una muestra |
| **Espacio latente** | Representación interna comprimida aprendida por el encoder |
| **Cuello de botella** | Parte más pequeña de la red donde se concentra la información |
| **Reconstrucción** | Salida generada por el decoder |
| **Error de reconstrucción** | Diferencia entre entrada original y salida reconstruida |
| **Manifold** | Estructura interna de baja dimensión donde se organizan los datos |
| **Outlier** | Dato raro o anómalo que no sigue el patrón general |

---

# Idea central

Un autoencoder no aprende simplemente a copiar.

Aprende a representar los datos de forma más útil, eliminando información redundante y conservando los patrones importantes.

La calidad del autoencoder se mide comparando:

`entrada original` vs `salida reconstruida`

Si el error de reconstrucción es bajo, el modelo ha aprendido una buena representación.

Si el error es alto, puede significar que:

| Causa | Interpretación |
|---|---|
| El dato es muy raro | Posible anomalía |
| El modelo es demasiado simple | No tiene capacidad suficiente |
| El cuello de botella es demasiado pequeño | Se pierde demasiada información |
| Hay muchos outliers en entrenamiento | El modelo aprende una representación contaminada |