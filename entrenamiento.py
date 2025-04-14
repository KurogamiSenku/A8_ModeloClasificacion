# entrenamiento.py

import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
import joblib

# 1. Cargar el dataset con separador ';'
df = pd.read_csv('data/vino.csv', sep=';')

# 2. Normalizar nombres de columnas (por si acaso)
df.columns = df.columns.str.strip().str.lower()

# 3. Definir variables independientes y dependiente
X = df[['acidez', 'alcohol', 'azucar_residual']]
y = df['calidad']

# 4. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Entrenar el modelo
modelo = ExtraTreesClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 6. Evaluación
y_pred = modelo.predict(X_test)
print("==== Métricas de Evaluación ====")
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.2f}")
print(f"Precision: {precision_score(y_test, y_pred):.2f}")
print(f"Recall:    {recall_score(y_test, y_pred):.2f}")
print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))

# 7. Guardar el modelo entrenado
joblib.dump(modelo, 'models/modelo_entrenado.pkl')
print("\n✅ Modelo guardado en 'models/modelo_entrenado.pkl'")
