from http.server import BaseHTTPRequestHandler, HTTPServer
from http.cookies import SimpleCookie
import urllib.parse

# Definimos nuestra clase manejadora del servidor
class MyHandler(BaseHTTPRequestHandler):
    # Método para manejar las peticiones GET
    def do_GET(self):
        # Análisis de la URL y obtención de parámetros
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        
        # Inicializamos el nombre a None
        name = None
        
        # Verificamos si hay un parámetro 'name' en la URL
        if 'name' in query_params:
            name = query_params['name'][0]
        
        # Manejamos las cookies
        cookie = SimpleCookie(self.headers.get('Cookie'))
        
        if name:
            # Si se proporciona un nombre, lo guardamos en una cookie
            cookie['name'] = name
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Set-Cookie', cookie.output(header='', sep=''))
            self.end_headers()
            self.wfile.write(f"Hola {name}".encode())
        else:
            # Si no se proporciona un nombre, intentamos obtenerlo de las cookies
            if 'name' in cookie:
                name = cookie['name'].value
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f"Hola {name}".encode())
            else:
                # Si no hay nombre en la URL ni en las cookies, pedimos al usuario que lo proporcione
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write("Hola Extraño!!!!!".encode())

# Definimos la función principal para ejecutar el servidor
def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor corriendo en el puerto {port}...')
    httpd.serve_forever()

# Ejecutamos la función principal
if __name__ == '__main__':
    run()