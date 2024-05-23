# Capítulo 9. Condicionales y operador ternario.

Un condicional en programación es una estructura que permite que un programa tome decisiones basadas en la evaluación de una expresión booleana (que resulta en `True` o `False`). Los condicionales son fundamentales para el control de flujo en un programa, permitiendo que ciertas partes del código se ejecuten o no, dependiendo de las condiciones especificadas.

### Estructura básica de un condicional en Python:

![](media/image_9_1.jpeg)

Esta es la estructura básica de un condicional en python. La condición es una expresión cuyo resultado puede ser interpretado como `True` o `False`. Los bloques son corresponden a las expresiones que se ejecutarán si la condición es Verdadera o Falsa.

```python
if condicion:
    # Bloque de código si la condición es verdadera
else:
    # Bloque de código si la condición es falsa
```

Nota la sangría (muchas veces llamado indentado) de los bloques de código. La indentación en Python es un aspecto fundamental de la sintaxis del lenguaje y se utiliza para estructurar el código de manera significativa. En Python, la indentación se refiere a la cantidad de espacios o tabulaciones que preceden a una línea de código. La indentación se usa para delimitar bloques de código dentro de estructuras de control, funciones, clases y otros bloques de código.

Si no aplicas el sangrado en una expresión de condicional se generará un error. 

```python
if True: 
print("Esto va a generar un error" ) # Esto va a generar un error
```

```python
if True: 
    print("Esto funciona" ) # imprime "Esto funciona" 
```

### Funcionamiento de un condicional:

![](media/image_9_2.jpeg)

1. **Evaluación de la condición:** Se evalúa la expresión booleana después del `if`.
2. **Ejecución del bloque correspondiente:** Si la condición es `True`, se ejecuta el bloque de código bajo el `if`; de lo contrario, se ejecuta el bloque bajo el `else`.

### Uso de condicionales:

- **Tomar decisiones:** Permite que el programa ejecute diferentes bloques de código según la situación.
- **Control de flujo:** Determina cómo el programa se mueve a través de sus instrucciones.
- **Manejo de casos especiales:** Puede usarse para manejar situaciones específicas y tomar acciones en consecuencia.

### Valores para los cuales un condicional es verdadero:

Un condicional en Python se considera verdadero (`True`) cuando la expresión booleana después del `if` se evalúa como verdadera. Algunos ejemplos de condiciones verdaderas pueden ser:

- Comparaciones de números (`a > b`, `x <= y`, `x == y`, `x != y`).
- Verificar si un elemento está en una lista o cadena (`elemento in lista`).
- Comprobar si una cadena no está vacía (`len(cadena) > 0`).
- Evaluaciones de verdad (`True` es siempre verdadero).

### Ejemplos de condicionales en Python:

![](media/image_9_3.jpeg)

#### Ejemplo 1: Condición numérica

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

#### Ejemplo 2: Condición de pertenencia

```python
frutas = ['manzana', 'naranja', 'plátano']

if 'pera' in frutas:
    print("La pera está en la lista de frutas.")
else:
    print("La pera no está en la lista de frutas.")
```

#### Ejemplo 3: Condición de verdad

```python
verdadero = True

if verdadero:
    print("La condición es verdadera.")
else:
    print("La condición es falsa.")
```

Los condicionales son esenciales para construir programas que pueden tomar decisiones dinámicamente en función de las condiciones cambiantes durante la ejecución del programa.

### Condicionales Anidados:

![](media/image_9_7.jpeg)


Los condicionales anidados se refieren a la inclusión de un condicional dentro de otro. Esto se hace al colocar un bloque `if` dentro de otro bloque `if` o `else`. Los condicionales anidados permiten evaluar múltiples condiciones de manera jerárquica.

**Ejemplo de condicionales anidados:**

```python
edad = 25

if edad >= 18:
    print("Eres mayor de edad.")
    if edad >= 21:
        print("También puedes beber alcohol en Estados Unidos.")
else:
    print("Eres menor de edad.")
```

### Condicionales en Cascada:

![](media/image_9_6.jpeg)


Los condicionales en cascada, también conocidos como `elif` (contracción de "else if"), permiten evaluar múltiples condiciones en secuencia sin necesidad de anidamiento excesivo. La palabra reservada `elif` se utiliza para agregar condiciones adicionales después de un `if` inicial.

**Ejemplo de condicionales en cascada con `elif`:**

```python
puntuacion = 75

if puntuacion >= 90:
    print("A")
elif puntuacion >= 80:
    print("B")
elif puntuacion >= 70:
    print("C")
elif puntuacion >= 60:
    print("D")
else:
    print("F")
```

En este ejemplo, cada bloque `elif` se evalúa solo si las condiciones anteriores son falsas. La evaluación sigue en orden y el primer bloque cuya condición sea verdadera se ejecutará, evitando la necesidad de verificar todas las condiciones.

### Ejemplo combinando condicionales anidados y en cascada:

![](media/image_9_5.jpeg)


```python
temperatura = 28

if temperatura > 30:
    print("Hace mucho calor.")
elif temperatura > 20:
    print("El clima es agradable.")
    if temperatura <= 25:
        print("Puedes disfrutar al aire libre.")
    else:
        print("Quizás sea un poco caliente para algunas personas.")
else:
    print("Hace frío.")
```

En este ejemplo, se utiliza un condicional en cascada para evaluar diferentes rangos de temperatura, y dentro de uno de los bloques se incorpora un condicional anidado para realizar evaluaciones adicionales.

Ambos conceptos, condicionales anidados y condicionales en cascada, son útiles para estructurar el flujo de control de un programa y tomar decisiones basadas en múltiples condiciones.

## El operador ternario 

![](media/image_9_4.jpeg)


En Python, el operador ternario es una forma concisa de escribir una expresión condicional en una sola línea. También se conoce como el operador condicional o expresión ternaria. Su sintaxis es la siguiente:

```python
resultado_si_verdadero if condicion else resultado_si_falso
```

Esto se traduce como "resultado_si_verdadero" si la "condicion" es verdadera, y "resultado_si_falso" en caso contrario.

### Ejemplos de operador ternario:

#### Ejemplo 1: Verificar si un número es par o impar

```python
numero = 15
resultado = "par" if numero % 2 == 0 else "impar"
print(resultado)
# Imprime "impar"
```

#### Ejemplo 2: Asignar un valor basado en la condición

```python
puntuacion = 85
estado = "Aprobado" if puntuacion >= 70 else "Reprobado"
print(estado)
# Imprime "Aprobado"
```

#### Ejemplo 3: Operador ternario anidado

```python
edad = 25
grupo_etario = "Adulto" if edad >= 18 else ("Adolescente" if edad >= 13 else "Niño")
print(grupo_etario)
# Imprime "Adulto"
```

En este último ejemplo, el operador ternario se utiliza de manera anidada para asignar un valor a `grupo_etario` en función de la edad.

El operador ternario es una herramienta útil para escribir expresiones condicionales de forma más concisa, especialmente cuando el resultado de la condición es simple. Sin embargo, es importante no abusar de su uso para mantener la legibilidad del código.

____

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

Enero 2024