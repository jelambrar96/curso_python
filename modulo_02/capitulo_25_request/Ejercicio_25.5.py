"""
### Ejercicio 2: Enviar datos mediante una solicitud POST

**Objetivo:** Enviar datos a una API usando una solicitud POST y manejar la respuesta.

**Instrucciones:**

1. Usa `requests` para enviar una solicitud POST a la API `https://jsonplaceholder.typicode.com/posts`.
2. Envía un diccionario de datos con los campos `title`, `body`, y `userId`.
3. Lee la respuesta del servidor y conviértela en un diccionario.
4. Imprime los datos enviados y la respuesta del servidor.

# Datos a enviar
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Enviar la solicitud POST
response = requests.post(url, json=data)

# Convertir la respuesta a JSON
response_data = response.json()

"""

import requests

# URL de la API
url = 'https://jsonplaceholder.typicode.com/posts'
