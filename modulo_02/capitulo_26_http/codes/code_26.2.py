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
