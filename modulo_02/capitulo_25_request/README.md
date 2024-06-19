# Capítulo 25: Los paquetes `urllib` y `requests`

## El paquete `urllib`

¡Hola a todos! Hoy vamos a aprender sobre el paquete `urllib` en Python es una biblioteca estándar para trabajar con URLs. Veremos para qué se utiliza, algunos ejemplos prácticos y cómo se pueden manejar diferentes aspectos de las solicitudes y respuestas HTTP.

El paquete `urllib` es una herramienta muy útil y poderosa para trabajar con URLs y realizar solicitudes HTTP en Python. Aunque es un poco más complejo y menos intuitivo que `requests`, sigue siendo muy versátil y está incluido en la biblioteca estándar de Python, lo que significa que no necesitas instalar paquetes adicionales para usarlo.

### ¿Qué es el paquete `urllib`?

El paquete `urllib` es una biblioteca estándar de Python que se utiliza para trabajar con URLs (Uniform Resource Locators). Permite realizar solicitudes HTTP, manejar URLs, y trabajar con datos provenientes de la web. Está dividido en varios submódulos, cada uno con su funcionalidad específica:

- `urllib.request`: Para abrir y leer URLs.
- `urllib.parse`: Para analizar URLs.
- `urllib.error`: Para manejar errores resultantes de solicitudes.
- `urllib.robotparser`: Para analizar archivos `robots.txt`.

### Ejemplos de uso de `urllib`

#### Hacer una solicitud GET

Vamos a empezar con un ejemplo básico de cómo hacer una solicitud GET usando `urllib.request`:

```python
import urllib.request

url = 'http://www.example.com'
response = urllib.request.urlopen(url)
html = response.read()

print(response.status)  # Debe imprimir 200 si la solicitud fue exitosa
print(html)  # Imprime el contenido HTML de la página
```

#### Manejo de errores

Es importante manejar los errores cuando se trabaja con solicitudes web. `urllib.error` proporciona clases para manejar estos errores:

```python
import urllib.request
import urllib.error

url = 'http://www.example.com/nonexistentpage'
try:
    response = urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print(f'Error HTTP: {e.code}')
except urllib.error.URLError as e:
    print(f'Error URL: {e.reason}')
else:
    html = response.read()
    print(html)
```

#### Enviar datos en una solicitud POST

Para enviar datos en una solicitud POST, puedes usar `urllib.request` con el método `urlopen`:

```python
import urllib.request
import urllib.parse

url = 'http://www.example.com/login'
data = {
    'username': 'example_user',
    'password': 'example_password'
}
data = urllib.parse.urlencode(data).encode('utf-8')  # Codificar los datos

request = urllib.request.Request(url, data=data)
response = urllib.request.urlopen(request)

print(response.status)  # Debe imprimir 200 si la solicitud fue exitosa
print(response.read())  # Imprime la respuesta del servidor
```

#### Análisis de URLs

El submódulo `urllib.parse` permite analizar y construir URLs. Aquí hay un ejemplo de cómo separar una URL en sus componentes:

```python
from urllib.parse import urlparse

url = 'http://www.example.com/some/page?name=ferret&color=purple'
parsed_url = urlparse(url)

print(parsed_url.scheme)   # http
print(parsed_url.netloc)   # www.example.com
print(parsed_url.path)     # /some/page
print(parsed_url.query)    # name=ferret&color=purple
```

También puedes construir una URL a partir de sus componentes:

```python
from urllib.parse import urlunparse

components = ('http', 'www.example.com', '/some/page', '', 'name=ferret&color=purple', '')
url = urlunparse(components)
print(url)  # http://www.example.com/some/page?name=ferret&color=purple
```

[python] ¡Claro! Vamos a profundizar en el análisis de URLs usando el paquete `urllib.parse` de Python. Para comenzar, es importante entender la estructura básica de una URL.

### Estructura de una URL

Una URL (Uniform Resource Locator) tiene varios componentes. Aquí está la estructura general:

```
scheme://netloc/path;parameters?query#fragment
```

- **scheme**: El esquema indica el protocolo a utilizar (por ejemplo, `http`, `https`, `ftp`).
- **netloc**: La parte de la red, que incluye el dominio y, opcionalmente, el puerto (por ejemplo, `www.example.com` o `www.example.com:8080`).
- **path**: La ruta al recurso en el servidor (por ejemplo, `/path/to/page`).
- **parameters**: Información adicional separada por punto y coma (`;`) que se aplica al recurso.
- **query**: La cadena de consulta que contiene datos para ser enviados al servidor (por ejemplo, `?name=ferret&color=purple`).
- **fragment**: Una referencia a una sección específica dentro del recurso (por ejemplo, `#section2`).

### Uso de `urllib.parse` para analizar URLs

El submódulo `urllib.parse` de Python proporciona una variedad de herramientas para analizar, manipular y construir URLs. Estos ejemplos cubren los casos más comunes y deberían darte una base sólida para trabajar con URLs en tus proyectos de Python. 

El submódulo `urllib.parse` proporciona varias funciones para manejar URLs. Vamos a ver algunas de las más importantes y útiles:

- `urlparse()`: Analiza una URL en sus componentes.
- `urlunparse()`: Construye una URL a partir de sus componentes.
- `urlsplit()`: Similar a `urlparse()` pero trata parámetros y la cadena de consulta como partes separadas.
- `urlunsplit()`: Construye una URL a partir de componentes divididos por `urlsplit()`.
- `urljoin()`: Combina una URL base con una URL relativa.
- `parse_qs()`: Convierte una cadena de consulta en un diccionario.
- `parse_qsl()`: Convierte una cadena de consulta en una lista de pares clave-valor.

### Ejemplos prácticos

#### Ejemplo 1: Análisis de una URL con `urlparse`

```python
from urllib.parse import urlparse

# URL a analizar
url = 'http://www.example.com:8080/path/to/page?name=ferret&color=purple#section2'

# Analizar la URL
parsed_url = urlparse(url)

print('Esquema:', parsed_url.scheme)         # http
print('Netloc:', parsed_url.netloc)         # www.example.com:8080
print('Ruta:', parsed_url.path)             # /path/to/page
print('Parámetros:', parsed_url.params)     # (vacío en este caso)
print('Consulta:', parsed_url.query)        # name=ferret&color=purple
print('Fragmento:', parsed_url.fragment)    # section2
```

#### Ejemplo 2: Construcción de una URL con `urlunparse`

```python
from urllib.parse import urlunparse

# Componentes de la URL
scheme = 'https'
netloc = 'www.example.com'
path = '/new/path'
params = ''
query = 'type=animal&name=ferret'
fragment = 'info'

# Construir la URL
constructed_url = urlunparse((scheme, netloc, path, params, query, fragment))
print('URL construida:', constructed_url)
```

#### Ejemplo 3: Análisis y reconstrucción con `urlsplit` y `urlunsplit`

```python
from urllib.parse import urlsplit, urlunsplit

# URL a analizar
url = 'http://www.example.com/path;params?name=ferret&color=purple#section2'

# Analizar la URL
split_url = urlsplit(url)

print('Esquema:', split_url.scheme)       # http
print('Netloc:', split_url.netloc)       # www.example.com
print('Ruta:', split_url.path)           # /path
print('Parámetros:', split_url.query)    # name=ferret&color=purple
print('Fragmento:', split_url.fragment)  # section2

# Reconstruir la URL
reconstructed_url = urlunsplit(split_url)
print('URL reconstruida:', reconstructed_url)
```

#### Ejemplo 4: Combinación de URLs con `urljoin`

```python
from urllib.parse import urljoin

# URL base y relativa
base_url = 'http://www.example.com/path/to/page'
relative_url = '../another/page?name=ferret'

# Combinar las URLs
combined_url = urljoin(base_url, relative_url)
print('URL combinada:', combined_url)
```

#### Ejemplo 5: Conversión de cadena de consulta a diccionario con `parse_qs`

```python
from urllib.parse import parse_qs

# Cadena de consulta
query_string = 'name=ferret&color=purple&color=blue'

# Convertir a diccionario
query_dict = parse_qs(query_string)
print('Diccionario de consulta:', query_dict)
```

#### Ejemplo 6: Conversión de cadena de consulta a lista de pares clave-valor con `parse_qsl`

```python
from urllib.parse import parse_qsl

# Cadena de consulta
query_string = 'name=ferret&color=purple&color=blue'

# Convertir a lista de pares clave-valor
query_list = parse_qsl(query_string)
print('Lista de consulta:', query_list)
```

## El paquete `request`

¡Hola a todos! Hoy vamos a aprender sobre el paquete `requests` en Python, que es una herramienta muy poderosa para hacer solicitudes HTTP de manera sencilla. Vamos a ver para qué se utiliza, algunos ejemplos prácticos, los principales métodos que ofrece, y cómo hacer solicitudes a una API con credenciales.

El paquete `requests` es extremadamente útil para interactuar con APIs y realizar solicitudes HTTP en Python. Con sus métodos intuitivos y su manejo sencillo de las respuestas, es una herramienta indispensable para cualquier desarrollador que necesite trabajar con servicios web. 

### ¿Qué es el paquete `requests`?

El paquete `requests` es una biblioteca de Python que facilita el envío de solicitudes HTTP. Nos permite interactuar con servicios web de manera muy intuitiva y con una sintaxis simple y directa. Es una de las bibliotecas más populares para realizar solicitudes HTTP debido a su facilidad de uso y su potente funcionalidad.

### Instalación

Primero, asegúrate de tener instalado el paquete. Puedes instalarlo usando `pip`:

```bash
pip install requests
```

### Principales métodos del paquete `requests`

Los métodos más utilizados en `requests` son:

- `requests.get()`: Para obtener datos de un recurso.
- `requests.post()`: Para enviar datos a un servidor para crear un nuevo recurso.
- `requests.put()`: Para actualizar un recurso existente.
- `requests.delete()`: Para eliminar un recurso.
- `requests.head()`: Para obtener los encabezados de una respuesta sin el cuerpo.
- `requests.options()`: Para obtener información sobre las opciones de comunicación con el servidor.

### Ejemplos básicos

#### Hacer una solicitud GET

Vamos a empezar con un ejemplo básico de cómo hacer una solicitud GET a una API pública:

```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # Debe imprimir 200 si la solicitud fue exitosa
print(response.json())  # Devuelve la respuesta en formato JSON
```

#### Hacer una solicitud POST

Ahora veamos un ejemplo de cómo enviar datos a un servidor usando una solicitud POST:

```python
import requests

data = {
    'username': 'example_user',
    'password': 'example_password'
}

response = requests.post('https://httpbin.org/post', data=data)
print(response.status_code)  # Debe imprimir 200 si la solicitud fue exitosa
print(response.json())  # Devuelve la respuesta en formato JSON
```

### Solicitud con credenciales a una API

Supongamos que necesitamos hacer una solicitud a una API que requiere autenticación mediante una clave API (API key). Veamos cómo hacerlo:

```python
import requests

url = 'https://api.example.com/data'
headers = {
    'Authorization': 'Bearer your_api_key_here'
}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())
```

En este ejemplo, hemos agregado un encabezado de autorización (`Authorization`) con una clave API para autenticarnos con el servidor.

### Ejemplo completo: Haciendo una solicitud a una API con credenciales

Vamos a realizar un ejemplo más completo donde hacemos una solicitud a una API de prueba que requiere autenticación con un token:

```python
import requests

# URL de la API
api_url = 'https://api.example.com/protected/data'

# Cabeceras con el token de autenticación
headers = {
    'Authorization': 'Bearer your_api_token_here'
}

# Hacer la solicitud GET
response = requests.get(api_url, headers=headers)

# Comprobar el estado de la respuesta
if response.status_code == 200:
    # Imprimir los datos obtenidos
    print('Datos:', response.json())
else:
    print('Error:', response.status_code, response.text)
```

En este ejemplo, estamos usando una API ficticia `https://api.example.com/protected/data` y enviamos un token de autenticación en las cabeceras de la solicitud. Verificamos si la solicitud fue exitosa comprobando el código de estado y luego imprimimos los datos obtenidos.

____

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

Junio 2024
