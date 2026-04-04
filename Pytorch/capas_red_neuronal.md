### 1. Linear (Fully Connected)
`nn.Linear(in_features, out_features)`  
👉 para datos tabulares (números, features clásicas)  
es la capa básica en la mayoría de modelos  

---

### 2. Convolucional (Conv)
`nn.Conv1d / nn.Conv2d`  
👉 para datos espaciales  
imágenes, audio, señales  
detecta patrones locales (bordes, formas, etc.)  

---

### 3. Recurrente (RNN)
`nn.RNN / nn.LSTM / nn.GRU`  
👉 para datos secuenciales  
texto, series temporales  
tiene memoria de lo anterior  

---

### 4. Embedding
`nn.Embedding(num_embeddings, embedding_dim)`  
👉 para variables categóricas grandes  
texto, IDs, palabras  
convierte índices en vectores numéricos  

---

### Resumen práctico (muy importante)

| Tipo de dato | Capa principal |
|-------------|---------------|
| Datos tabulares | Linear |
| Imágenes | Conv2d |
| Texto / secuencias | RNN / LSTM / GRU |
| Categóricos grandes | Embedding |