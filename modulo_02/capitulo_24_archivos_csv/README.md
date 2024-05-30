Los archivos CSV (Comma-Separated Values) son un formato ampliamente utilizado para almacenar datos tabulares. Python proporciona varias maneras de trabajar con archivos CSV, siendo las más comunes el módulo integrado `csv` y la biblioteca `pandas`. A continuación, te muestro cómo leer y escribir archivos CSV utilizando ambas herramientas.

### Uso del módulo `csv`

#### Leer un Archivo CSV

Para leer un archivo CSV con el módulo `csv`, puedes utilizar la función `csv.reader()`, que permite iterar sobre las filas del archivo.

**Ejemplo de Lectura con `csv`:**

```python
import csv

# Abrir el archivo CSV para lectura
with open('datos.csv', 'r') as file:
    reader = csv.reader(file)
    # Omitir el encabezado si es necesario
    next(reader)
    # Iterar sobre las filas del archivo
    for row in reader:
        print(row)
```

En este ejemplo, `csv.reader(file)` crea un objeto lector que itera sobre las líneas del archivo CSV. `next(reader)` es utilizado para saltar el encabezado si es necesario.

#### Escribir en un Archivo CSV

Para escribir en un archivo CSV, puedes usar la función `csv.writer()`, que proporciona métodos para escribir datos en formato CSV.

**Ejemplo de Escritura con `csv`:**

```python
import csv

data = [
    ['nombre', 'edad', 'ciudad'],
    ['Juan', '30', 'Ciudad X'],
    ['Ana', '25', 'Ciudad Y']
]

# Abrir el archivo CSV para escritura
with open('nuevos_datos.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Escribir datos en el archivo
    for row in data:
        writer.writerow(row)
```

`csv.writer(file)` crea un objeto escritor que permite escribir filas en el archivo. `writer.writerow(row)` escribe cada fila de datos en el archivo CSV.

### Uso de `pandas`

`pandas` es una biblioteca de análisis de datos que proporciona funciones de alto nivel para la manipulación de datos estructurados, incluidos los CSV.

#### Leer un Archivo CSV

Con `pandas`, leer un archivo CSV es sencillo y permite cargar los datos directamente en un DataFrame, una estructura de datos bidimensional similar a una tabla.

**Ejemplo de Lectura con `pandas`:**

```python
import pandas as pd

# Leer el archivo CSV en un DataFrame
df = pd.read_csv('datos.csv')

# Mostrar las primeras filas del DataFrame
print(df.head())
```

`pd.read_csv('datos.csv')` lee el archivo CSV y lo convierte en un DataFrame, que es fácil de manipular y analizar.

#### Escribir en un Archivo CSV

Para escribir un DataFrame de `pandas` en un archivo CSV, puedes utilizar el método `to_csv()` del DataFrame.

**Ejemplo de Escritura con `pandas`:**

```python
import pandas as pd

# Crear un DataFrame
data = {
    'nombre': ['Juan', 'Ana'],
    'edad': [30, 25],
    'ciudad': ['Ciudad X', 'Ciudad Y']
}
df = pd.DataFrame(data)

# Escribir el DataFrame en un archivo CSV
df.to_csv('nuevos_datos.csv', index=False)
```

`df.to_csv('nuevos_datos.csv', index=False)` escribe el DataFrame en un archivo CSV. `index=False` indica que el índice del DataFrame no debe escribirse en el archivo.

### Consejos Adicionales

- **Manejo de grandes volúmenes de datos**: Para grandes conjuntos de datos, `pandas` es más eficiente que el módulo `csv`.
- **Manejo de excepciones**: Es buena práctica añadir manejo de excepciones al trabajar con archivos para gestionar errores como problemas de lectura/escritura o archivos no encontrados.

____

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

Mayo 2024
