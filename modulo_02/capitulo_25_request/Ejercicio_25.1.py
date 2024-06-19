"""
Ejercicio 1: Realizar una solicitud GET y extraer información

**Objetivo:** Realizar una solicitud GET a una página web y extraer el título de la página HTML.

**Instrucciones:**

1. Usa `urllib.request` para hacer una solicitud GET a la URL `http://example.com`.
2. Lee el contenido de la respuesta y conviértelo en una cadena.
3. Utiliza el paquete `re` (expresiones regulares) para encontrar y 
    extraer el contenido del título (`<title>`) de la página HTML.
4. Imprime el título extraído.

TIPS: 

# Realizar la solicitud GET
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

# Extraer el título de la página usando expresiones regulares
title_pattern = r'<title>(.*?)</title>'
title_match = re.search(title_pattern, html)

"""

import urllib.request
import re

# URL a la que se realizará la solicitud GET
URL = 'http://github.com/jelambrar96/curso_python'
