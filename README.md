# Clasificación de Calidad de Vinos - Extra Trees Classifier

Esta es una aplicación desarrollada en Python con Flask para predecir la calidad del vino basada en sus características químicas.

## ¿Cómo usar la aplicación?

1. **Abrir la aplicación Flask**: Ejecuta el archivo `app.py` usando `python app.py`.

2. **Subir archivo de datos**:
   - Haz clic en el botón "Seleccionar archivo".
   - Carga un archivo Excel (`.xlsx`) que contenga las siguientes columnas:
     - `acidez`
     - `alcohol`
     - `azucar_residual`
   - Ejemplo de estructura del archivo:

     | acidez | alcohol | azucar_residual |
     |--------|---------|-----------------|
     | 7.0    | 9.4     | 1.2             |
     | 6.3    | 10.1    | 1.9             |
     | 8.1    | 9.8     | 2.3             |

3. **Clasificar**:
   - Una vez cargado el archivo, haz clic en el botón "Clasificar".
   - La aplicación mostrará una tabla con los resultados y la predicción de calidad (`0` para baja, `1` para alta).

4. **Exportar resultados**:
   - Haz clic en el botón "Exportar Resultados" para descargar un nuevo archivo Excel con la columna adicional de predicción.

## Recomendaciones

- Asegúrate de que los nombres de las columnas coincidan exactamente.
- No dejes celdas vacías en el archivo Excel.
- Usa valores numéricos en las columnas de entrada.

## Créditos
Proyecto para la asignatura de Machine Learning, semestre 6 de Ingeniería de Sistemas y Computación.