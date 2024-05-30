# Capítulo 21: Manejando archivos

Vamos a profundizar en cómo manejar archivos en Python, un componente esencial en la programación backend, ya que a menudo necesitamos leer configuraciones, procesar datos almacenados y registrar información de operaciones.

### 1. Introducción al Manejo de Archivos

- **Usos comunes**: Leer datos de configuración, guardar resultados, interactuar con logs, etc.

### 2. Abrir un Archivo

- **Función `open()`**:

Para trabajar con archivos en Python, el primer paso es abrir el archivo usando la función `open()`. Esta función es fundamental y su sintaxis básica es:

```python
archivo = open('ruta/al/archivo', 'modo')
```

Donde `'ruta/al/archivo'` debe ser reemplazada por la ruta al archivo que deseas abrir, y `'modo'` indica cómo quieres abrir el archivo. La función `open()` devuelve un objeto de archivo que se utiliza para llamar a otros métodos asociados con operaciones de archivo.

#### Modos de apertura**: 
Los modos de apertura definen cómo el archivo será abierto y utilizado. Aquí están los más comunes:

- **`'r'`** - Modo de solo lectura. Este es el modo predeterminado si no se especifica ninguno. El archivo debe existir, de lo contrario, se lanzará un error.

  ```python
  archivo = open('ejemplo.txt', 'r')
  contenido = archivo.read()
  ```

- **`'w'`** - Modo de solo escritura. Si el archivo no existe, se crea. Si el archivo existe, su contenido será borrado antes de que se empiece a escribir.

  ```python
  archivo = open('ejemplo.txt', 'w')
  archivo.write('Hola mundo!')
  ```

- **`'a'`** - Modo añadir. Si el archivo no existe, se crea. Si el archivo existe, el contenido que escribas se añadirá al final del archivo, sin borrar el contenido existente.

  ```python
  archivo = open('ejemplo.txt', 'a')
  archivo.write('\nAdiós mundo!')
  ```

- **`'r+'`** - Modo de lectura y escritura. El archivo debe existir. Puedes leer y escribir en el archivo.

  ```python
  archivo = open('ejemplo.txt', 'r+')
  datos = archivo.read()
  archivo.write('\nNuevo texto al final')
  ```

- **`'w+'`** - Modo de escritura y lectura. Similar a `'w'`, pero también permite leer el archivo.

  ```python
  archivo = open('ejemplo.txt', 'w+')
  archivo.write('Nuevo contenido')
  archivo.seek(0)  # Mueve el cursor al inicio del archivo
  print(archivo.read())
  ```

- **`'a+'`** - Modo añadir y leer. Permite añadir contenido al final del archivo y leer desde cualquier punto.

  ```python
  archivo = open('ejemplo.txt', 'a+')
  archivo.write('\nOtro texto al final')
  archivo.seek(0)
  print(archivo.read())
  ```

### 3. Leer de un Archivo

- **Método `read()`**:
  ```python
  contenido = archivo.read()
  ```

- **Método `readline()`** (lee una línea cada vez):
  ```python
  linea = archivo.readline()
  ```

- **Método `readlines()`** (lee todas las líneas, devuelve lista):
  ```python
  lineas = archivo.readlines()
  ```

- **Uso de bucles** (leer líneas en un bucle):
  ```python
  for linea in archivo:
      print(linea)
  ```

### 4. Escribir en un Archivo

- **Método `write()`** (escribe una cadena de texto):
  ```python
  archivo.write('Hola mundo\n')
  ```

- **Método `writelines()`** (escribe una lista de cadenas):
  ```python
  archivo.writelines(['Hola', 'Mundo'])
  ```

### 5. Manejo de Errores al Trabajar con Archivos

- **Uso de bloques `try-except`**:
  ```python
  try:
      archivo = open('ruta/al/archivo.txt', 'r')
  except FileNotFoundError:
      print("El archivo no existe.")
  except Exception as e:
      print("Ocurrió un error:", e)
  ```

- **Importancia de `finally` para cerrar archivos**:
  ```python
  finally:
      archivo.close()
  ```

### 6. Uso del Administrador de Contexto `with`

- **Ventajas**: Automatiza el cierre de archivos.

- **Ejemplo**:
  ```python
  with open('ruta/al/archivo.txt', 'r') as archivo:
      for linea in archivo:
          print(linea)
  ```

Siempre es recomendable manejar los archivos con un bloque `with`, que asegura que el archivo se cierre automáticamente al terminar de trabajar con él, incluso si ocurren excepciones:

```python
with open('ejemplo.txt', 'r') as archivo:
    for linea in archivo:
        print(linea)
```

Utilizar correctamente estos modos te permitirá manejar archivos de manera eficiente en tus aplicaciones backend, asegurando tanto la integridad de los datos como la eficiencia del acceso a los mismos.

____

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

Mayo 2024
