"""
**Objetivo:** Realizar una solicitud GET a una API protegida 
con autenticación básica y manejar los encabezados de la solicitud.

**Instrucciones:**

1. Usa `requests` para hacer una solicitud GET a la API 
    `https://httpbin.org/basic-auth/user/passwd`.
2. Agrega autenticación básica con usuario `user` y contraseña `passwd`.
3. Agrega un encabezado personalizado a la solicitud.
4. Imprime el estado de la respuesta y los encabezados de la respuesta.

# Encabezados personalizados
headers = {
    'Custom-Header': 'CustomValue'
}

# Realizar la solicitud GET con autenticación básica
response = requests.get(url, headers=headers, auth=HTTPBasicAuth('user', 'passwd'))

# Verificar que la solicitud fue exitosa
if response.status_code == 200:

print('Encabezados de la respuesta:')
for key, value in response.headers.items():
    print(f'{key}: {value}')

"""

import requests
from requests.auth import HTTPBasicAuth

# URL de la API protegida
URL = 'https://httpbin.org/basic-auth/user/passwd'
