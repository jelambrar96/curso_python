"""
### Ejercicio 3: Enviar datos mediante una solicitud POST

**Objetivo:** Enviar datos a un servidor usando una solicitud POST y manejar la respuesta.

**Instrucciones:**

1. Usa `urllib.request` para enviar una solicitud POST a `https://httpbin.org/post`.
2. Envía un diccionario de datos con los campos `username` y `password`.
3. Lee la respuesta del servidor y conviértela en un diccionario.
4. Imprime los datos enviados y la respuesta del servidor.

TIPS:

# Datos a enviar
data = {
    'username': 'example_user',
    'password': 'example_password'
}

# Codificar los datos
encoded_data = urllib.parse.urlencode(data).encode('utf-8')

# Enviar la solicitud POST
request = urllib.request.Request(url, data=encoded_data)
response = urllib.request.urlopen(request)

# Leer y decodificar la respuesta
response_data = response.read().decode('utf-8')

"""

import urllib.request
import urllib.parse
import json

# URL del servidor
url = 'https://httpbin.org/post'
