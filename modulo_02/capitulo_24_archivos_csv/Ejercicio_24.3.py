## Ejercicio 24.3

"""
Escribe un programa que lea un archivo CSV llamado empleados.csv.
El archivo inicial contendrá datos de empleados con las columnas: 
    "ID", "Nombre", "Departamento" y "Salario".
El programa debe calcular un aumento del 10% en el salario para 
los empleados del departamento de "IT".
Añadir una nueva columna "Email" basada en los nombres de los empleados 
(formato: nombre.apellido@empresa.com).
Guardar el resultado en un nuevo archivo CSV llamado empleados_actualizados.csv.
"""

import pandas as pd

#Cargar los datos desde un archivo CSV
df = pd.read_csv('empleados.csv')

#Aplica un aumento del 10% en el salario para los empleados del departamento de IT
#Añade tu código aquí

#Genera una columna de email basada en el nombre de los empleados
#Añade tu código aquí

#Guarda el DataFrame actualizado en un nuevo archivo CSV
#Añade tu código aquí

