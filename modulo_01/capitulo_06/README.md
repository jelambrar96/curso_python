# Capítulo 6. Operaciones con datos string

Los datos de tipo string en Python representan secuencias de caracteres. Aquí tienes algunas operaciones comunes que puedes realizar con datos de tipo string, junto con ejemplos:

1. **Concatenación de Cadenas:**
   Puedes concatenar dos o más cadenas utilizando el operador `+`.

   ```python
   cadena1 = "Hola"
   cadena2 = "Mundo"

   concatenacion = cadena1 + " " + cadena2
   print(concatenacion)  # Salida: Hola Mundo
   ```

2. **Repetición de Cadenas:**
   Puedes repetir una cadena multiplicándola por un número.

   ```python
   cadena = "Python "
   repetida = cadena * 3
   print(repetida)  # Salida: Python Python Python
   ```

3. **Indexación y Slicing:**
   Puedes acceder a caracteres individuales de una cadena mediante indexación, y puedes extraer subcadenas utilizando el slicing.

   ```python
   mensaje = "Hola Python"

   primer_caracter = mensaje[0]
   print(primer_caracter)  # Salida: H

   subcadena = mensaje[5:11]
   print(subcadena)  # Salida: Python
   ```

4. **Longitud de una Cadena:**
   Puedes obtener la longitud de una cadena utilizando la función `len()`.

   ```python
   mensaje = "¡Hola!"

   longitud = len(mensaje)
   print(longitud)  # Salida: 6
   ```

Estas son solo algunas de las operaciones comunes que puedes realizar con datos de tipo string en Python. Las cadenas son versátiles y ofrecen una amplia variedad de métodos y operadores para manipular y trabajar con texto de manera efectiva.

## El operador slice [:]

En Python, el operador de rebanado (slice) `[:]` se utiliza para extraer una porción (subcadena) de una cadena (string). El formato general es `cadena[inicio:fin]`, donde `inicio` es inclusivo y `fin` es exclusivo. Si alguno de ellos se omite, se asume que se refiere al principio o al final de la cadena, respectivamente. Aquí tienes ejemplos para ilustrar su uso:

**Ejemplos de operador de slice en strings:**

```python
# Definir una cadena
cadena = "Python es genial"

# Obtener una porción desde el inicio hasta el índice 6 (sin incluir)
porcion1 = cadena[:6]
print(porcion1)  # Imprime "Python"

# Obtener una porción desde el índice 7 hasta el final
porcion2 = cadena[7:]
print(porcion2)  # Imprime "es genial"

# Obtener una porción desde el índice 7 hasta el índice 9 (sin incluir)
porcion3 = cadena[7:9]
print(porcion3)  # Imprime "es"

# Utilizar índices negativos para contar desde el final
porcion4 = cadena[-5:-1]
print(porcion4)  # Imprime "geni"

# Obtener toda la cadena (equivalente a cadena[:])
copia_completa = cadena[:]
print(copia_completa)  # Imprime "Python es genial"

# Obtener una porción con un paso (cada segundo caracter)
porcion_con_paso = cadena[::2]
print(porcion_con_paso)  # Imprime "Pto sgnl"
```

Es importante tener en cuenta que el operador de slice no modifica la cadena original, sino que crea una nueva cadena con la porción solicitada. Esto hace que sea una herramienta útil para trabajar con subcadenas en Python.

## Metodos de los datos string

Los datos de tipo string en Python tienen muchos métodos incorporados que facilitan la manipulación y transformación de cadenas. Aquí te presento algunos de los métodos más comunes con ejemplos:

1. **`upper()` y `lower()`:**
   - `upper()`: Convierte la cadena a mayúsculas.
   - `lower()`: Convierte la cadena a minúsculas.

   ```python
   mensaje = "Python es divertido"

   en_mayusculas = mensaje.upper()
   print(en_mayusculas)  # Salida: PYTHON ES DIVERTIDO

   en_minusculas = mensaje.lower()
   print(en_minusculas)  # Salida: python es divertido
   ```

2. **`capitalize()` y `title()`:**
   - `capitalize()`: Convierte la primera letra de la cadena a mayúscula.
   - `title()`: Convierte la primera letra de cada palabra a mayúscula.

   ```python
   frase = "python es un lenguaje de programación"

   capitalizada = frase.capitalize()
   print(capitalizada)  # Salida: Python es un lenguaje de programación

   en_titulo = frase.title()
   print(en_titulo)  # Salida: Python Es Un Lenguaje De Programación
   ```

3. **`count(subcadena)` y `find(subcadena)`:**
   - `count(subcadena)`: Cuenta el número de ocurrencias de una subcadena en la cadena.
   - `find(subcadena)`: Devuelve la posición de la primera ocurrencia de la subcadena, o -1 si no se encuentra.

   ```python
   texto = "python es divertido y python es poderoso"

   ocurrencias = texto.count("python")
   print(ocurrencias)  # Salida: 2 (hay dos ocurrencias de "python")

   posicion = texto.find("divertido")
   print(posicion)  # Salida: 11 (posición del primer carácter de "divertido")
   ```

4. **`replace(viejo, nuevo)` y `strip()`:**
   - `replace(viejo, nuevo)`: Reemplaza todas las ocurrencias de una subcadena con otra.
   - `strip()`: Elimina espacios en blanco al inicio y al final de la cadena.

   ```python
   mensaje = "   Hola, Python!   "

   sin_espacios = mensaje.strip()
   print(sin_espacios)  # Salida: Hola, Python!

   reemplazado = mensaje.replace("Python", "Programador")
   print(reemplazado)  # Salida:   Hola, Programador!   
   ```

Estos son solo algunos ejemplos de métodos de cadenas en Python. Puedes explorar más métodos y sus detalles en la documentación oficial de Python. Estos métodos son útiles para manipular y transformar cadenas según las necesidades de tu programa.


## Una tabla con algnos métodos más. 

| Método          | Descripción                                                   |
|-----------------|---------------------------------------------------------------|
| capitalize()    | Convierte la primera letra a mayúscula.                        |
| casefold()      | Convierte la cadena a minúsculas de manera más agresiva.       |
| center()        | Devuelve una cadena centrada.                                  |
| count()         | Devuelve el número de veces que ocurre un valor especificado en una cadena. |
| encode()        | Devuelve una versión codificada de la cadena.                  |
| endswith()      | Devuelve verdadero si la cadena termina con el valor especificado. |
| expandtabs()    | Establece el tamaño de la tabulación en la cadena.             |
| find()          | Busca en la cadena un valor especificado y devuelve la posición donde se encontró. |
| format()        | Formatea valores especificados en una cadena.                  |
| format_map()    | Formatea valores especificados en una cadena.                  |
| index()         | Busca en la cadena un valor especificado y devuelve la posición donde se encontró. |
| isalnum()       | Devuelve True si todos los caracteres en la cadena son alfanuméricos. |
| isalpha()       | Devuelve True si todos los caracteres en la cadena están en el alfabeto. |
| isascii()       | Devuelve True si todos los caracteres en la cadena son caracteres ASCII. |
| isdecimal()     | Devuelve True si todos los caracteres en la cadena son decimales. |
| isdigit()       | Devuelve True si todos los caracteres en la cadena son dígitos. |
| isidentifier()  | Devuelve True si la cadena es un identificador.                |
| islower()       | Devuelve True si todos los caracteres en la cadena están en minúsculas. |
| isnumeric()     | Devuelve True si todos los caracteres en la cadena son numéricos. |
| isprintable()   | Devuelve True si todos los caracteres en la cadena son imprimibles. |
| isspace()       | Devuelve True si todos los caracteres en la cadena son espacios en blanco. |
| istitle()       | Devuelve True si la cadena sigue las reglas de un título.      |
| isupper()       | Devuelve True si todos los caracteres en la cadena están en mayúsculas. |
| join()          | Convierte los elementos de un iterable en una cadena.          |
| ljust()         | Devuelve una versión justificada a la izquierda de la cadena.  |
| lower()         | Convierte una cadena a minúsculas.                             |
| lstrip()        | Devuelve una versión recortada a la izquierda de la cadena.    |
| maketrans()     | Devuelve una tabla de traducción para ser utilizada en traducciones. |
| partition()     | Devuelve una tupla donde la cadena se divide en tres partes.  |
| replace()       | Devuelve una cadena donde un valor especificado es reemplazado por otro valor especificado. |
| rfind()         | Busca en la cadena un valor especificado y devuelve la última posición donde se encontró. |
| rindex()        | Busca en la cadena un valor especificado y devuelve la última posición donde se encontró. |
| rjust()         | Devuelve una versión justificada a la derecha de la cadena.    |
| rpartition()    | Devuelve una tupla donde la cadena se divide en tres partes.  |
| rsplit()        | Divide la cadena en el separador especificado y devuelve una lista. |
| rstrip()        | Devuelve una versión recortada a la derecha de la cadena.      |
| split()         | Divide la cadena en el separador especificado y devuelve una lista. |
| splitlines()    | Divide la cadena en saltos de línea y devuelve una lista.      |
| startswith()    | Devuelve verdadero si la cadena comienza con el valor especificado. |
| strip()         | Devuelve una versión recortada de la cadena.                  |
| swapcase()      | Intercambia mayúsculas y minúsculas, minúsculas se convierten en mayúsculas y viceversa. |
| title()         | Convierte el primer carácter de cada palabra a mayúscula.     |
| translate()     | Devuelve una cadena traducida.                                 |
| upper()         | Convierte una cadena a mayúsculas.                             |
| zfill()         | Rellena la cadena con un número especificado de ceros al principio. |
