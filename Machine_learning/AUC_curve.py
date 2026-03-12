from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve,roc_auc_score
import matplotlib.pyplot as plt


# Generar un dataset sintetico:
x,y = make_classification(n_samples=1000,n_features=20, n_classes=2,random_state=3)

# Dividir el dataset en entrenamiento y prueba:
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=5)

# Creamos un modelo predictivo:
model = LogisticRegression(max_iter=1000)
model.fit(x_train,y_train)

# Predicciones del modelo:
y_probs = model.predict_proba(x_test)[:,1]

# Calcular el area AUC-ROC
auc_roc = roc_auc_score(y_test,y_probs)
print(f'AUC-ROC: {auc_roc}')

fpr,tpr,thresholds = roc_curve(y_test,y_probs)

# Grafico las curvas ROC
plt.figure(figsize=(8,6))
plt.plot(fpr,tpr,color='orange',label=f'ROC curve (area={auc_roc:.2f})')
plt.plot([0,1],[0,1],color='darkgrey',linestyle='--')
plt.xlabel('TASA DE FALSOS POSITIVOS(FP)')
plt.ylabel('TASA DE VERDADEROS POSITIVOS(VP)')
plt.title('Receiver Operating Characteristics (ROC) Curve')
plt.legend(loc='lower right')
plt.show()