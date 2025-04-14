from flask import Flask, render_template, request, redirect, send_file
import pandas as pd
import joblib
import os

# Crear la app Flask
app = Flask(__name__)

# Cargar el modelo entrenado
modelo = joblib.load('modelo/modelo_vino.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predecir', methods=['POST'])
def predecir():
    if 'file' not in request.files:
        return "No se subió archivo"

    archivo = request.files['file']
    
    if archivo.filename == '':
        return "Nombre de archivo vacío"
    
    # Leer el archivo Excel
    df_nuevos = pd.read_excel(archivo)
    
    # Predecir
    predicciones = modelo.predict(df_nuevos)
    df_nuevos['Predicción'] = predicciones

    # Guardar resultados
    ruta_resultado = 'resultados/resultados.xlsx'
    df_nuevos.to_excel(ruta_resultado, index=False)

    # Mostrar en tabla
    return render_template('resultado.html', tablas=[df_nuevos.to_html(classes='table table-striped', index=False)], archivo=ruta_resultado)

@app.route('/descargar')
def descargar():
    return send_file('resultados/resultados.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
