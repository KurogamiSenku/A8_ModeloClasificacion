import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Cargar dataset
df = pd.read_csv("winequality-red.csv", sep=';')

# Separar X e y
X = df.drop('quality', axis=1)
y = df['quality']

# Entrenar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

# Evaluar
y_pred = modelo.predict(X_test)
print(classification_report(y_test, y_pred))

# Guardar modelo
joblib.dump(modelo, 'modelo/modelo_vino.pkl')
