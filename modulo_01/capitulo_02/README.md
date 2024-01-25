# Capítulo 2. La función print y la impresión de datos en la consola. 

En este capítulo se presenta el primer paso para el aprendizaje de este lenguaje de programación: imprimir desde la consola. La impresión de datos por consola nos permite mostrar el valor delas variables que se encuentran dentro de la aplicación, hacer logging y mucho más. 

## La función print()

### Lo más básico

La función ```print()``` en Python se utiliza para mostrar información en la consola o en otro dispositivo de salida. Puede imprimir cadenas de texto, variables, números y otros tipos de datos.

La función print() es una herramienta útil para mostrar información mientras se desarrolla y depura código en Python.

Funciona de la siguiente manera:

```python
print("Hola, mundo!")
```

En este ejemplo, la función print() muestra el texto "Hola, mundo!" en la consola. 

Cuando se utilizan comillas simples ```''``` en lugar de comillas dobles ```""```, se tiene el mismo resultado. 

```python
print('Hola, mundo!')
```

```plain
Hola mundo!
```


### Imprimiendo otros tipos de datos

Además de cadenas de texto la función print es capaz de imprimir números enteros y con parte decimas. También puede imprimir otros tipos de datos como **boolean**: ```True``` y ```False```

```python
print(0)
print(-5)
print(2.59)
print(True)
print(False)
```

En este ejemplo, las funciones print muentran los siguientes textos:

```plain
0
-5
2.59
True
False
```

Note que cada funcion print imprime en una línea diferente. 

### Imprimiendo más de un dato a la vez

En el ejemplo anterior se utilizaron funciones ```print()``` para mostrar por pantalla una serie de datos. Sin embargo, la función ```print()``` es capaz de imprimir más de un dato a la vez. Para ello, basta con separar cada uno de los datos por comas, como se muestra en este ejemplo. 

```python
print("Buenos", "Días")
```

La salida del código anterior es: 

```plain 
Buenos Días
```

Los diferentes valores que se impriman al tiempo pueden ser de diferentes tipos. Miremos este ejempo. 
```python
print("Buenos", "Días", 0, -5, 2.59, True, False)
```

Como resultado del código anterior se tiene:

```plain 
Buenos Días 0 -5 2.59 True False
```

Python de forma predeterminada separa los datos con un espacio en blanco ```' '```. Sin embargo, es posible reemplazarlo con otro algún otro valor. 

### Imprimiendo más de un dato a la vez y agregando un separador

En Python, la función print() tiene un parámetro opcional llamado "sep" que se utiliza para especificar el separador entre los elementos que se van a imprimir. Por defecto, el separador es un espacio en blanco.

Por ejemplo:

```python
print("a", "b", "c")
```

Esto imprimirá:

```plain
a b c
```

Pero si especificamos un separador diferente utilizando el parámetro "sep":

```python
print("a", "b", "c", sep="-")
```

Esto imprimirá:

```plain
a-b-c
```

En este caso, el guion ("-") se utiliza como separador en lugar del espacio en blanco predeterminado. El parámetro "sep" es útil cuando se quiere controlar cómo se separan los elementos que se imprimen en la consola.

### Eliminando el salto de línea 

En Python, el salto de línea en la función print() se maneja de forma automática al imprimir cada elemento. Por defecto, al imprimir un elemento, la función print() agrega un salto de línea al final.

Por ejemplo:

```python
print("Primera línea")
print("Segunda línea")
```

Esto imprimirá:

```plain
Primera línea
Segunda línea
```

Si se desea evitar el salto de línea al final de la impresión, se puede utilizar el parámetro "end" para especificar un carácter diferente al final de la impresión. Por ejemplo:

```python
print("Primera línea", end=" ")
print("Segunda línea")
```

Esto imprimirá:

```python
Primera línea Segunda línea
```

En este caso, se utilizó un espacio en blanco como el carácter final en lugar del salto de línea predeterminado. Esto puede ser útil cuando se quiere controlar el formato de la salida en la consola.


### Imprimiendo otras cosas bombitas

Existen cadenas de más de una linea, la función ```print()``` puede imprimir datos de más de una linea. 

```python
print("""Hola,
¿Cómo estas?""")
```

La salida de este código es

```plain
Hola,
¿Cómo estás?
```

Finalmente, la función print() de Python es capaz de manejar caracteres especiales como el salto de línea ```'\n'``` y el salto de carro ```'\r'```. Veamos el siguiente ejemplo: 

```python
print('line1\r\nline2\r\nline3')
```

Donde la salida es la siguiente: 

```plain


line3
```

## Comentarios 

En Python, un comentario es una parte del código que no se ejecuta y se utiliza para hacer anotaciones o explicaciones sobre el código. Los comentarios son útiles para hacer que el código sea más legible para otros programadores (o para ti mismo en el futuro) y para explicar el propósito de ciertas partes del código.

En Python, hay dos formas de hacer comentarios. El primero es usando el símbolo de numeral (#). Todo lo que sigue a este símbolo en la misma línea se considera un comentario y no se ejecutará. Por ejemplo:

```python
# Este es un comentario en Python
print("Hola, mundo")  # Este también es un comentario

```

La segunda forma de hacer comentarios es utilizando tres comillas simples (```'''```) o tres comillas dobles (```"""```). Todo lo que esté dentro de estas comillas se considerará un comentario. Este tipo de comentario es útil para comentarios de varias líneas. Por ejemplo:

```python
'''
Este es un comentario
de varias líneas
en Python
'''
print("Hola, mundo")
```

### References

- Your Guide to the Python print() Function. Real Pyth. https://realpython.com/python-print/

____

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

Enero 2024