# capítulo 20: Manjejando intervalos de tiempo y fecha: El paquete `time` y `datetime`

# El paquete `time`

```python
import time
```

El paquete `time` en Python es parte de la biblioteca estándar y proporciona varias funciones relacionadas con el tiempo. Es especialmente útil para manejar operaciones relacionadas con tiempos de espera, marcas de tiempo y medición de la duración de las operaciones de código.

### Funcionalidad Básica

El paquete `time` permite a los desarrolladores realizar operaciones basadas en tiempos y fechas, como pausar la ejecución de un programa, obtener la hora actual, y medir el rendimiento de diferentes partes del código.

### Principales Métodos y Ejemplos

1. **`time()`**: Devuelve el tiempo actual en segundos desde la época (1 de enero de 1970, 00:00:00 UTC).

   ```python
   import time
   print(time.time())  # Ejemplo: 1609459200.737163
   ```

2. **`ctime()`**: Convierte un tiempo expresado en segundos desde la época a una cadena representando la hora local.

   ```python
   print(time.ctime(1609459200))  # Ejemplo: 'Fri Jan  1 00:00:00 2021'
   ```

3. **`sleep(seconds)`**: Pausa la ejecución del programa por el número de segundos especificado.

   ```python
   time.sleep(5)  # Pausa el programa por 5 segundos
   ```

4. **`perf_counter()`**: Retorna un contador de rendimiento, es decir, un float que representa el tiempo en segundos, con la mayor resolución disponible para medir un intervalo corto.

   ```python
   start = time.perf_counter()
   time.sleep(2)
   end = time.perf_counter()
   print(f"Tiempo transcurrido: {end - start} segundos")  # Ejemplo: 'Tiempo transcurrido: 2.002 segundos'
   ```

5. **`gmtime(secs)`**: Convierte un tiempo expresado en segundos desde la época en una estructura de tiempo en UTC.

   ```python
   print(time.gmtime(1609459200))  # Ejemplo: time.struct_time(tm_year=2021, tm_mon=1, tm_mday=1, ...)
   ```

6. **`localtime(secs)`**: Similar a `gmtime`, pero convierte a hora local.

   ```python
   print(time.localtime(1609459200))  # Ejemplo: time.struct_time(tm_year=2021, tm_mon=1, tm_mday=1, ...)
   ```

7. **`time.strftime(format, t)`**: Convierte una estructura de tiempo o una tupla de nueve elementos en una cadena de acuerdo con un formato especificado.

   ```python
   formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
   print("Hora formateada:", formatted_time)
   ```

8. **`time.strptime(string, format)`**: Parsea una cadena de tiempo de acuerdo a un formato dado y retorna una estructura de tiempo.

   ```python
   time_string = "2024-05-22 15:30:00"
   parsed_time = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
   print("Año parseado:", parsed_time.tm_year)
   print("Mes parseado:", parsed_time.tm_mon)
   ```

### Recomendaciones al Usar el Paquete `time`

- **Precisión y resolución**: Ten en cuenta que la función `sleep()` no garantiza que el hilo o proceso se reanude exactamente después del tiempo especificado debido a la precisión del sistema operativo y la planificación del procesador. Para mediciones de tiempo más precisas, usa `perf_counter()`.
- **Uso del tiempo de CPU**: Las funciones como `clock()` han quedado obsoletas en Python 3.8 y se recomienda usar `perf_counter()` o `process_time()` para medir el tiempo de CPU.
- **Zonas horarias**: Al convertir tiempos y trabajar con fechas, siempre considera la zona horaria. Las funciones `gmtime()` y `localtime()` no manejan zonas horarias diferentes de UTC y la hora local del sistema, respectivamente.
- **Funciones de bloqueo**: Al usar `sleep()`, recuerda que bloquea la ejecución del hilo en el que se llama, lo que puede no ser deseable en aplicaciones que requieren alta responsividad o en entornos de multitarea.

## El paquete `datetime`

El paquete `datetime` en Python es una biblioteca fundamental para manejar fechas y horas. A diferencia del módulo `time`, que es principalmente para trabajar con tiempos en segundos desde la época, `datetime` permite la manipulación de fechas y horas con mucho más detalle, incluyendo la gestión de zonas horarias, lo cual es esencial para muchas aplicaciones modernas.

### Funcionalidad Básica

`datetime` soporta la creación, manipulación y formateo de objetos de fecha y hora. Es ideal para proyectos que requieren cálculos de fechas, como la gestión de eventos, logística, o interfaces que necesitan mostrar fechas y horas de manera legible.

### Principales Clases y Métodos

1. **`datetime.date`**: Una clase ideal para manejar fechas (año, mes, día).

   ```python
   from datetime import date
   d = date(2021, 1, 1)
   print(d)  # Ejemplo: 2021-01-01
   ```

2. **`datetime.time`**: Una clase para manejar horas, minutos, segundos y microsegundos.

   ```python
   from datetime import time
   t = time(12, 30, 45)
   print(t)  # Ejemplo: 12:30:45
   ```

3. **`datetime.datetime`**: Combina tanto la fecha como la hora en un solo objeto.

   ```python
   from datetime import datetime
   dt = datetime(2021, 1, 1, 12, 30, 45)
   print(dt)  # Ejemplo: 2021-01-01 12:30:45
   ```

4. **`datetime.timedelta`**: Utilizado para calcular diferencias de tiempo y fechas.

   ```python
   from datetime import timedelta
   delta = timedelta(days=1, seconds=3600)  # 1 día y 1 hora
   new_dt = dt + delta
   print(new_dt)  # Ejemplo: 2021-01-02 13:30:45
   ```

### Métodos Útiles

- **`today()`** y **`now()`**: Obtiene la fecha actual.

   ```python
   today = date.today()
   now = datetime.now()
   print(today, now)  # Ejemplo: 2021-01-01, 2021-01-01 12:30:45.000123
   ```

- **`strftime()`**: Formatea objetos de fecha/hora como cadenas.

   ```python
   formatted = now.strftime("%Y-%m-%d %H:%M:%S")
   print(formatted)  # Ejemplo: 2021-01-01 12:30:45
   ```

- **`strptime()`**: Parsea cadenas para convertirlas en objetos `datetime`.

   ```python
   date_str = "01-01-2021 14:20"
   date_object = datetime.strptime(date_str, "%d-%m-%Y %H:%M")
   print(date_object)  # Ejemplo: 2021-01-01 14:20:00
   ```

### Centrémonos en datetime, normalmente es el más usado. 

La clase `datetime` del módulo `datetime` en Python es muy poderosa para trabajar con fechas y horas juntas. Aquí explicaré con ejemplos algunos de sus métodos y atributos más útiles:

### 1. Creación de un objeto `datetime`

- **`datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0)`**: Constructor para crear un objeto `datetime`.

```python
import datetime

# Crear un objeto datetime para el 1 de enero de 2025 a las 15:45
dt = datetime.datetime(2025, 1, 1, 15, 45)
print("Objeto datetime:", dt)
```

### 2. Métodos y Atributos Comunes

- **`now()`**: Retorna la fecha y hora actual del sistema local.
- **`utcnow()`**: Retorna la fecha y hora actual en UTC.
- **`strftime(format)`**: Convierte un objeto `datetime` a una cadena de texto formateada.

```python
# Obtener la fecha y hora actual
ahora = datetime.datetime.now()
print("Ahora:", ahora)

# Obtener la fecha y hora actual en UTC
ahora_utc = datetime.datetime.utcnow()
print("Ahora en UTC:", ahora_utc)

# Formatear la fecha y hora
fecha_formateada = ahora.strftime("%Y-%m-%d %H:%M:%S")
print("Fecha formateada:", fecha_formateada)
```

### 3. Métodos de Manipulación de Fechas

- **`replace(year, month, day, hour, minute, second, microsecond)`**: Devuelve un nuevo objeto `datetime` con el cambio especificado.
- **`timedelta`**: Utilizado para representar una diferencia entre dos fechas u horas.

```python
# Cambiar el año y la hora del objeto datetime
dt_modificado = dt.replace(year=2026, hour=10)
print("DateTime modificado:", dt_modificado)

# Añadir 5 días y 3 horas al objeto datetime
from datetime import timedelta
nueva_fecha = ahora + timedelta(days=5, hours=3)
print("Fecha más 5 días y 3 horas:", nueva_fecha)
```

### 4. Métodos de Comparación

Los objetos `datetime` se pueden comparar usando operadores como `==`, `!=`, `<`, `>`, `<=`, `>=`, lo que es útil para verificar eventos antes o después de cierta fecha y hora.

```python
fecha1 = datetime.datetime(2025, 1, 1)
fecha2 = datetime.datetime(2025, 1, 2)

# Comparar dos fechas
print("¿Fecha1 es antes que Fecha2?", fecha1 < fecha2)
```

### 5. Métodos de Extracción

- **`date()`**: Extrae la fecha de un objeto `datetime`.
- **`time()`**: Extrae la hora de un objeto `datetime`.

```python
# Extraer fecha y hora por separado
solo_fecha = ahora.date()
solo_hora = ahora.time()
print("Solo fecha:", solo_fecha)
print("Solo hora:", solo_hora)
```

Estos ejemplos ilustran cómo puedes trabajar de manera efectiva con fechas y horas en Python usando la clase `datetime`. Este conjunto de herramientas te permite manipular, formatear y comparar fechas y horas de manera poderosa y flexible.

Para extraer información específica como el año, mes, día, día de la semana, hora, minuto y segundo de un objeto `datetime` en Python, puedes utilizar los atributos correspondientes de la clase `datetime`. Aquí te muestro cómo hacerlo con un ejemplo:

```python
import datetime

# Crear un objeto datetime para el 22 de mayo de 2024 a las 15:30:45
dt = datetime.datetime(2024, 5, 22, 15, 30, 45)
print("Objeto datetime completo:", dt)

# Extraer el año
ano = dt.year
print("Año:", ano)

# Extraer el mes
mes = dt.month
print("Mes:", mes)

# Extraer el día
dia = dt.day
print("Día:", dia)

# Extraer el día de la semana (lunes=0, domingo=6)
dia_semana = dt.weekday()
print("Día de la semana (0 es lunes):", dia_semana)

# Extraer la hora
hora = dt.hour
print("Hora:", hora)

# Extraer el minuto
minuto = dt.minute
print("Minuto:", minuto)

# Extraer el segundo
segundo = dt.second
print("Segundo:", segundo)
```

En este código:
- **`year`**, **`month`**, **`day`**, **`hour`**, **`minute`**, y **`second`** son atributos de la instancia `dt` de la clase `datetime`, que te permiten acceder a los componentes individuales de la fecha y hora.
- **`weekday()`** es un método que devuelve el día de la semana, donde lunes es `0` y domingo es `6`.

Estos atributos y métodos son muy útiles cuando necesitas manipular o comparar componentes específicos de fechas y horas en aplicaciones de Python.


### Recomendaciones al Usar el Paquete `datetime`

- **Manejo de zonas horarias**: Para aplicaciones que requieren manejo de diferentes zonas horarias, considera usar `pytz` o `dateutil`, ya que `datetime` por sí solo no maneja zonas horarias de manera muy detallada.
- **Formato de fechas**: Siempre valida y maneja excepciones al convertir cadenas a fechas, especialmente cuando los formatos pueden variar.
- **Dependencias**: Si tu proyecto necesita manipulación avanzada de fechas y horas (por ejemplo, cálculos recurrentes), evalúa librerías adicionales como `pandas` para series temporales.
- **Comparación de fechas y tiempos**: Asegúrate de que las comparaciones de objetos `datetime` consideren el manejo correcto de la igualdad, especialmente si se incluyen componentes de microsegundos.

El paquete `datetime` es extremadamente poderoso y esencial para cualquier programador de Python que necesite trabajar con fechas y horas en sus proyectos.