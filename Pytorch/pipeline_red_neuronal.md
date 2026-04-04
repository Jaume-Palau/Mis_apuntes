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
5. Limpiar gradientes 

---

## 🟡 BLOQUE 4 — EVALUACIÓN

1. Convertir salida del modelo a 0 o 1  
2. Comparar con valores reales  
3. Calcular métricas (accuracy, etc.)  

---

## 🔁 RESUMEN

DATOS → MODELO → ENTRENAMIENTO → RESULTADO