"""
### Ejercicio 2: Análisis y construcción de URLs

**Objetivo:** Analizar una URL y luego reconstruirla cambiando algunos de sus componentes.

**Instrucciones:**

1. Usa `urllib.parse` para analizar la URL `http://www.example.com/path/to/page?name=ferret&color=purple`.
2. Extrae y modifica los siguientes componentes:
    - Cambia el esquema a `https`.
    - Cambia el dominio a `www.changedexample.com`.
    - Añade un nuevo parámetro de consulta `age=5`.
3. Reconstruye la URL modificada y imprímela.

TIPS: 

# Analizar la URL
parsed_url = urlparse(url)

# Modificar componentes
scheme = 'https'
netloc = 'www.changedexample.com'
path = parsed_url.path


query = parse_qs(parsed_url.query)
query['age'] = '5'

# Reconstruir la URL
new_query = urlencode(query, doseq=True)
modified_url = urlunparse((scheme, netloc, path, '', new_query, ''))
"""

from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

# URL a analizar
URL = 'http://www.example.com/path/to/page?name=ferret&color=purple'

