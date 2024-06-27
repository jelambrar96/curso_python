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
