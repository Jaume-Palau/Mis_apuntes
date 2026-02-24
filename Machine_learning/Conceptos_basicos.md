## Conceptos básicos de Machine Learning (Redes Neuronales)

### 1. Capa densa (Dense Layer)
Capa que realiza: entrada × pesos + bias.  
Transforma los datos usando parámetros entrenables.

### 2. Pesos (Weights)
Números que la red ajusta para aprender.  
Son lo que realmente aprende el modelo.

### 3. Bias
Valor adicional que permite desplazar el resultado.  
Evita que la neurona dependa solo de multiplicaciones.

### 4. Forward Pass
Proceso de calcular la predicción desde la entrada hasta la salida.

### 5. Función de pérdida (Loss)
Mide qué tan mala es la predicción.  
Si es alta → el modelo está fallando.

### 6. Categorical Cross-Entropy
Función de pérdida usada en clasificación.  
Penaliza mucho cuando la clase correcta tiene probabilidad baja.

### 7. One-Hot Encoding
Forma de representar etiquetas como vectores.  
Ejemplo: clase 2 → [0,0,1,0].

### 8. Gradiente
Número que indica cuánto y en qué dirección hay que corregir.

### 9. Backpropagation
Proceso de enviar el error hacia atrás para ajustar los pesos.

### 10. Regla de la cadena
Método para propagar el efecto del error capa por capa.

### 11. Derivada (en este contexto)
Medida de cuánto cambia el error si cambiamos ligeramente algo.

### 12. dweights
Cuánto deben cambiar los pesos.

### 13. dbiases
Cuánto deben cambiar los bias.

### 14. dinputs
Gradiente que se pasa a la capa anterior para seguir corrigiendo.

### 15. Softmax
Convierte números en probabilidades que suman 1.

### 16. Iteración
Una pasada completa: forward + backward + actualización.

### 17. Muestras (Batch)
Conjunto de datos que se procesan juntos.

### 18. Learning Rate (Tasa de aprendizaje)
Factor que controla el tamaño del paso al actualizar los pesos.  
Si es muy grande → puede hacer que el entrenamiento sea inestable.  
Si es muy pequeño → el modelo aprende muy lento.

### 19. Decay
Reducción progresiva del learning rate con el tiempo.  
Permite empezar con pasos grandes y después afinar el ajuste.

### 20. Optimizador
Algoritmo que actualiza los pesos usando los gradientes.  
Ejemplos: SGD, AdaGrad, RMSProp.

### 21. Cache (en optimizadores adaptativos)
Memoria interna que almacena información de gradientes anteriores  
para ajustar dinámicamente el tamaño del paso.

### 22. AdaGrad
Optimizador que acumula el cuadrado de los gradientes.  
Hace que el learning rate efectivo disminuya con el tiempo.

### 23. RMSProp
Optimizador que usa una media exponencial del cuadrado del gradiente.  
Evita que el learning rate se vuelva demasiado pequeño.