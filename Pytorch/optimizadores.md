### 1. SGD (Stochastic Gradient Descent)
`torch.optim.SGD`  
👉 el más básico  
actualiza pesos usando el gradiente directamente  
puede usar momentum  

✔ simple  
❌ más lento, necesita ajuste fino del learning rate  

---

### 2. Adam
`torch.optim.Adam`  
👉 el más usado hoy en día  
combina momentum + ajuste automático del learning rate  

✔ rápido, estable  
✔ suele funcionar bien sin tocar mucho  
❌ a veces sobreajusta  

---

### 3. RMSprop
`torch.optim.RMSprop`  
👉 adapta el learning rate según el historial  

✔ bueno para datos ruidosos  
✔ usado en RNN  
❌ menos común que Adam  

---

### 4. Adagrad
`torch.optim.Adagrad`  
👉 reduce el learning rate con el tiempo  

✔ útil si tienes features poco frecuentes  
❌ el learning rate puede volverse demasiado pequeño  

---

### Resumen práctico (muy importante)

| Situación | Optimizador |
|----------|------------|
| Empiezo y quiero algo que funcione | Adam |
| Quiero control total / experimentar | SGD |
| Datos ruidosos / secuencias | RMSprop |
| Features raras / sparse | Adagrad |