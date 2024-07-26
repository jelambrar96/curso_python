"""
### Ejercicio 3: Construye un servidor en el puerto 8000 que se capaz de utilizar cookies

**Objetivo:** Construye un servidor en el puerto 8000  que al recibir un metodo GET 
muestre un "Hola" seguido del nombre que es introducido a través de la URL y que lo almacene en una cookie.
En caso de no haber introducido algún nombre, debe mostrar el nombre almacenado en la cookie

pasos:

1. construye el servidor en el puerto 8000
2. construyeun objeto cookie que almacene la variable "name"
3. diseña el método doGet que permita al servidor responder ante una petición get
4. aplica urllib para extraer el parámetro nombre
5. guarda el nombre en una cookie
6. imprime el nombre introducido o el valor de la cookie

"""
