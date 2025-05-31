# app.py

from flask import Flask, render_template, request, redirect, send_file
import pandas as pd
import joblib
import os
from werkzeug.utils import secure_filename

# Configuración de Flask
app = Flask(__name__)
UPLOAD_FOLDER = 'data'
ALLOWED_EXTENSIONS = {'xlsx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Cargar el modelo entrenado
modelo = joblib.load('models/modelo_entrenado.pkl')

# Verifica si el archivo tiene extensión válida
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html', tabla=None)

# Ruta para clasificar datos desde un archivo Excel
@app.route('/clasificar', methods=['POST'])
def clasificar():
    if 'file' not in request.files:
        return redirect('/')
    
    file = request.files['file']
    
    if file.filename == '' or not allowed_file(file.filename):
        return redirect('/')
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        # Cargar archivo Excel
        df = pd.read_excel(filepath)

        # Verificar columnas esperadas
        columnas_esperadas = ['acidez', 'alcohol', 'azucar_residual']
        if not all(col in df.columns for col in columnas_esperadas):
            return "El archivo debe tener las columnas: acidez, alcohol, azucar_residual"

        # Realizar predicciones
        predicciones = modelo.predict(df[columnas_esperadas])
        df['prediccion_calidad'] = predicciones

        # Guardar archivo con resultados
        resultado_path = os.path.join(app.config['UPLOAD_FOLDER'], 'resultado.xlsx')
        df.to_excel(resultado_path, index=False)

        # Mostrar tabla en el navegador
        return render_template(
            'index.html',
            tabla=df.to_html(classes='table table-bordered table-striped', index=False)
        )
    
    except Exception as e:
        return f"Ocurrió un error al procesar el archivo: {str(e)}"

# Ruta para descargar el archivo con resultados
@app.route('/descargar')
def descargar():
    resultado_path = os.path.join(app.config['UPLOAD_FOLDER'], 'resultado.xlsx')
    return send_file(resultado_path, as_attachment=True)

# Ejecutar en local
if __name__ == '__main__':
    app.run(debug=True)
