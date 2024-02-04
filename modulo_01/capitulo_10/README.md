# Capítulo 10. Bucles: while, for y la palabra reservada ```break```.

En programación, los bucles (o loops) permiten ejecutar un bloque de código repetidamente, hasta que se cumpla una condición especificada. Aquí tienes información sobre los bucles más comunes en Python:

### 2. Bucle `while`:

El bucle `while` se utiliza para ejecutar un bloque de código mientras una condición sea verdadera. Es importante asegurarse de que la condición eventualmente sea falsa para evitar un bucle infinito.

**Ejemplo de bucle `while`:**

```python
contador = 0

while contador < 5:
    print(contador)
    contador += 1
# Imprime:
# 0
# 1
# 2
# 3
# 4
```


Los bucles while son útiles cuando no se conoce de antemano cuántas veces se ejecutará el bloque de código y se desea que el código se repita mientras una condición sea verdadera. Sin embargo, es importante tener cuidado para evitar bucles infinitos asegurándose de que la condición eventualmente sea falsa.

### Uso de bucles while:

- Iteración hasta que se cumpla una condición: Se utilizan cuando no se conoce de antemano el número exacto de iteraciones, pero se desea que el bloque de código se ejecute mientras una condición sea verdadera.
- Evitar bucles infinitos: Es importante asegurarse de que la condición eventualmente se vuelva falsa para evitar bucles infinitos.


### 1. Bucle `for`: Iterando sobre una lista, tupla o conjunto. 

El bucle `for` se utiliza para iterar sobre una secuencia (como una lista, tupla, cadena o rango) y ejecutar un bloque de código para cada elemento de la secuencia.

**Ejemplo de bucle `for`:**

```python
frutas = ["manzana", "naranja", "plátano"]

for fruta in frutas:
    print(fruta)
# Imprime:
# manzana
# naranja
# plátano
```

### 3. Bucle `for` con `range()`:

La función `range()` se utiliza comúnmente con el bucle `for` para generar una secuencia de números.

**Ejemplo de bucle `for` con `range()`:**

```python
for i in range(5):
    print(i)
# Imprime:
# 0
# 1
# 2
# 3
# 4
```

### 4. Bucle `for` con `enumerate()`:

La función `enumerate()` se utiliza con el bucle `for` para obtener tanto el índice como el valor de cada elemento en la secuencia.

**Ejemplo de bucle `for` con `enumerate()`:**

```python
frutas = ["manzana", "naranja", "plátano"]

for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")
# Imprime:
# Índice 0: manzana
# Índice 1: naranja
# Índice 2: plátano
```

### 5. Iterando diccionarios

Sí, como desarrollador Python, puedo explicarte cómo puedes iterar sobre un diccionario. En Python, hay varias formas de recorrer (iterar) un diccionario para acceder a sus claves, valores o ambos. Aquí tienes algunas técnicas comunes:

### 1. Iterar sobre las claves:

Puedes utilizar el bucle `for` para iterar sobre las claves de un diccionario utilizando el método `keys()`:

```python
mi_diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Bogotá'}

for clave in mi_diccionario.keys():
    print(clave)
# Imprime:
# nombre
# edad
# ciudad
```

### 2. Iterar sobre los valores:

Puedes utilizar el bucle `for` para iterar sobre los valores del diccionario utilizando el método `values()`:

```python
mi_diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Bogotá'}

for valor in mi_diccionario.values():
    print(valor)
# Imprime:
# Juan
# 25
# Bogotá
```

### 3. Iterar sobre los pares clave-valor:

Puedes utilizar el bucle `for` para iterar sobre los pares clave-valor del diccionario utilizando el método `items()`:

```python
mi_diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Bogotá'}

for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")
# Imprime:
# nombre: Juan
# edad: 25
# ciudad: Bogotá
```

### 4. Iterar con desempaquetado de items:

Puedes desempaquetar los items directamente en el bucle `for`:

```python
mi_diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Bogotá'}

for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")
# Imprime:
# nombre: Juan
# edad: 25
# ciudad: Bogotá
```

### 5. Iterar utilizando dict.items() en una lista:

Puedes convertir el diccionario en una lista de items y luego iterar sobre ella:

```python
mi_diccionario = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Bogotá'}

for item in mi_diccionario.items():
    print(item)
# Imprime:
# ('nombre', 'Juan')
# ('edad', 25)
# ('ciudad', 'Bogotá')
```

## Las palabras `break` y `continue`

Las palabras reservadas `break` y `continue` se utilizan para controlar el flujo de ejecución en bucles. Ambas palabras reservadas son útiles para controlar el flujo de ejecución y tomar decisiones dentro de bucles en función de ciertas condiciones. Es importante usarlas con moderación para mantener un código claro y legible.

### 1. `break`:

La palabra reservada `break` se utiliza para salir abruptamente de un bucle, interrumpiendo su ejecución incluso si la condición del bucle aún es verdadera.

**Ejemplo de `break`:**

```python
for numero in range(10):
    if numero == 5:
        break
    print(numero)
# Imprime:
# 0
# 1
# 2
# 3
# 4
```

En este ejemplo, el bucle `for` se interrumpe cuando `numero` es igual a 5 debido a la declaración `break`, y no se imprimirán números mayores a 4.

```python
contador = 0

while contador < 10:
    print(contador)
    if contador == 5:
        print("¡Condición cumplida! Salimos del bucle.")
        break
    contador += 1
```

En este ejemplo, el bucle `while` se ejecutará mientras `contador` sea menor que 10. Cuando `contador` llega a 5, la declaración `break` se ejecuta, lo que hace que el bucle se interrumpa abruptamente.

### 2. `continue`:

La palabra reservada `continue` se utiliza para saltar a la siguiente iteración del bucle sin ejecutar el resto del código dentro del bucle para esa iteración en particular.

**Ejemplo de `continue`:**

```python
for numero in range(6):
    if numero == 3:
        continue
    print(numero)
# Imprime:
# 0
# 1
# 2
# 4
# 5
```

En este ejemplo, cuando `numero` es igual a 3, la declaración `continue` salta directamente a la siguiente iteración del bucle, evitando la impresión del número 3.

```python
contador = 0

while contador < 5:
    contador += 1
    if contador == 3:
        print("¡Condición cumplida! Saltamos a la siguiente iteración.")
        continue
    print(contador)
```

En este caso, cuando `contador` es igual a 3, la declaración `continue` se ejecuta, omitiendo la impresión del número 3 y saltando directamente a la siguiente iteración del bucle `while`.

### Uso común:

- **`break`:** Se usa para salir de un bucle anticipadamente cuando se cumple una condición específica.
- **`continue`:** Se utiliza para omitir parte del código dentro del bucle y pasar a la siguiente iteración, basándose en una condición.

### Uso de `break` para salir de un bucle basado en la entrada del usuario:

```python
while True:
    respuesta = input("¿Quieres continuar? (s/n): ")
    
    if respuesta.lower() == 'n':
        print("Saliendo del bucle.")
        break
    
    print("Continuando...")
```

En este ejemplo, el bucle `while` se ejecutará indefinidamente hasta que el usuario ingrese 'n' como respuesta. Cuando se ingresa 'n', la declaración `break` se ejecuta, y el bucle se termina.
