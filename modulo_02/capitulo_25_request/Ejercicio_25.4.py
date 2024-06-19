"""
### Ejercicio 1: Realizar una solicitud GET y extraer datos

**Objetivo:** Realizar una solicitud GET a una API pública y extraer información específica de la respuesta JSON.

**Instrucciones:**

1. Usa `requests` para hacer una solicitud GET a la API `https://jsonplaceholder.typicode.com/posts`.
2. Extrae el título y el cuerpo del primer post en la respuesta JSON.
3. Imprime el título y el cuerpo del primer post.

TIPS:

# Realizar la solicitud GET
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # hacer algo
    
# Convertir la respuesta a JSON
posts = response.json()

# Extraer el título y el cuerpo del primer post
first_post = posts[0]
title = first_post['title']
body = first_post['body']

# Imprimir el título y el cuerpo del primer post
print('Título:', title)
print('Cuerpo:', body)

"""

import requests

# URL de la API
url = 'https://jsonplaceholder.typicode.com/posts'
