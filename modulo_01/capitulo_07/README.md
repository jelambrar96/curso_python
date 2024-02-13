# Capítulo 7. Iterables: Listas, tuplas y range

En Python, las estructuras iterables son objetos que se pueden recorrer o iterar. Esto significa que puedes acceder a sus elementos uno por uno en un orden específico. Aquí tienes algunas de las estructuras iterables más comunes en Python:

1. **Listas:**
   - Ejemplo:

     ```python
     lista = [1, 2, 3, 4, 5]
     ```

2. **Tuplas:**
   - Ejemplo:

     ```python
     tupla = (10, 20, 30, 40, 50)
     ```

3. **Cadenas de texto (Strings):**
   - Ejemplo:

     ```python
     cadena = "Python"
     ```

4. **Conjuntos (Sets):**
   - Ejemplo:

     ```python
     conjunto = {1, 2, 3, 4, 5}
     ```

5. **Diccionarios:**
   - Ejemplo:

     ```python
     diccionario = {'a': 1, 'b': 2, 'c': 3}
     ```

6. **Rangos (Ranges):**
   - Ejemplo:

     ```python
     rango = range(0,10,2)
     ```

7. **Archivos:**
   - Ejemplo:

     ```python
     with open('archivo.txt', 'r') as archivo:
        pass
     ```

Estas estructuras permiten la iteración a través de sus elementos, ya sea utilizando un bucle `for` o mediante otras técnicas de iteración. Además, Python proporciona funciones y métodos integrados que trabajan con estructuras iterables, como `enumerate`, `zip`, y `map`, que pueden ser útiles para realizar operaciones más avanzadas durante la iteración.


# Listas

¡Por supuesto! En Python, una lista es una estructura de datos que te permite almacenar y organizar elementos de manera secuencial. Aquí tienes información sobre las listas, sus características principales, algunos métodos y funciones esenciales, así como ejemplos:

**Características principales de las listas en Python:**
1. **Secuencialidad:** Los elementos en una lista están organizados en un orden específico y se accede a ellos mediante índices.
2. **Mutabilidad:** Las listas son mutables, lo que significa que puedes modificar, añadir o eliminar elementos después de haber creado la lista.
3. **Heterogeneidad:** Una lista puede contener elementos de diferentes tipos de datos, como números, cadenas, booleanos, otras listas, etc.

**Operaciones comunes con listas:**
1. **Concatenación (`+`):** Combina dos listas en una sola.
2. **Repetición (`*`):** Repite los elementos de una lista.
3. **Indexación (`[]`):** Accede a elementos individuales mediante índices.
4. **Slicing (`[:]`):** Obtiene una porción de la lista.
5. **Pertenencia (`in`):** Verifica si un elemento está presente en la lista.

**Recordando el operador slice [:]**
En Python, el operador de slice `[:]` también se utiliza con listas para obtener una porción específica de la lista. El formato general es `lista[inicio:fin]`, donde `inicio` es inclusivo y `fin` es exclusivo. Aquí tienes ejemplos para ilustrar su uso:

**Ejemplos de operador de slice en listas:**

```python
# Definir una lista
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtener una porción desde el inicio hasta el índice 6 (sin incluir)
porcion1 = mi_lista[:6]
print(porcion1)  # Imprime [1, 2, 3, 4, 5, 6]

# Obtener una porción desde el índice 7 hasta el final
porcion2 = mi_lista[7:]
print(porcion2)  # Imprime [8, 9, 10]

# Obtener una porción desde el índice 2 hasta el índice 8 (sin incluir)
porcion3 = mi_lista[2:8]
print(porcion3)  # Imprime [3, 4, 5, 6, 7, 8]

# Utilizar índices negativos para contar desde el final
porcion4 = mi_lista[-5:-1]
print(porcion4)  # Imprime [6, 7, 8, 9]

# Obtener toda la lista (equivalente a lista[:])
copia_completa = mi_lista[:]
print(copia_completa)  # Imprime [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtener una porción con un paso (cada segundo elemento)
porcion_con_paso = mi_lista[::2]
print(porcion_con_paso)  # Imprime [1, 3, 5, 7, 9]
```

Al igual que con las cadenas, el operador de slice en listas no modifica la lista original, sino que crea una nueva lista con la porción deseada. Este operador es muy útil para manipular y trabajar con subconjuntos de datos en listas de manera eficiente.


**Métodos y funciones principales para trabajar con listas:**

1. **Creación de una lista:**
   - Ejemplo:

     ```python
     lista_numeros = [1, 2, 3, 4, 5]
     lista_strings = ['apple', 'banana', 'cherry']
     lista_mixta = [1, 'dos', True, 4.5]
     ```

2. **Acceso a elementos:**
   - Ejemplo:

     ```python
     primer_elemento = lista_numeros[0]
     segundo_elemento = lista_strings[1]
     ```

3. **Longitud de la lista:**
   - Método: `len()`
   - Ejemplo:

     ```python
     longitud = len(lista_mixta)
     ```

4. **Añadir elementos al final de la lista:**
   - Método: `append()`
   - Ejemplo:

     ```python
     lista_numeros.append(6)
     ```

5. **Insertar elementos en una posición específica:**
   - Método: `insert()`
   - Ejemplo:

     ```python
     lista_strings.insert(1, 'orange')
     ```

6. **Eliminar el último elemento de la lista o uno específico:**
   - Métodos: `pop()` o `remove()`
   - Ejemplos:

     ```python
     ultimo_elemento = lista_numeros.pop()
     lista_strings.remove('banana')
     ```

7. **Ordenar la lista:**
   - Métodos: `sort()`
   - Ejemplo:

     ```python
     lista_numeros.sort()
     ```

8. **Revertir la lista:**
   - Método: `reverse()`
   - Ejemplo:

     ```python
     lista_mixta.reverse()
     ```

**Ejemplos de uso de listas:**

```python
# Creación de una lista
frutas = ['manzana', 'naranja', 'plátano', 'uva']

# Acceso a elementos
print(frutas[0])  # Imprime 'manzana'

# Añadir un elemento al final de la lista
frutas.append('kiwi')

# Insertar un elemento en una posición específica
frutas.insert(2, 'pera')

# Eliminar un elemento específico
frutas.remove('naranja')

# Imprimir la lista actualizada
print(frutas)  # Imprime ['manzana', 'plátano', 'pera', 'uva', 'kiwi']
```

Las listas son una herramienta versátil y poderosa en Python, utilizadas para manejar colecciones de datos de manera eficiente y flexible. Con estos métodos y funciones, los desarrolladores pueden manipular y trabajar con listas de manera efectiva en sus programas.

## El método `sort()` y la función `sorted()`

 En Python, tanto el método `sort()` como la función `sorted()` se utilizan para ordenar elementos en una lista. Sin embargo, hay diferencias clave en su comportamiento y cómo se aplican. Aquí tienes una explicación detallada de cada uno:

### Método `sort()`:

- **In-place:** El método `sort()` ordena la lista "in-place", lo que significa que modifica la lista original directamente.
- **Modificación de la lista original:** La lista original se modifica, y no se crea una nueva lista.
- **No devuelve un nuevo objeto:** No devuelve nada (`None`).
- **Uso específico para listas:** Solo puede aplicarse a listas y no a otros tipos de secuencias.

**Ejemplo:**

```python
mi_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
mi_lista.sort()
print(mi_lista)
# Imprime: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

### Función `sorted()`:

- **Crea una nueva lista ordenada:** La función `sorted()` devuelve una nueva lista ordenada y no modifica la lista original.
- **Puede trabajar con cualquier iterable:** No está limitada a listas y puede ordenar cualquier iterable, incluyendo tuplas, cadenas y más.
- **Devuelve un nuevo objeto:** La función `sorted()` devuelve una nueva lista ordenada.

**Ejemplo:**

```python
mi_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
nueva_lista_ordenada = sorted(mi_lista)
print(nueva_lista_ordenada)
# Imprime: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# La lista original no ha sido modificada
print(mi_lista)
# Imprime: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
```

### Resumen:

- Usa `sort()` si deseas ordenar una lista existente y no necesitas conservar la lista original.
- Usa `sorted()` si necesitas una nueva lista ordenada y quieres mantener la original sin cambios, o si estás trabajando con otros tipos de iterables.

En resumen, la principal diferencia radica en el hecho de que `sort()` modifica la lista original, mientras que `sorted()` crea una nueva lista ordenada sin modificar la original.


# tuplas

¡Claro! En Python, una tupla es una estructura de datos similar a una lista, pero con la diferencia principal de que las tuplas son inmutables. Esto significa que una vez que creas una tupla, no puedes modificar su contenido, agregar o eliminar elementos. Aquí tienes información sobre las tuplas, sus características principales, algunos métodos y funciones esenciales, así como ejemplos:

**Características principales de las tuplas en Python:**
1. **Inmutabilidad:** Una vez creada, no se pueden modificar, agregar ni eliminar elementos.
2. **Heterogeneidad:** Pueden contener elementos de diferentes tipos de datos.
3. **Indexación:** Se accede a los elementos mediante índices, igual que en las listas.

**Operaciones comunes con tuplas:**
1. **Indexación (`[]`):** Acceder a elementos individuales mediante índices.
2. **Slicing (`[:]`):** Obtener una porción de la tupla.
3. **Concatenación (`+`):** Combina dos tuplas en una sola.
4. **Repetición (`*`):** Repite los elementos de una tupla.
5. **Pertenencia (`in`):** Verifica si un elemento está presente en la tupla.

**Métodos y funciones principales para trabajar con tuplas:**

1. **Creación de una tupla:**
   - Ejemplo:

     ```python
     tupla_numeros = (1, 2, 3, 4, 5)
     tupla_strings = ('manzana', 'naranja', 'plátano')
     tupla_mixta = (1, 'dos', True)
     ```

2. **Acceso a elementos:**
   - Ejemplo:

     ```python
     primer_elemento = tupla_numeros[0]
     segundo_elemento = tupla_strings[1]
     ```

3. **Longitud de la tupla:**
   - Función: `len()`
   - Ejemplo:

     ```python
     longitud = len(tupla_mixta)
     ```

4. **Desempaquetado de tuplas:**
   - Ejemplo:

     ```python
     tupla = (10, 20, 30)
     a, b, c = tupla
     ```

5. **Concatenación de tuplas:**
   - Ejemplo:

     ```python
     tupla1 = (1, 2, 3)
     tupla2 = ('a', 'b', 'c')
     tupla_concatenada = tupla1 + tupla2
     ```

6. **Repetición de elementos:**
   - Ejemplo:

     ```python
     tupla_repetida = (1, 2) * 3
     ```

**Ejemplos de uso de tuplas:**

```python
# Creación de una tupla
coordenadas = (3, 7)

# Acceso a elementos
x = coordenadas[0]  # x es igual a 3

# Longitud de la tupla
longitud = len(coordenadas)  # longitud es igual a 2

# Desempaquetado de tuplas
a, b = coordenadas  # a es igual a 3, b es igual a 7

# Concatenación de tuplas
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla_concatenada = tupla1 + tupla2  # tupla_concatenada es igual a (1, 2, 3, 'a', 'b', 'c')
```

Las tuplas son útiles cuando se desea garantizar la integridad de los datos y prevenir modificaciones accidentales. Se utilizan comúnmente en situaciones donde la inmutabilidad es deseada, como para representar coordenadas, configuraciones iniciales o cualquier conjunto de datos que no debería cambiar durante la ejecución del programa.

# range

En Python, `range` es un tipo de datos que representa una secuencia de números inmutables. Aunque a menudo se utiliza en bucles, no es una lista, sino un objeto que produce valores según sea necesario. Aquí tienes información sobre los `range`, sus características principales, algunos métodos y funciones esenciales, así como ejemplos:

**Características principales de los `range` en Python:**
1. **Inmutabilidad:** Al igual que las tuplas, los `range` son inmutables, lo que significa que no puedes modificar sus valores después de haber sido creados.
2. **Eficiencia en el uso de memoria:** Los `range` no almacenan todos los valores en memoria, sino que generan los valores necesarios cuando se requieren.
3. **Sintaxis:** La sintaxis básica de `range` es `range(inicio, fin, paso)`, donde `inicio` es inclusive y `fin` es exclusivo.

**Operaciones comunes con objetos `range`:**
1. **Iteración:** Se utilizan comúnmente en bucles `for` para generar secuencias de números.
2. **Conversión a lista:** Puedes convertir un objeto `range` en una lista utilizando la función `list()`.

**Métodos y funciones principales para trabajar con `range`:**

1. **Creación de un objeto `range`:**
   - Ejemplo:

     ```python
     rango = range(0, 10, 2)
     ```

2. **Convertir `range` en lista:**
   - Función: `list()`
   - Ejemplo:

     ```python
     lista_rango = list(range(0, 10, 2))
     ```

3. **Iterar sobre un `range`:**
   - Ejemplo:

     ```python
     for i in range(5):
         print(i)
     ```

4. **Verificar si un valor está en un `range`:**
   - Ejemplo:

     ```python
     esta_en_rango = 3 in range(0, 5)  # devuelve True
     ```

**Ejemplos de uso de `range`:**

```python
# Creación de un objeto range
mi_rango = range(0, 10, 2)

# Iteración sobre el rango
for numero in mi_rango:
    print(numero)  # Imprime 0, 2, 4, 6, 8

# Convertir el rango en una lista
lista_mi_rango = list(mi_rango)  # lista_mi_rango es igual a [0, 2, 4, 6, 8]

# Verificar si un valor está en el rango
esta_en_rango = 3 in mi_rango  # devuelve False
```

Los objetos `range` son eficientes en términos de memoria y se utilizan comúnmente en bucles `for` para generar secuencias de números. Pueden ser útiles cuando necesitas iterar sobre un rango específico de valores sin necesidad de crear una lista completa en memoria.

## Conjuntos: sets  

En Python, un conjunto `set` es una colección no ordenada y mutable de elementos únicos. Aquí tienes información sobre los conjuntos, sus características principales, operaciones, métodos y funciones esenciales, así como ejemplos:

**Características principales de los conjuntos en Python:**
1. **Unicidad:** Los conjuntos no contienen elementos duplicados; cada elemento es único en el conjunto.
2. **Mutabilidad:** Los conjuntos son mutables, lo que significa que puedes agregar y eliminar elementos después de su creación.
3. **No ordenados:** Los elementos en un conjunto no tienen un orden específico.

**Operaciones comunes con conjuntos:**
1. **Unión (`|`):** Combina elementos de dos conjuntos.
2. **Intersección (`&`):** Obtiene los elementos comunes a dos conjuntos.
3. **Diferencia (`-`):** Obtiene los elementos presentes en un conjunto pero no en otro.
4. **Diferencia simétrica (`^`):** Obtiene los elementos que están en uno de los conjuntos, pero no en ambos.

**Métodos y funciones principales para trabajar con conjuntos:**

1. **Creación de un conjunto:**
   - Ejemplo:

     ```python
     conjunto_a = {1, 2, 3, 4, 5}
     conjunto_b = set([4, 5, 6, 7, 8])
     ```

2. **Agregar elementos:**
   - Método: `add()`
   - Ejemplo:

     ```python
     conjunto_a.add(6)
     ```

3. **Eliminar un elemento:**
   - Métodos: `remove()`, `discard()`
   - Ejemplo:

     ```python
     conjunto_a.remove(3)
     ```

4. **Comprobar la pertenencia:**
   - Operador: `in`
   - Ejemplo:

     ```python
     pertenece = 4 in conjunto_a  # devuelve True
     ```

5. **Unión de conjuntos:**
   - Método: `union()`
   - Ejemplo:

     ```python
     union_conjuntos = conjunto_a.union(conjunto_b)
     ```

6. **Intersección de conjuntos:**
   - Método: `intersection()`
   - Ejemplo:

     ```python
     interseccion_conjuntos = conjunto_a.intersection(conjunto_b)
     ```

7. **Diferencia de conjuntos:**
   - Método: `difference()`
   - Ejemplo:

     ```python
     diferencia_conjuntos = conjunto_a.difference(conjunto_b)
     ```

8. **Diferencia simétrica de conjuntos:**
   - Método: `symmetric_difference()`
   - Ejemplo:

     ```python
     diferencia_simetrica = conjunto_a.symmetric_difference(conjunto_b)
     ```

**Ejemplos de uso de conjuntos:**

```python
# Creación de conjuntos
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = set([4, 5, 6, 7, 8])

# Agregar un elemento
conjunto_a.add(6)

# Eliminar un elemento
conjunto_a.remove(3)

# Unión de conjuntos
union_conjuntos = conjunto_a.union(conjunto_b)

# Intersección de conjuntos
interseccion_conjuntos = conjunto_a.intersection(conjunto_b)

# Diferencia de conjuntos
diferencia_conjuntos = conjunto_a.difference(conjunto_b)

# Diferencia simétrica de conjuntos
diferencia_simetrica = conjunto_a.symmetric_difference(conjunto_b)
```

Los conjuntos son útiles para operaciones que involucran membresía, comparaciones y operaciones de conjuntos en matemáticas y ciencias de la computación. Su capacidad para contener elementos únicos y realizar operaciones eficientes los hace valiosos en diversas situaciones.

____

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

Enero 2024