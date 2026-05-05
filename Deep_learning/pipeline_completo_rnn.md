# Chuleta RNN / LSTM / GRU

## 1. Cuándo usar una RNN

| Caso | ¿Tiene sentido? |
|---|---|
| Datos con orden temporal | Sí |
| Texto / frases / secuencias | Sí |
| Audio / señales | Sí |
| Predicción de precios, demanda, temperatura | Sí |
| Datos tabulares sin orden | Normalmente no |

---

## 2. Preguntas antes de empezar

| Pregunta | Para decidir |
|---|---|
| ¿Predigo un número o una clase? | Tipo de problema |
| ¿Qué quiero predecir? | Target |
| ¿Qué variables uso como entrada? | Features |
| ¿Cuántos pasos anteriores necesito mirar? | Ventana temporal |
| ¿Los datos están ordenados por tiempo? | División correcta |
| ¿Hay valores nulos o raros? | Limpieza |
| ¿Necesito escalar los datos? | Casi siempre sí |
| ¿Estoy usando datos futuros sin querer? | Evitar fuga de datos |

---

## 3. Pipeline general

| Paso | Qué hacer |
|---|---|
| 1 | Cargar datos |
| 2 | Ordenar por fecha / tiempo |
| 3 | Elegir features |
| 4 | Elegir target |
| 5 | Dividir en train / validation / test |
| 6 | Escalar usando solo train |
| 7 | Crear ventanas temporales |
| 8 | Comprobar formas |
| 9 | Crear modelo RNN / LSTM / GRU |
| 10 | Compilar |
| 11 | Entrenar |
| 12 | Evaluar |
| 13 | Predecir |
| 14 | Desnormalizar si hace falta |
| 15 | Interpretar resultados |

---

## 4. División de datos

| Tipo de datos | División |
|---|---|
| Serie temporal | Respetar orden temporal |
| Datos normales tabulares | Se puede mezclar |
| Series temporales | No conviene mezclar aleatoriamente |

| Conjunto | Uso |
|---|---|
| Train | Aprende |
| Validation | Ajusta decisiones |
| Test | Evalúa al final |

---

## 5. Forma que necesita una RNN

| Dimensión | Significado |
|---|---|
| Samples | Número de ejemplos |
| Timesteps | Pasos temporales por ejemplo |
| Features | Variables en cada paso |

| Parte | Ejemplo |
|---|---|
| Samples | 1000 ventanas |
| Timesteps | 60 días anteriores |
| Features | 3 variables por día |

---

## 6. Ventana temporal

| Concepto | Significado |
|---|---|
| Ventana corta | Mira poco pasado |
| Ventana larga | Mira más contexto |
| Ventana demasiado corta | Puede perder patrones |
| Ventana demasiado larga | Más coste y posible ruido |

Pregunta clave:

> ¿Cuánto pasado necesito para predecir el siguiente valor?

---

## 7. Elegir modelo

| Modelo | Uso típico |
|---|---|
| SimpleRNN | Pruebas simples |
| LSTM | Secuencias con dependencias más largas |
| GRU | Similar a LSTM, más ligera |
| Dense final | Convierte la salida en predicción |

| Situación | Modelo inicial |
|---|---|
| Primera prueba | LSTM simple |
| Modelo lento | GRU |
| Ejercicio básico | SimpleRNN o LSTM |
| Datos complejos | LSTM / GRU con más ajuste |

---

## 8. Elegir función de pérdida

| Problema | Salida esperada | Loss |
|---|---|---|
| Regresión | Número continuo | MSE, MAE, Huber |
| Clasificación binaria | 0 o 1 | Binary Crossentropy |
| Multiclase | Una clase entre varias | Sparse Categorical Crossentropy |
| Multiclase one-hot | Vector de clases | Categorical Crossentropy |

| Si predigo... | Uso... |
|---|---|
| Un precio, temperatura, valor | MSE / MAE |
| Sí / no | Binary Crossentropy |
| Una categoría | Categorical Crossentropy |

---

## 9. Métricas

| Problema | Métricas útiles |
|---|---|
| Regresión | MSE, MAE, RMSE |
| Clasificación binaria | Accuracy, Precision, Recall, F1 |
| Multiclase | Accuracy, matriz de confusión |
| Series temporales | Gráfico real vs predicho |

---

## 10. Callbacks útiles

| Callback | Para qué sirve |
|---|---|
| EarlyStopping | Parar si deja de mejorar |
| ModelCheckpoint | Guardar el mejor modelo |
| ReduceLROnPlateau | Bajar learning rate si se estanca |

---

## 11. Señales de problemas

| Resultado | Interpretación |
|---|---|
| Train bien, validation mal | Sobreajuste |
| Train mal, validation mal | Modelo pobre o datos mal preparados |
| Validation bien, test mal | Mala generalización futura |
| Pérdida no baja | Escalado, modelo o learning rate mal |
| Predicción va con retraso | Modelo sigue la tendencia pero no anticipa bien |
| Predicción casi plana | Modelo no está aprendiendo suficiente |

---

## 12. Checklist final

| Comprobación | Hecho |
|---|---|
| Datos ordenados por tiempo | ☐ |
| Target elegido | ☐ |
| Features elegidas | ☐ |
| División temporal correcta | ☐ |
| Escalado sin fuga de datos | ☐ |
| Ventanas temporales creadas | ☐ |
| Entrada en formato 3D | ☐ |
| Loss correcta para el problema | ☐ |
| Métricas adecuadas | ☐ |
| Validation incluida | ☐ |
| Test usado solo al final | ☐ |
| Resultados interpretados con gráfico | ☐ |
