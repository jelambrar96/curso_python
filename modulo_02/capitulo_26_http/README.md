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
____

Made with Love ❤️ by [@jelambrar96](https://github.com/jelambrar96)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/jelambrar1)

Junio 2024
