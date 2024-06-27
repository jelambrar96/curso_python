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
