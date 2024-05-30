# Capítulo 23: Manejando archivos `.json`, `.yaml` y `.config`

## Manejando archivos `.json`

Trabajar con archivos JSON en Python es una tarea común debido a la popularidad de este formato para almacenar y transmitir datos estructurados. Python ofrece un módulo llamado `json` que permite serializar (convertir estructuras de datos a cadenas JSON) y deserializar (convertir cadenas JSON de nuevo a estructuras de datos) fácilmente. Aquí te explicaré cómo puedes leer y escribir información en archivos JSON utilizando este módulo.

Estas operaciones básicas de lectura y escritura JSON son esenciales para trabajar con datos estructurados en Python, especialmente en aplicaciones web, APIs, y al manipular configuraciones.

### ¿Qué es JSON?

JSON (JavaScript Object Notation) es un formato de texto ligero para intercambio de datos. Es fácil de leer para los humanos y fácil de analizar para las máquinas. Un ejemplo de un objeto JSON podría ser:

```json
{
    "nombre": "Juan",
    "edad": 30,
    "esEstudiante": false,
    "hobbies": ["fútbol", "pintura"],
    "direccion": {
        "calle": "Avenida Central",
        "ciudad": "Ciudad X"
    }
}
```

### Leer un Archivo JSON

Para leer un archivo JSON en Python y convertirlo en una estructura de datos de Python (como un diccionario), puedes usar el método `json.load()`.

**Ejemplo:**

Supongamos que tienes un archivo llamado `usuario.json` con el contenido mostrado arriba.

```python
import json

# Abrir el archivo JSON para lectura
with open('usuario.json', 'r') as file:
    data = json.load(file)

# Acceder a los datos
print(data['nombre'])  # Salida: Juan
print(data['direccion']['ciudad'])  # Salida: Ciudad X
```

En este código:
- `open('usuario.json', 'r')` abre el archivo en modo lectura.
- `json.load(file)` lee el archivo y lo convierte en un diccionario de Python.

### Escribir en un Archivo JSON

Para escribir datos de Python en un archivo JSON, puedes usar el método `json.dump()`, que toma una estructura de datos de Python y la escribe en un archivo como JSON.

**Ejemplo:**

```python
import json

data = {
    "nombre": "Ana",
    "edad": 25,
    "esEstudiante": True,
    "hobbies": ["lectura", "ajedrez"],
    "direccion": {
        "calle": "Calle Falsa 123",
        "ciudad": "Ciudad Y"
    }
}

# Abrir el archivo JSON para escritura
with open('nuevo_usuario.json', 'w') as file:
    json.dump(data, file, indent=4)

# Comprobar el contenido del archivo
with open('nuevo_usuario.json', 'r') as file:
    print(file.read())
```

En este ejemplo:
- `open('nuevo_usuario.json', 'w')` abre el archivo en modo escritura. Si el archivo no existe, se creará.
- `json.dump(data, file, indent=4)` escribe el diccionario `data` en el archivo, convirtiéndolo en una cadena JSON. El argumento `indent=4` hace que el archivo sea más fácil de leer para los humanos, añadiendo 4 espacios de indentación.

### Consejos Adicionales

- **Manipulación de JSON como strings**: Si necesitas trabajar con JSON directamente como un string en lugar de escribirlo o leerlo desde un archivo, puedes usar `json.dumps()` para serializar y `json.loads()` para deserializar.
- **Manejo de excepciones**: Es una buena práctica añadir manejo de excepciones al trabajar con archivos para gestionar errores como archivos no encontrados o problemas de permisos.


## Manejo de archivos `.config`

Los archivos `.config` son una forma práctica de almacenar configuraciones en un formato legible y fácilmente editable. En Python, estos archivos generalmente siguen la sintaxis INI, que permite definir secciones, cada una con claves y valores. Para trabajar con estos archivos, Python ofrece la biblioteca `configparser`, que facilita la lectura y escritura de configuraciones.

Utilizar `configparser` para manejar archivos `.config` en Python es una forma eficiente de gestionar configuraciones en aplicaciones, permitiendo un fácil acceso y modificación de la información de configuración sin necesidad de cambiar el código fuente.

### ¿Qué es un archivo .config?

Un archivo `.config` o `.ini` estructura la información en secciones, cada una con pares de clave-valor. Aquí tienes un ejemplo de cómo puede lucir un archivo `.config`:

```ini
[DEFAULT]
Server = 192.168.1.1
Port = 8080

[database]
user = admin
password = secret
host = localhost

[files]
log_path = /var/log/app.log
```

### Leer un Archivo .config

Para leer este tipo de archivos, utilizamos la biblioteca `configparser` de Python. Aquí te muestro cómo puedes hacerlo:

**Ejemplo:**

```python
import configparser

# Crear un objeto ConfigParser
config = configparser.ConfigParser()

# Leer el archivo .config
config.read('configuracion.config')

# Acceder a los valores de las configuraciones
server = config['DEFAULT']['Server']
port = config.getint('DEFAULT', 'Port')
user = config['database']['user']

print("Server:", server)
print("Port:", port)
print("Database user:", user)
```

En este código:
- `configparser.ConfigParser()` crea un objeto `ConfigParser` que permite leer y escribir archivos `.config`.
- `config.read('configuracion.config')` carga las configuraciones desde el archivo especificado.
- Puedes acceder a los valores usando `config['sección']['clave']` o `config.getint('sección', 'clave')` para obtener un valor como un entero.

### Escribir en un Archivo .config

Escribir en un archivo `.config` también se realiza con `configparser`. Puedes modificar el objeto `ConfigParser` y luego escribir sus contenidos de vuelta a un archivo.

**Ejemplo:**

```python
import configparser

# Crear un objeto ConfigParser
config = configparser.ConfigParser()

# Agregar una sección y algunas configuraciones
config.add_section('server')
config.set('server', 'host', '192.168.1.1')
config.set('server', 'port', '8080')

# Crear otra sección con más configuraciones
config['database'] = {'user': 'root', 'password': 'supersecret', 'host': 'localhost'}

# Escribir las configuraciones en un archivo
with open('nueva_configuracion.config', 'w') as configfile:
    config.write(configfile)

# Comprobar el contenido del archivo
with open('nueva_configuracion.config', 'r') as configfile:
    print(configfile.read())
```

En este ejemplo:
- `add_section('nombre')` crea una nueva sección.
- `set('sección', 'clave', 'valor')` establece una clave con su correspondiente valor en la sección especificada.
- `config['sección'] = {...}` es otra forma de añadir secciones y valores.
- `config.write(configfile)` escribe el objeto `ConfigParser` al archivo, guardando todas las configuraciones.

### Consejos Adicionales

- **Manejo de excepciones**: Añade manejo de excepciones para capturar errores como archivos no encontrados o problemas al escribir en un archivo.
- **Usar `with` para archivos**: Esto garantiza que el archivo se cierra correctamente después de su uso, incluso si ocurre una excepción.

## Manejo de archivos `.yaml`

Los archivos YAML (YAML Ain't Markup Language) son muy utilizados para configuraciones debido a su fácil legibilidad y capacidad para representar estructuras de datos complejas, como listas y diccionarios. En Python, para trabajar con archivos YAML, se utiliza comúnmente la biblioteca `PyYAML`. A continuación, te explico cómo leer y escribir archivos YAML en Python, junto con algunos ejemplos detallados.

Utilizar PyYAML para manejar archivos YAML te permite trabajar con configuraciones de una manera más estructurada y clara, facilitando la gestión y mantenimiento del código en proyectos de software.

### ¿Qué es un archivo YAML?

Un archivo YAML utiliza un formato basado en texto para representar datos de forma jerárquica, lo cual es ideal para archivos de configuración. Aquí tienes un ejemplo de cómo puede lucir un archivo YAML:

```yaml
usuario:
  nombre: Juan
  edad: 30
  esEstudiante: false
  hobbies:
    - fútbol
    - pintura
  direccion:
    calle: Avenida Central
    ciudad: Ciudad X
```

### Instalación de PyYAML

Antes de poder leer o escribir archivos YAML, necesitarás instalar la biblioteca `PyYAML` si aún no lo has hecho. Puedes instalarla usando pip:

```bash
pip install PyYAML
```

### Leer un Archivo YAML

Para leer un archivo YAML, utilizas la función `load()` o `safe_load()` de PyYAML. La función `safe_load()` es recomendada porque evita la ejecución de código arbitrario que podría estar presente en el YAML.

**Ejemplo de Lectura:**

```python
import yaml

# Abrir el archivo YAML para lectura
with open('configuracion.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Acceder a los datos
print(data['usuario']['nombre'])  # Salida: Juan
print(data['usuario']['direccion']['ciudad'])  # Salida: Ciudad X
```

En este código:
- `open('configuracion.yaml', 'r')` abre el archivo en modo lectura.
- `yaml.safe_load(file)` lee el archivo y convierte el contenido en un diccionario de Python.

### Escribir en un Archivo YAML

Para escribir en un archivo YAML, puedes usar la función `dump()` de PyYAML, que toma una estructura de datos de Python y la escribe en un archivo en formato YAML.

**Ejemplo de Escritura:**

```python
import yaml

data = {
  'usuario': {
    'nombre': 'Ana',
    'edad': 25,
    'esEstudiante': True,
    'hobbies': ['lectura', 'ajedrez'],
    'direccion': {
      'calle': 'Calle Falsa',
      'ciudad': 'Ciudad Y'
    }
  }
}

# Abrir el archivo YAML para escritura
with open('nuevo_configuracion.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)

# Comprobar el contenido del archivo
with open('nuevo_configuracion.yaml', 'r') as file:
    print(file.read())
```

En este ejemplo:
- `yaml.dump(data, file, default_flow_style=False)` escribe la estructura de datos `data` al archivo, formateándola en el estilo de bloques de YAML, que es más legible que el estilo en línea (flow style).

### Consejos Adicionales

- **Seguridad**: Aunque `safe_load()` es más seguro que `load()`, siempre debes estar seguro del origen de los archivos YAML que procesas para evitar vulnerabilidades.
- **Manejo de excepciones**: Es buena práctica añadir manejo de excepciones al trabajar con archivos para gestionar errores como problemas de lectura/escritura o archivos no encontrados.


____

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

Mayo 2024
