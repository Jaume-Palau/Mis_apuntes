### 1. MSELoss (Mean Squared Error)
`nn.MSELoss`  
👉 para regresión  
mide el error cuadrático  

✔ simple  
❌ no adecuada para clasificación  

---

### 2. BCELoss (Binary Cross Entropy)
`nn.BCELoss`  
👉 para clasificación binaria  
requiere sigmoid en la salida  

✔ fácil de entender  
❌ menos estable que su alternativa  

---

### 3. BCEWithLogitsLoss
`nn.BCEWithLogitsLoss`  
👉 clasificación binaria (la mejor opción)  
incluye sigmoid internamente  

✔ más estable  
✔ recomendada en PyTorch  

---

### 4. CrossEntropyLoss
`nn.CrossEntropyLoss`  
👉 clasificación multiclase  
incluye softmax internamente  

✔ estándar para multiclase  

---

### Resumen práctico (muy importante)

| Problema | Función de pérdida |
|---------|------------------|
| Regresión | MSELoss |
| Binaria | BCEWithLogitsLoss |
| Multiclase | CrossEntropyLoss |