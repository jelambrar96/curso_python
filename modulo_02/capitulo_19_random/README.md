# Capítulo 19: Manejando números pseudoaletórios: El paquete `random`

El paquete `random` en Python es una biblioteca extremadamente útil y versátil que permite generar números aleatorios. Este paquete es parte de la biblioteca estándar de Python, por lo que no necesitas instalar nada adicional para usarlo. Se utiliza en una variedad de campos, incluyendo simulaciones, juegos, pruebas de algoritmos, y más. Aquí vamos a explorar cómo funciona y algunos de sus métodos más importantes.

### Importar el paquete python

```python
import random
```

### Funcionalidad Básica

El paquete `random` puede generar números aleatorios de varias maneras, ya sea números enteros o flotantes, selección aleatoria de elementos de una secuencia, entre otros.

### Principales Métodos y Ejemplos

1. **`random()`**: Retorna un número flotante aleatorio entre 0.0 y 1.0.

   ```python
   print(random.random())  # Ejemplo: 0.37444887175646646
   ```

2. **`randint(a, b)`**: Retorna un número entero aleatorio N tal que a <= N <= b.

   ```python
   print(random.randint(1, 10))  # Ejemplo: 3
   ```

3. **`uniform(a, b)`**: Retorna un número flotante aleatorio tal que a <= N <= b.

   ```python
   print(random.uniform(1, 10))  # Ejemplo: 9.180014607311752
   ```

4. **`choice(seq)`**: Retorna un elemento aleatorio de una secuencia no vacía.

   ```python
   print(random.choice(['manzana', 'banana', 'cereza']))  # Ejemplo: 'banana'
   ```

5. **`choices(seq, k)`**: Retorna k elementos aleatorio de una secuencia no vacía.

   ```python
   print(random.choice(['manzana', 'banana', 'cereza'], k=2))  # Ejemplo: ['banana', 'cereza']
   ```

6. **`shuffle(seq)`**: Mezcla los elementos de una lista en lugar.

   ```python
   lista = [1, 2, 3, 4, 5]
   random.shuffle(lista)
   print(lista)  # Ejemplo: [2, 5, 3, 1, 4]
   ```

7. **`sample(population, k)`**: Retorna una lista de k elementos únicos elegidos de la población proporcionada.

   ```python
   print(random.sample(range(100), 10))  # Ejemplo: [30, 83, 7, 20, 35, 95, 8, 58, 13, 77]
   ```

#### Weights: Seleccionando con pesos

El método `random.choices()` de Python te permite seleccionar elementos de manera aleatoria de una lista, con la posibilidad de especificar una distribución de probabilidades para la selección de cada elemento mediante el argumento `weights`. Aquí tienes un ejemplo sencillo:

```python
import random

# Lista de elementos a seleccionar
elementos = ['manzana', 'banana', 'cereza', 'durazno']

# Ponderaciones para cada elemento
pesos = [10, 1, 1, 5]

# Seleccionar un elemento de la lista usando las ponderaciones dadas
elemento_seleccionado = random.choices(elementos, weights=pesos, k=1)[0]

print("Elemento seleccionado:", elemento_seleccionado)
```

En este ejemplo:
- La lista `elementos` contiene cuatro frutas diferentes.
- La lista `pesos` asigna una mayor probabilidad a la 'manzana' (con un peso de 10) comparado con 'banana' y 'cereza' (con un peso de 1 cada una), y un peso moderado al 'durazno' (con un peso de 5).
- `random.choices()` se utiliza para seleccionar un elemento según las ponderaciones especificadas, donde `k=1` indica que se seleccionará solo un elemento.


### Otras métodos del paquete `random` 

| Método            | Descripción                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------------------|
| `seed()`          | Inicializa el generador de números aleatorios.                                                                       |
| `getstate()`      | Devuelve el estado interno actual del generador de números aleatorios.                                               |
| `setstate()`      | Restaura el estado interno del generador de números aleatorios.                                                      |
| `getrandbits()`   | Devuelve un número representando los bits aleatorios.                                                                |
| `randrange()`     | Devuelve un número aleatorio dentro de un rango especificado.                                                        |
| `randint()`       | Devuelve un número entero aleatorio entre el rango dado, inclusivo.                                                  |
| `choice()`        | Devuelve un elemento aleatorio de una secuencia dada.                                                                |
| `choices()`       | Devuelve una lista con una selección aleatoria de una secuencia dada.                                                |
| `shuffle()`       | Mezcla una secuencia en el lugar y devuelve nada.                                                                    |
| `sample()`        | Devuelve una muestra de elementos seleccionados aleatoriamente de una secuencia.                                     |
| `random()`        | Devuelve un número flotante aleatorio entre 0 y 1.                                                                   |
| `uniform()`       | Devuelve un número flotante aleatorio dentro de un rango especificado entre dos parámetros dados.                    |
| `triangular()`    | Devuelve un número flotante aleatorio entre dos parámetros dados, pudiendo especificar un modo que es el punto medio.|
| `betavariate()`   | Devuelve un número flotante aleatorio entre 0 y 1 basado en la distribución Beta.                                    |
| `expovariate()`   | Devuelve un número flotante aleatorio basado en la distribución Exponencial.                                         |
| `gammavariate()`  | Devuelve un número flotante aleatorio basado en la distribución Gamma.                                               |
| `gauss()`         | Devuelve un número flotante aleatorio basado en la distribución Gaussiana.                                           |
| `lognormvariate()`| Devuelve un número flotante aleatorio basado en una distribución log-normal.                                         |
| `normalvariate()` | Devuelve un número flotante aleatorio basado en la distribución normal.                                              |
| `vonmisesvariate()`| Devuelve un número flotante aleatorio basado en la distribución de von Mises (utilizada en estadísticas direccionales).|
| `paretovariate()` | Devuelve un número flotante aleatorio basado en la distribución de Pareto.                                           |
| `weibullvariate()`| Devuelve un número flotante aleatorio basado en la distribución de Weibull.                                          |

### Extra: Cómo generar secuencia de caracteres aleatorios en python

Para generar secuencias de caracteres aleatorios en Python, puedes utilizar el módulo `random` de la biblioteca estándar, que ofrece varias funciones útiles para generar números aleatorios y realizar selecciones aleatorias. Aquí te dejo un ejemplo de cómo generar una secuencia de caracteres aleatorios:

```python
import random
import string

def generar_secuencia_aleatoria(longitud):
    # Define los caracteres que quieres incluir (letras mayúsculas, minúsculas y números)
    caracteres = string.ascii_letters + string.digits
    # Utiliza random.choice para seleccionar caracteres al azar de la cadena de caracteres
    secuencia = ''.join(random.choice(caracteres) for _ in range(longitud))
    return secuencia

# Ejemplo de uso: generar una secuencia de 10 caracteres aleatorios
secuencia_aleatoria = generar_secuencia_aleatoria(10)
print(secuencia_aleatoria)
```

En este código:
- `string.ascii_letters` incluye todas las letras del alfabeto (mayúsculas y minúsculas).
- `string.digits` incluye todos los números del 0 al 9.
- La función `random.choice` selecciona un carácter al azar de la cadena de caracteres especificada.
- El código `join` junto con una comprensión de lista crea una secuencia de caracteres aleatorios de la longitud deseada.


### Recomendaciones al Usar el Paquete `random`

- **No para Criptografía**: Los métodos del paquete `random` no son seguros para usos en criptografía debido a que los números generados son predecibles con suficiente información. Para criptografía, se debe utilizar el módulo `secrets` que proporciona generación de números aleatorios más seguros.
- **Reproducibilidad**: Para fines de depuración o pruebas donde se necesitan resultados reproducibles, se puede fijar la semilla del generador de números aleatorios utilizando `random.seed(a=None)`. Esto hace que la secuencia de números aleatorios sea predecible.
- **Uso con cuidado en simulaciones**: Asegúrate de entender bien la distribución de los números aleatorios que necesitas para tu simulación para evitar sesgos o resultados incorrectos.

____

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

Enero 2024
