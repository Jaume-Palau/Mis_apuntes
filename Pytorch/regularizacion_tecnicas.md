### Regularización en Redes Neuronales

---

### 1. Dropout
`nn.Dropout(p)`

👉 apaga neuronas aleatoriamente durante el entrenamiento  
reduce dependencia entre neuronas  
evita overfitting en redes grandes  

---

### 2. L2 (Weight Decay)
`optim.Adam(..., weight_decay=0.001)`

👉 penaliza pesos grandes  
hace el modelo más simple  
es la regularización más usada  

---

### 3. L1
(no tan común en PyTorch directo)

👉 empuja muchos pesos a 0  
sirve para selección de features  
genera modelos más “sparse”  

---

### 4. Early Stopping
(no es una capa, es estrategia)

👉 parar el entrenamiento cuando el modelo deja de mejorar en test  
evita sobreentrenar  
muy usado en práctica real  

---

### 5. Batch Normalization
`nn.BatchNorm1d(num_features)`

👉 normaliza activaciones internas  
mejora estabilidad del entrenamiento  
a veces actúa como regularizador  

---

### 6. Reducir modelo
(cambiar arquitectura)

👉 menos capas o neuronas  
reduce capacidad de memorizar  
primera opción si hay overfitting  

---

### 7. Data Augmentation
(no aplica en tabular)

👉 generar más datos artificiales  
muy usado en imágenes  

---

### 8. Añadir ruido
(manual)

👉 añadir ruido a los datos de entrada  
hace el modelo más robusto  
uso más avanzado  

---