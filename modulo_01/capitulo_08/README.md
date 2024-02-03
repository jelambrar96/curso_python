# Capítulo 8. Diccionarios y sus principales métodos. 

En Python, un diccionario es una estructura de datos que permite almacenar y organizar información en pares clave-valor. Aquí tienes información detallada sobre los diccionarios, sus características principales, operaciones, métodos y ejemplos de implementación:

**Características principales de los diccionarios en Python:**
1. **Pares clave-valor:** Cada elemento en un diccionario consiste en un par clave-valor, donde la clave es única y asociada a un valor.
2. **Mutabilidad:** Los diccionarios son mutables, lo que significa que puedes modificar, agregar o eliminar elementos después de su creación.
3. **Heterogeneidad:** Pueden contener valores de diferentes tipos de datos, tanto para las claves como para los valores.
4. **No ordenados:** Los elementos en un diccionario no tienen un orden específico.

**Operaciones comunes con diccionarios:**
1. **Acceso a elementos:** Puedes acceder a un valor utilizando su clave.
2. **Modificación de valores:** Puedes modificar el valor asociado a una clave específica.
3. **Adición de elementos:** Puedes agregar nuevos pares clave-valor al diccionario.
4. **Eliminación de elementos:** Puedes eliminar elementos específicos utilizando sus claves.
5. **Verificación de pertenencia:** Puedes verificar si una clave está presente en el diccionario.

**Métodos y funciones principales para trabajar con diccionarios:**

1. **Creación de un diccionario:**
   - Ejemplo:

     ```python
     mi_diccionario = {'clave1': 'valor1', 'clave2': 'valor2', 'clave3': 'valor3'}
     ```

2. **Acceso a valores:**
   - Ejemplo:

     ```python
     valor = mi_diccionario['clave1']
     ```

3. **Modificación de valores:**
   - Ejemplo:

     ```python
     mi_diccionario['clave1'] = 'nuevo_valor'
     ```

4. **Adición de elementos:**
   - Método: `update()`
   - Ejemplo:

     ```python
     mi_diccionario.update({'clave4': 'valor4', 'clave5': 'valor5'})
     ```

5. **Eliminación de elementos:**
   - Métodos: `pop()`, `del`
   - Ejemplos:

     ```python
     valor_eliminado = mi_diccionario.pop('clave2')
     del mi_diccionario['clave3']
     ```

6. **Obtención de claves, valores y pares clave-valor:**
   - Métodos: `keys()`, `values()`, `items()`
   - Ejemplos:

     ```python
     claves = mi_diccionario.keys()
     valores = mi_diccionario.values()
     pares = mi_diccionario.items()
     ```

**Ejemplo de uso de diccionario:**

```python
# Creación de un diccionario
persona = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Bogotá'}

# Acceso a valores
nombre = persona['nombre']  # nombre es igual a 'Juan'

# Modificación de valores
persona['edad'] = 26

# Adición de elementos
persona['ocupacion'] = 'Ingeniero'

# Eliminación de elementos
ciudad = persona.pop('ciudad')

# Obtención de claves, valores y pares clave-valor
claves = persona.keys()  # claves es igual a ['nombre', 'edad', 'ocupacion']
valores = persona.values()  # valores es igual a ['Juan', 26, 'Ingeniero']
pares = persona.items()  # pares es igual a [('nombre', 'Juan'), ('edad', 26), ('ocupacion', 'Ingeniero')]
```

Los diccionarios son herramientas poderosas y versátiles en Python, utilizadas para representar información estructurada y asociar claves con valores. Pueden ser implementados en una amplia variedad de situaciones para organizar y manipular datos de manera eficiente.