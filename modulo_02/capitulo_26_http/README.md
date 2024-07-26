# Capítulo 26: El paquete `http`

¡Hola a todos! Hoy vamos a aprender sobre el paquete `http` en Python, que forma parte de la biblioteca estándar y proporciona una serie de clases y funciones para manejar solicitudes y respuestas HTTP. Veremos para qué se utiliza, algunos ejemplos prácticos y cómo se pueden manejar diferentes aspectos de HTTP.

El paquete `http` en Python es una herramienta poderosa para trabajar con el protocolo HTTP tanto del lado del cliente como del servidor. Aunque puede ser un poco más complejo que bibliotecas de terceros como `requests`, ofrece una gran flexibilidad y está incluido en la biblioteca estándar de Python, lo que significa que no necesitas instalar paquetes adicionales para usarlo.

### ¿Qué es el paquete `http`?

El paquete `http` en Python proporciona una colección de módulos para trabajar con el protocolo HTTP. Está dividido en varios submódulos, cada uno con su funcionalidad específica:

- `http.client`: Para realizar solicitudes HTTP.
- `http.server`: Para crear servidores HTTP.
- `http.cookies`: Para trabajar con cookies HTTP.
- `http.cookiejar`: Para manejar cookies de manera más avanzada.

### Ejemplos de uso de `http.client`

El submódulo `http.client` permite realizar solicitudes HTTP desde el cliente. Aquí hay un ejemplo de cómo hacer una solicitud GET:

#### Hacer una solicitud GET

```python
import http.client

# Conectar al servidor
conn = http.client.HTTPSConnection("www.example.com")

# Enviar una solicitud GET
conn.request("GET", "/")

# Obtener la respuesta
response = conn.getresponse()
print(response.status, response.reason)

# Leer el contenido de la respuesta
data = response.read()
print(data)

# Cerrar la conexión
conn.close()
```

#### Hacer una solicitud POST

Aquí hay un ejemplo de cómo enviar datos usando una solicitud POST:

```python
import http.client
import json

# Conectar al servidor
conn = http.client.HTTPSConnection("www.example.com")

# Crear los datos para enviar
payload = json.dumps({
    'username': 'example_user',
    'password': 'example_password'
})

# Enviar una solicitud POST
headers = {'Content-type': 'application/json'}
conn.request("POST", "/login", body=payload, headers=headers)

# Obtener la respuesta
response = conn.getresponse()
print(response.status, response.reason)

# Leer el contenido de la respuesta
data = response.read()
print(data)

# Cerrar la conexión
conn.close()
```

### Ejemplos de uso de `http.server`

El submódulo `http.server` permite crear servidores HTTP simples. Aquí hay un ejemplo de cómo crear un servidor HTTP básico que maneja solicitudes GET:

#### Crear un servidor HTTP básico

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, world!")

# Configurar y ejecutar el servidor
server_address = ('', 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print("Server running on port 8000...")
httpd.serve_forever()
```

### Ejemplos de uso de `http.cookies`

El submódulo `http.cookies` permite trabajar con cookies HTTP. Aquí hay un ejemplo de cómo crear y leer cookies:

#### Crear y leer cookies

```python
from http.cookies import SimpleCookie

# Crear una cookie
cookie = SimpleCookie()
cookie["username"] = "example_user"
cookie["username"]["domain"] = "example.com"
cookie["username"]["path"] = "/"

# Imprimir la cookie
print(cookie.output())

# Leer una cookie
cookie_string = "username=example_user"
cookie = SimpleCookie()
cookie.load(cookie_string)

# Obtener el valor de la cookie
print(cookie["username"].value)
```

### Clases Principales del paquete Http

El paquete `http.server` es una herramienta poderosa y flexible para crear servidores HTTP en Python. La clase `BaseHTTPRequestHandler` permite manejar diferentes tipos de solicitudes HTTP personalizando los métodos, mientras que la clase `HTTPServer` se encarga de la configuración y ejecución del servidor.

#### BaseHTTPRequestHandler

La clase `BaseHTTPRequestHandler` es la base para manejar solicitudes HTTP. Define métodos que se pueden sobreescribir para manejar diferentes tipos de solicitudes HTTP, como `GET`, `POST`, `PUT`, `DELETE`, etc. Aquí están algunos de los métodos importantes:

- `do_GET(self)`: Maneja las solicitudes GET.
- `do_POST(self)`: Maneja las solicitudes POST.
- `send_response(self, code, message=None)`: Envía una línea de estado HTTP.
- `send_header(self, keyword, value)`: Envía un encabezado HTTP.
- `end_headers(self)`: Finaliza los encabezados HTTP.

#### HTTPServer

La clase `HTTPServer` representa un servidor HTTP. Se utiliza para crear el servidor, especificar la dirección y el puerto en los que escuchará y asociarlo con una clase de manejador de solicitudes.

### Ejemplo 1: Crear un servidor HTTP básico

Vamos a crear un servidor HTTP básico que maneje solicitudes GET.

**Código:**

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enviar respuesta de estado
        self.send_response(200)
        # Enviar encabezados de la respuesta
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Enviar el cuerpo de la respuesta
        self.wfile.write(b"Hola, mundo!")

# Configurar la dirección y el puerto del servidor
server_address = ('', 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print("Servidor corriendo en el puerto 8000...")
# Ejecutar el servidor
httpd.serve_forever()
```

### Ejemplo 2: Manejar solicitudes POST

Ahora, vamos a expandir nuestro servidor para manejar solicitudes POST. Este servidor recibirá datos en formato JSON y responderá con un mensaje de confirmación.

**Código:**

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hola, mundo!")

    def do_POST(self):
        # Leer la longitud del contenido
        content_length = int(self.headers['Content-Length'])
        # Leer el contenido
        post_data = self.rfile.read(content_length)
        # Convertir el contenido de JSON a un diccionario
        data = json.loads(post_data)

        # Enviar respuesta de estado
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        # Enviar el cuerpo de la respuesta
        response = {
            'message': 'Datos recibidos',
            'data': data
        }
        self.wfile.write(json.dumps(response).encode('utf-8'))

server_address = ('', 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print("Servidor corriendo en el puerto 8000...")
httpd.serve_forever()
```

### Ejemplo 3: Servir archivos estáticos

Finalmente, vamos a crear un servidor que sirva archivos estáticos desde un directorio específico. Usaremos la clase `SimpleHTTPRequestHandler` que ya incluye funcionalidad para servir archivos.

**Código:**

```python
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

# Configurar el directorio de trabajo
os.chdir('/path/to/your/static/files')

# Configurar la dirección y el puerto del servidor
server_address = ('', 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print("Servidor corriendo en el puerto 8000...")
httpd.serve_forever()
```

### ¿Qué es `http.cookies`?

El submódulo `http.cookies` proporciona clases y funciones para la creación, manipulación y análisis de cookies HTTP. Las cookies son pequeñas piezas de datos que los servidores pueden enviar a los navegadores y que los navegadores almacenan y envían de vuelta al servidor con solicitudes futuras. Esto permite mantener el estado entre las solicitudes HTTP, que son de otra manera sin estado. Las clases principales en este submódulo son:

- `SimpleCookie`: La clase principal para trabajar con cookies. Permite crear y manejar cookies de manera sencilla.
- `BaseCookie`: Una clase base para manejar cookies, que es más general y menos específica que `SimpleCookie`.

### Creación de Cookies

Vamos a ver cómo crear cookies usando `SimpleCookie`.

#### Ejemplo 1: Crear una cookie

```python
from http.cookies import SimpleCookie

# Crear una instancia de SimpleCookie
cookie = SimpleCookie()

# Asignar valores a la cookie
cookie["username"] = "john_doe"
cookie["username"]["domain"] = "example.com"
cookie["username"]["path"] = "/"

# Imprimir la cookie en formato HTTP
print(cookie.output())
```

Este código crea una cookie con el nombre `username` y el valor `john_doe`. También establece el dominio y la ruta de la cookie.

### Análisis de Cookies

El submódulo `http.cookies` también permite analizar cookies de una cadena de cookies recibida en una solicitud HTTP.

#### Ejemplo 2: Analizar una cadena de cookies

```python
from http.cookies import SimpleCookie

# Cadena de cookies recibida en una solicitud HTTP
cookie_string = "username=john_doe; session_token=abc123"

# Crear una instancia de SimpleCookie y cargar la cadena de cookies
cookie = SimpleCookie()
cookie.load(cookie_string)

# Acceder a los valores de las cookies
username = cookie["username"].value
session_token = cookie["session_token"].value

print("Username:", username)
print("Session Token:", session_token)
```

Este código analiza una cadena de cookies y extrae los valores de las cookies `username` y `session_token`.

Este es otro ejemplo: 

```python
from http.cookies import BaseCookie

# Crear una instancia de BaseCookie
cookie = BaseCookie()

# Asignar valores a las cookies
cookie["username"] = "john_doe"
cookie["session_token"] = "abc123"

# Establecer propiedades adicionales
cookie["username"]["domain"] = "example.com"
cookie["username"]["path"] = "/"
cookie["session_token"]["httponly"] = True

# Imprimir las cookies en formato HTTP
for key, morsel in cookie.items():
    print(f'{key}: {morsel.OutputString()}')
```

### Manipulación de Cookies

Puedes agregar, modificar y eliminar cookies usando `SimpleCookie`.

#### Ejemplo 3: Modificar y eliminar cookies

```python
from http.cookies import SimpleCookie

# Crear una instancia de SimpleCookie y agregar cookies
cookie = SimpleCookie()
cookie["username"] = "john_doe"
cookie["session_token"] = "abc123"

# Modificar el valor de una cookie
cookie["username"] = "jane_doe"

# Eliminar una cookie
del cookie["session_token"]

# Imprimir la cookie en formato HTTP
print(cookie.output())
```

Este código muestra cómo modificar el valor de una cookie existente y eliminar una cookie.

Este es otro ejemplo:

```python
from http.cookies import BaseCookie

# Cadena de cookies recibida en una solicitud HTTP
cookie_string = "username=john_doe; session_token=abc123"

# Crear una instancia de BaseCookie y cargar la cadena de cookies
cookie = BaseCookie()
cookie.load(cookie_string)

# Acceder a los valores de las cookies
username = cookie["username"].value
session_token = cookie["session_token"].value

print("Username:", username)
print("Session Token:", session_token)
```

### Envío de Cookies desde un Servidor

Vamos a ver un ejemplo de cómo enviar cookies desde un servidor HTTP usando `http.server`.

#### Ejemplo 4: Enviar cookies desde un servidor HTTP

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
from http.cookies import SimpleCookie

class CookieHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Crear una instancia de SimpleCookie
        cookie = SimpleCookie()
        cookie["username"] = "john_doe"
        
        # Enviar respuesta de estado
        self.send_response(200)
        
        # Agregar encabezados de cookies
        for morsel in cookie.values():
            self.send_header("Set-Cookie", morsel.OutputString())
        
        # Finalizar encabezados
        self.end_headers()
        
        # Enviar el cuerpo de la respuesta
        self.wfile.write(b"Cookies enviadas!")

# Configurar la dirección y el puerto del servidor
server_address = ('', 8000)
httpd = HTTPServer(server_address, CookieHTTPRequestHandler)

print("Servidor corriendo en el puerto 8000...")
# Ejecutar el servidor
httpd.serve_forever()
```

En este ejemplo, el servidor HTTP envía una cookie `username` al cliente cada vez que se realiza una solicitud GET.

## Despedida

Espero que esta clase te haya dado una buena introducción a cómo crear servidores HTTP básicos en Python. Te animo a experimentar más con estas herramientas y crear servidores más complejos y útiles. ¡Feliz codificación!

____

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

Junio 2024
