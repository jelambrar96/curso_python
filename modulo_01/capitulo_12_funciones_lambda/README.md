# Capítulo 12. Algo más sobre funciones y lambdas.

## Introducción a las Funciones Lambda en Python

Las funciones lambda en Python son una forma de crear funciones anónimas; es decir, funciones sin nombre. Estas son útiles para realizar operaciones rápidas o para transformar datos sin necesidad de definir una función con el tradicional `def`.

La sintaxis de una función lambda es la siguiente: 
```python
lambda argumentos: expresion
```

### Ejemplos de Funciones Lambda

- **Sumar dos números:** Ejemplo 
  ```python
  sumar = lambda x, y: x + y; print(sumar(5, 3))  # Salida: 8
  ```

- **Obtener el cuadrado de un número:** Ejemplo 
  ```python
  al_cuadrado = lambda numero: numero ** 2; print(al_cuadrado(4)) # Salida: 16
  ```

## Programación Funcional en Python

La programación funcional es un paradigma de programación que enfatiza el uso de funciones y el flujo de datos entre ellas. En Python, este paradigma se aplica mediante funciones y características que facilitan el trabajo con datos de forma más expresiva y menos imperativa.

### Ventajas de la Programación Funcional

- **Código más limpio y expresivo:** Al utilizar funciones puras, el código se vuelve más simple y fácil de entender.
- **Facilidad para depurar y mantener:** Las funciones puras y el flujo de datos claro hacen que el código sea más predecible y, por ende, más fácil de mantener.

El módulo `functools` en Python incluye una serie de herramientas que facilitan el trabajo con funciones de orden superior, que son aquellas que operan sobre otras funciones, ya sea aceptándolas como argumentos o devolviéndolas como resultado. Entre estas herramientas se destacan funciones como `reduce()`, y otras como `partial()`, `cmp_to_key()`, y `lru_cache()`. En esta discusión, nos enfocaremos en `reduce()`, así como en las funciones `map()` y `filter()`, que aunque no son parte de `functools`, están estrechamente relacionadas por su naturaleza funcional y su uso común en la programación funcional.

### Uso de `map()`
La función `map()` se utiliza para aplicar una función a cada elemento de un iterable (como una lista) y generar un nuevo iterable con los resultados. Por ejemplo, si queremos obtener el cuadrado de cada número en una lista, podemos hacerlo fácilmente con `map()`:

```python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))
```

Este código generará la salida `[1, 4, 9, 16, 25]`.

### Uso de `filter()`
La función `filter()` permite filtrar elementos de un iterable creando un nuevo iterable para los elementos que cumplen una determinada condición. Por ejemplo, si deseamos filtrar solo los números impares de una lista, podemos usar `filter()` de la siguiente manera:

```python
numbers = [1, 2, 3, 4, 5]
odd_numbers = filter(lambda x: x % 2 != 0, numbers)
print(list(odd_numbers))
```

Esto imprimirá `[1, 3, 5]`.

### Uso de `reduce()`
`reduce()` es una función de `functools` que se utiliza para reducir una colección de elementos a un solo valor, aplicando una función acumulativa. Es útil para operaciones que necesitan consolidar una serie de valores en uno solo, como sumar todos los elementos de una lista:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)
```

Esto dará como resultado `15`, que es la suma de todos los números en la lista.

### Aplicaciones prácticas
Estas herramientas son especialmente útiles en la programación funcional y pueden aplicarse en análisis de datos, procesamiento de señales, o cualquier contexto donde se necesite manipular colecciones de datos de manera eficiente.

- **Análisis de datos**: Puedes usar `map()` y `filter()` para preparar y limpiar datos, mientras que `reduce()` puede ayudarte a realizar cálculos agregados, como sumas, promedios o encontrar el mínimo/máximo.
- **Procesamiento en paralelo**: Al trabajar con grandes volúmenes de datos, `map()` y `filter()` se pueden paralelizar fácilmente para mejorar el rendimiento, ya que cada operación es independiente de las otras.
- **Cadena de transformaciones**: Es común encadenar `map()`, `filter()`, y `reduce()` para realizar transformaciones complejas y agregaciones en pasos claramente definidos.

Estas funciones promueven un estilo de código declarativo, lo que puede hacer que el código sea más expresivo y fácil de entender, especialmente en proyectos complejos donde la claridad y la eficiencia son cruciales.

## Argumentos `*args` y `**kwargs`

Estos argumentos especiales permiten a las funciones aceptar un número indefinido de argumentos. `*args` se usa para argumentos posicionales, mientras que `**kwargs` se refiere a argumentos con nombre.

#### Ejemplos

```python
# Uso de *args para sumar números
def suma(*args):
    return sum(args)

print(suma(1, 2, 3, 4))  # Salida: 10

# Uso de **kwargs para trabajar con argumentos nombrados
def info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

info(nombre='Alice', edad=30)  # Salida: nombre: Alice
                               #         edad: 30
```

En Python, los argumentos especiales `*args` y `**kwargs` son increíblemente útiles para escribir funciones flexibles y reutilizables. `*args` permite a una función aceptar un número arbitrario de argumentos posicionales, mientras que `**kwargs` acepta un número arbitrario de argumentos con nombre. Aquí te presento más ejemplos para enriquecer tu comprensión y mostrarte cómo estos pueden ser aplicados en diferentes contextos.

### Uso avanzado de `*args`

`*args` se usa no solo para sumar números, sino también puede ser útil en funciones donde necesitas operar con listas de elementos que varían en número, como en la construcción de una función que necesita multiplicar elementos, compararlos, o incluso combinar cadenas de texto.

```python
# Uso de *args para multiplicar números
def multiplicar(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

print(multiplicar(1, 2, 3, 4))  # Salida: 24

# Uso de *args para encontrar el mínimo de un conjunto de valores
def minimo(*args):
    return min(args)

print(minimo(10, 20, 5, 15))  # Salida: 5

# Uso de *args para concatenar cadenas
def concatenar(*args):
    return ' '.join(args)

print(concatenar("Hola", "mundo", "Python!"))  # Salida: Hola mundo Python!
```

### Uso avanzado de `**kwargs`

`**kwargs` es útil para trabajar con argumentos que requieren identificadores claros, como cuando se pasan propiedades a un objeto o configuraciones a una función. Esto es especialmente útil en funciones que configuran o inicializan objetos con múltiples atributos o en la creación de funciones que necesitan opciones de configuración flexibles.

```python
# Uso de **kwargs para configurar propiedades de un objeto
def crear_persona(**kwargs):
    edad = kwargs.get('edad', 30)  # Proporciona un valor predeterminado si 'edad' no está presente
    persona = {'nombre': kwargs['nombre'], 'edad': edad, 'profesion': kwargs.get('profesion', 'Desconocida')}
    return persona

persona = crear_persona(nombre='Juan', edad=35, profesion='Ingeniero')
print(persona)  # Salida: {'nombre': 'Juan', 'edad': 35, 'profesion': 'Ingeniero'}

# Uso de **kwargs en una función de configuración
def configurar(**kwargs):
    configuracion = {
        'color': kwargs.get('color', 'azul'),
        'tamaño': kwargs.get('tamaño', 'mediano'),
        'notificaciones': kwargs.get('notificaciones', True)
    }
    return configuracion

config = configurar(color='verde', notificaciones=False)
print(config)  # Salida: {'color': 'verde', 'tamaño': 'mediano', 'notificaciones': False}
```

Estos ejemplos muestran cómo `*args` y `**kwargs` pueden hacer que las funciones de Python sean más versátiles y cómo pueden manejar diferentes tipos de datos y requerimientos funcionales de manera eficiente. Su uso facilita la escritura de código limpio y adaptable, que puede manejar una variedad de situaciones sin necesidad de sobrecargar la función con demasiados parámetros.

____

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

Enero 2024