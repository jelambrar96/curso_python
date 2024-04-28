# Capítulo 11. Excepciones y manejo de excepciones. 

## Introducción a las Excepciones en Programación

Las excepciones son situaciones o eventos que pueden alterar el flujo normal de ejecución de un programa. En programación, las excepciones ocurren cuando sucede algo inesperado que el código no está preparado para manejar de manera ordinaria, como un error de división por cero o un archivo que no se puede encontrar. El manejo adecuado de excepciones es crucial para construir programas robustos que puedan gestionar errores sin romperse y proporcionar retroalimentación útil al usuario o al desarrollador.

![](media/image_13_01.jpeg)

## ¿Qué es una excepción en Python?

Una excepción en Python es un evento que se activa durante la ejecución de un programa que interrumpe el flujo normal de las instrucciones. En Python, las excepciones son tratadas como objetos que representan un error o una condición inusual. Cuando una excepción es lanzada, el flujo normal del programa se interrumpe, y Python intentará encontrar un manejo de excepciones correspondiente definido en el código.

### ¿En qué casos se aplican las excepciones?

Las excepciones se utilizan en situaciones donde pueden ocurrir errores durante la ejecución del programa que no se pueden prever fácilmente al momento de escribir el código. Ejemplos típicos incluyen:

- Intentar abrir un archivo que no existe.
- Dividir un número por cero.
- Operaciones en tipos de datos incompatibles.
- Acceder a elementos fuera del rango en listas.

## Sintaxis de una Excepción en Python

![](media/image_13_07.jpeg)

La sintaxis básica para manejar excepciones en Python involucra los bloques `try` y `except`:

```python
try:
    # Código que puede lanzar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si hay una excepción ZeroDivisionError
    print("No se puede dividir por cero")
```

En Python, el manejo de excepciones se realiza principalmente mediante el uso de los bloques `try`, `except`, `else`, y `finally`. Estas palabras reservadas permiten manejar errores de manera más controlada y realizar acciones específicas dependiendo de si ocurre o no una excepción.

### `try`

El bloque `try` permite probar un bloque de código en busca de errores. Es decir, el código dentro del bloque `try` es el que Python intentará ejecutar, y si ocurre un error durante su ejecución, Python saltará al bloque `except` correspondiente.

### `except`

El bloque `except` captura la excepción y permite ejecutar un bloque de código cuando se produce un error en el bloque `try`. Puedes especificar tipos específicos de excepciones que quieres capturar. Si no especificas un tipo, se capturarán todas las excepciones.

### `else`

El bloque `else` es opcional y, si se incluye, debe seguir a todos los bloques `except`. El código dentro del bloque `else` se ejecutará si el código dentro del bloque `try` se ejecutó sin lanzar una excepción.

### `finally`

El bloque `finally` también es opcional y se ejecutará al final de todos los bloques, independientemente de si se lanzó una excepción y de si fue capturada o no. Es útil para realizar acciones de limpieza que deben realizarse sin importar si ocurrió un error, como cerrar archivos o liberar recursos externos.

### Ejemplos

#### Ejemplo de uso de `try`, `except`, `else`, y `finally`:

```python
def dividir(x, y):
    try:
        resultado = x / y
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
    else:
        print(f"El resultado es {resultado}")
    finally:
        print("Ejecutando el bloque finally.")

dividir(10, 2)
dividir(10, 0)
```

**Explicación**:
- En el primer llamado a `dividir(10, 2)`, el bloque `try` ejecuta correctamente la división, no ocurre ninguna excepción, por lo que se ejecuta el bloque `else` y se imprime el resultado. Independientemente del resultado, se ejecuta el bloque `finally`.
- En el segundo llamado a `dividir(10, 0)`, el bloque `try` intenta ejecutar la división por cero, lo que lanza una excepción `ZeroDivisionError`. El bloque `except` captura esta excepción e imprime un mensaje. Finalmente, el bloque `finally` se ejecuta.

#### Ejemplo con múltiples `except`:

```python
def convertir_a_entero(valor):
    try:
        resultado = int(valor)
    except ValueError:
        print("Por favor, proporciona un número entero válido.")
    except TypeError:
        print("El tipo de dato no es apropiado para la conversión a entero.")
    else:
        print(f"Conversión exitosa: {resultado}")
    finally:
        print("Intento de conversión finalizado.")

convertir_a_entero('123')  # Entrada válida
convertir_a_entero('abc')  # Entrada que causa ValueError
convertir_a_entero(None)   # Entrada que causa TypeError
```

**Explicación**:
- `convertir_a_entero('123')` no produce errores, por lo que se ejecutan los bloques `else` y `finally`.
- `convertir_a_entero('abc')` produce un `ValueError`, capturado por el primer bloque `except`, y luego se ejecuta `finally`.
- `convertir_a_entero(None)` produce un `TypeError`, que es capturado por el segundo bloque `except`, seguido por la ejecución de `finally`.

Estos ejemplos demuestran cómo los diferentes bloques trabajan juntos para manejar diferentes situaciones en la ejecución del programa, permitiendo que el código sea más robusto y fácil de mantener.

### Excepciones Comunes en Python

![](media/image_13_03.jpeg)

Python define varias excepciones incorporadas que pueden manejar situaciones comunes en la mayoría de los programas. Algunas de las más comunes incluyen:

- `ZeroDivisionError`: Ocurre cuando un número es dividido por cero.
- `FileNotFoundError`: Se lanza cuando un archivo o directorio no existe.
- `TypeError`: Sucede cuando una operación o función se aplica a un objeto de tipo inapropiado.
- `IndexError`: Se produce cuando se intenta acceder a un índice fuera del rango de una lista o tupla.
- `ValueError`: Se produce cuando se intenta realizar una operación no soportada sobre una variable, como sumar un número con una cadena. 


### Manejo de Múltiples Excepciones

Es posible manejar múltiples excepciones a la vez utilizando una tupla de excepciones en un solo `except`:

```python
try:
    # Código que puede lanzar varias excepciones
    pass
except (TypeError, ValueError) as error:
    print(f"Se encontró un error: {error}")
```

## Las palabras reservadas `raise` y `assert`

![](media/image_13_04.jpeg)

En Python, las palabras reservadas `raise` y `assert` juegan roles importantes en el manejo de excepciones, aunque de maneras ligeramente diferentes. Ambas se utilizan para controlar el flujo del programa, especialmente para validar condiciones y manejar errores.

### Uso de `raise`

La palabra reservada `raise` se utiliza para forzar la ocurrencia de una excepción específica en Python, lo cual puede ser útil cuando deseas asegurarte de que ciertas condiciones erróneas en tu programa no pasen desapercibidas. Es fundamental en la implementación de verificaciones que no pueden o no deben ser manejadas de forma silenciosa.

#### Ejemplo con `raise`:
```python
def verificar_edad(edad):
    if edad < 18:
        raise ValueError("Acceso denegado. Debes tener al menos 18 años.")
    return "Acceso concedido."

try:
    resultado = verificar_edad(17)
except ValueError as e:
    print(e)
```
**Explicación**: Este código define una función que verifica si un usuario es mayor de edad. Si el usuario tiene menos de 18 años, se lanza una excepción `ValueError` con un mensaje específico. Esta excepción se maneja en el bloque `except`, donde se captura y se imprime el mensaje de error.

### Uso de `assert`

La palabra reservada `assert` se utiliza para establecer una condición de verificación dentro del código. Si la condición evaluada por `assert` es `True`, el programa continúa su ejecución normal; si es `False`, `assert` lanza una excepción `AssertionError`. Esta herramienta es útil para hacer debug y verificar que el estado interno de un programa sea como se espera durante el desarrollo.

#### Ejemplo con `assert`:
```python
def calcular_promedio(calificaciones):
    assert len(calificaciones) > 0, "La lista de calificaciones no puede estar vacía"
    return sum(calificaciones) / len(calificaciones)

try:
    promedio = calcular_promedio([])
except AssertionError as e:
    print(e)
```
**Explicación**: En este ejemplo, `assert` verifica que la lista de calificaciones no esté vacía antes de calcular el promedio. Si se pasa una lista vacía, `assert` lanza un `AssertionError` con un mensaje que indica que la lista no puede estar vacía. Este error se captura y maneja en el bloque `except`.

### Relación con el manejo de excepciones

Tanto `raise` como `assert` se relacionan con el manejo de excepciones porque ambos pueden lanzar errores que deben ser capturados y manejados para prevenir que el programa falle abruptamente. La diferencia principal es que `raise` se usa para lanzar excepciones específicas y controladas por el programador, mientras que `assert` está más orientado a la verificación de condiciones que deben cumplirse para que el programa continúe su ejecución de manera segura. `assert` es principalmente una herramienta de debugging que puede ser desactivada en entornos de producción ejecutando Python con la opción `-O` (optimize), lo cual no afecta a `raise`.

## Creando Tus Propias Excepciones

![](media/image_13_05.jpeg)

Puedes definir tus propias excepciones creando una clase que herede de `Exception` o de cualquier otra excepción incorporada:

```python
class MiError(Exception):
    pass

try:
    raise MiError("Ha ocurrido un error personalizado")
except MiError as error:
    print(error)
```

### Buenas Prácticas en el Uso de Try-Except

![](media/image_13_06.jpeg)

- **Especificar excepciones**: Captura excepciones específicas en lugar de usar un bloque `except` general.

```python
def dividir_numeros(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except TypeError:
        print("Error: Todos los operandos deben ser numéricos.")

# Uso correcto
dividir_numeros(10, 2)
# Intento de división por cero
dividir_numeros(10, 0)
# Error de tipo
dividir_numeros(10, 'a')
```

- **Minimizar el código dentro de `try`**: Solo incluye el código que puede generar la excepción que deseas capturar.

```python
def obtener_elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        print(f"Error: No existe el índice {indice} en la lista.")

# Uso correcto
lista = [1, 2, 3]
obtener_elemento(lista, 1)
# Índice fuera de rango
obtener_elemento(lista, 5)
```

- **Uso de `finally`**: Siempre limpia recursos (como archivos o conexiones de red) en el bloque `finally`, que se ejecuta independientemente de si se lanzó una excepción.

```python
def manejar_archivo():
    try:
        f = open("archivo.txt", "r")
        lineas = f.readlines()
        print(lineas)
    except FileNotFoundError:
        print("Error: El archivo no existe.")
    finally:
        f.close()
        print("El archivo fue cerrado correctamente.")

manejar_archivo()
```

- **Documentar las excepciones**: Documenta las excepciones que tu código puede lanzar, especialmente si escribes una biblioteca.

```python
def calcular_raiz_cuadrada(numero):
    """
    Calcula la raíz cuadrada de un número.
    
    Parámetros:
    numero (float): Un número del cual calcular la raíz cuadrada.

    Devuelve:
    float: La raíz cuadrada del número.

    Excepciones:
    ValueError: Si el número es negativo.
    """
    if numero < 0:
        raise ValueError("El número no puede ser negativo.")
    return numero ** 0.5

try:
    resultado = calcular_raiz_cuadrada(-1)
except ValueError as e:
    print(e)

```

Este enfoque proporciona una base sólida para que los estudiantes entiendan cómo y por qué manejar errores en Python, ayudándoles a escribir programas más seguros y fáciles de mantener.

____

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

Enero 2024