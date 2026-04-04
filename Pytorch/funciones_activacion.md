### 1. ReLU
max(0, x)
👉 la más usada en capas ocultas  
rápida y funciona bien  

---

### 2. Sigmoid
salida entre 0 y 1  
👉 para clasificación binaria (salida)  

---

### 3. Tanh
salida entre -1 y 1  
menos usada hoy, pero válida  

---

### 4. Softmax
convierte en probabilidades que suman 1  
👉 para clasificación multiclase  

---

### Resumen práctico (muy importante)

| Caso | Activación final |
|------|----------------|
| Binaria | Sigmoid (o ninguna + BCEWithLogits) |
| Multiclase | Softmax |
| Capas internas | ReLU |