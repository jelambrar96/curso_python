# Capítulo 3. Almacenando valores en Python. Variables, tipos de datos y conversiones. 

En este capítulo vamos a trabajar con las variables en Python. 

## Variables en Python

![](media/image_3_1.jpeg)


En programación, una variable es un **contenedor para almacenar datos**. Estos datos pueden ser de diferentes tipos, como números, cadenas de texto, listas, etc. Las variables se utilizan para almacenar información que puede cambiar durante la ejecución de un programa.

En Python, crear una variable es muy sencillo. Simplemente eliges un nombre para la variable y luego le asignas un valor utilizando el **operador de asignación** (`=`). Por ejemplo:

```python
# Creando una variable llamada "edad" y asignándole el valor 25
edad = 25

# Creando una variable llamada "nombre" y asignándole el valor "Jorge"
nombre = "Jorge"

# Creando una variable llamada "pi" y asignándole el valor 3.14159
pi = 3.14159

# Creando una variable llamada "algo" y asignándole el valor None
algo = None

# Creando una variable llamada "bandera" y asignándole el valor True
bandera = True
```

En el ejemplo anterior, "edad", "nombre", "pi", "algo" y "bandera" son los nombres de las variables, y les hemos asignado los valores 25, "Jorge",  3.14159, None y True (VERDADERO) respectivamente.

Es importante tener en cuenta que en Python no es necesario declarar explícitamente el tipo de dato que contendrá la variable, ya que Python es un lenguaje de tipado dinámico. Esto significa que el tipo de dato de la variable se infiere automáticamente según el valor que se le asigna.

## Python es un lenguaje de programación CaseSensitive

Python es un lenguaje de programación "case-sensitive". Eso significa que distingue entre mayúsculas y minúsculas. Es decir, Python considera que las letras mayúsculas y minúsculas son diferentes. Aquí tienes un ejemplo para ilustrar esto:

**Ejemplo: Variables con nombres similares pero con diferente capitalización**

```python
# Variables con nombres similares pero con diferente capitalización
edad = 25
Edad = 30

# Las variables son diferentes debido a la capitalización
print(edad)  # Imprime 25
print(Edad)  # Imprime 30
```

En este ejemplo, `edad` y `Edad` son dos variables diferentes porque la primera letra tiene diferente capitalización.

## Tipos de datos básicos en Python

![](media/image_3_2.jpeg)

Las variables pueden ser clasificadas según el tipo de dato que contegan. Esta clasificación permite que se puedan separa las variables en grupos con características y propiedades determinadas. De esta manera, los tipos de datos determinan los valores que puede o no tomar una variable y qué operaciones es posible realizar con ellas. 

### Datos de tipo numérico

En Python, existe un tipo de datos Número para todas las operaciones que involucran valores numéricos.

- Datos de tipo entero **int**. Este tipo de dato se utiliza para representar números enteros, positivos o negativos, sin parte decimal. Por ejemplo: 5, -3, 1000.
- Datos de tipo flotante **float**. Los números de punto flotante se utilizan para representar números reales, es decir, aquellos que tienen una parte decimal. Por ejemplo: 3.14, -0.001, 2.0.
- Datos de tipo complejo **complex**. Se utilizan para representar números que tengan una parte decimal y una parte imaginaria. Por ejemplo: 2.0 + 1.4j.
- Datos de tipo cadena. Se utilizan para representar texto. Las cadenas de texto se pueden definir utilizando comillas simples (```''```) o dobles (```""```). Por ejemplo: ```"Hola, mundo"```, ```'Python es genial'```.
- Datos de tipo boleano. Este tipo de dato solo puede tener dos valores: True (verdadero) o False (falso). Se utilizan para representar valores de verdad. Por ejemplo: True, False.
- El tipo ```None```. Este tipo de dato se utiliza para representar la ausencia de valor. Es útil cuando queremos inicializar una variable pero no queremos asignarle un valor específico en ese momento.

Además de estos tipos de datos básicos, Python también tiene estructuras de datos más complejas, como listas, tuplas, conjuntos y diccionarios, que permiten almacenar colecciones de datos. Pero de ellas hablaremos en otro capítulo. 

## Conocer el tipo de dato de una variable: la función ```type()```

![](media/image_3_3.jpeg)

En Python, la función `type()` se utiliza para obtener el tipo de datos de un objeto. Puedes pasar cualquier objeto como argumento a la función `type()` y te devolverá el tipo de datos al que pertenece ese objeto.

Aquí tienes un ejemplo sencillo de cómo se utiliza la función `type()`:

```python
x = 5
y = "Hola, mundo"
z = 3.14

print(type(x))  # Esto imprimirá <class 'int'>
print(type(y))  # Esto imprimirá <class 'str'>
print(type(z))  # Esto imprimirá <class 'float'>
```

En este ejemplo, la función `type()` se utiliza para imprimir el tipo de datos de las variables `x`, `y` y `z`, que contienen un entero, una cadena de texto y un número de punto flotante respectivamente.

La función `type()` es útil cuando necesitas verificar el tipo de datos de un objeto en Python, lo que puede ser útil en situaciones donde necesitas asegurarte de que estás trabajando con el tipo de datos correcto.

## Conversión de tipo de datos

![](media/image_3_4.jpeg)


En Python, el cambio de tipo se refiere a la conversión de un tipo de datos a otro. Python proporciona varias funciones integradas para realizar conversiones de tipo. Aquí tienes una descripción detallada de algunas de las conversiones de tipo más comunes:

1. **Cambio a Entero (int):** Puedes convertir otros tipos de datos a enteros utilizando la función `int()`. Por ejemplo:
   ```python
   x = int(3.14)  # Esto convierte el número de punto flotante 3.14 a un entero (3)
   y = int("5")   # Esto convierte la cadena de texto "5" a un entero (5)
   ```

2. **Cambio a Flotante (float):** Puedes convertir otros tipos de datos a números de punto flotante utilizando la función `float()`. Por ejemplo:
   ```python
   x = float(5)    # Esto convierte el entero 5 a un número de punto flotante (5.0)
   y = float("3.14")  # Esto convierte la cadena de texto "3.14" a un número de punto flotante (3.14)
   ```

3. **Cambio a Cadena de Texto (str):** Puedes convertir otros tipos de datos a cadenas de texto utilizando la función `str()`. Por ejemplo:
   ```python
   x = str(123)    # Esto convierte el entero 123 a una cadena de texto ("123")
   y = str(3.14)   # Esto convierte el número de punto flotante 3.14 a una cadena de texto ("3.14")
   ```

Es importante tener en cuenta que no todas las conversiones de tipo son posibles o tienen sentido. Por ejemplo, no puedes convertir una cadena de texto que no representa un número a un entero o un flotante sin antes realizar un análisis o validación.

El cambio de tipo es una herramienta útil para manipular datos en Python y asegurarte de que estás trabajando con el tipo de datos correcto en tu programa.

## Una característica de Python: El tipado dinámico. 

![](media/image_3_5.jpeg)


En Python, el tipado dinámico se refiere a la capacidad del lenguaje para asignar automáticamente el tipo de datos a una variable en tiempo de ejecución. Esto significa que en Python no es necesario declarar explícitamente el tipo de una variable al crearla; el tipo de la variable se infiere automáticamente según el valor que se le asigna.

Por ejemplo, en Python puedes hacer lo siguiente:

```python
x = 5      # x es un entero
x = "Hola" # x ahora es una cadena de texto
x = 3.14   # x ahora es un número de punto flotante
```

En este ejemplo, la variable `x` cambia de tipo dinámicamente a medida que se le asignan diferentes valores. En otros lenguajes de programación, como C++ o Java, tendrías que declarar el tipo de `x` al crearla y no podrías cambiar ese tipo más adelante.

El tipado dinámico en Python proporciona flexibilidad y conveniencia, ya que te permite escribir código de manera más concisa y centrarte en la lógica del programa en lugar de preocuparte por los tipos de datos.

Sin embargo, el tipado dinámico también requiere que los programadores sean conscientes de los tipos de datos con los que están trabajando, ya que los errores de tipo pueden ocurrir si no se manejan adecuadamente.

## Ten cuidado con las palabras reservadas 

![](media/image_3_6.jpeg)


En Python, existen ciertas palabras que están reservadas para realizar funciones específicas en el lenguaje. Estas palabras reservadas tienen un significado especial y no pueden ser utilizadas como nombres de variables, funciones u otros identificadores en tu código. Intentar usar una palabra reservada como nombre de variable resultará en un error.

Aquí hay algunas palabras reservadas comunes en Python:

|                   |                   |                   |                   |
|-------------------|-------------------|-------------------|-------------------|
| and               | as                | assert            | break             |
| class             | continue          | lambda            | def               |
| elif              | else              | exec              | except            |
| finally           | for               | from              | global            |
| if                | import            | in                | is                |
| not               | or                | pass              | print             |
| raise             | return            | try               | while             |
| with              | yield             |                   |                   |

```python
and = 5 # Esto genera una error
```

____

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

Enero 2024