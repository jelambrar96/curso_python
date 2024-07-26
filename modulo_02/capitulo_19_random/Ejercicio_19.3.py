##Ejercicio 19.3

#Eres profesor de una clase y tienes 12 estudiantes, Organizalos aleatoriamente en grupos de 3 estudiantes


import random


def batched(iterable, n=1):
    """batched"""
    salida = []
    grupo = []
    for item in iterable:
        if len(grupo) == n:
            salida.append(grupo[:])
            grupo = []
        grupo.append(item)
    return salida


estudiantes = [
    "Jorge",
    "Luis",
    "Alan",
    "Gerson",
    "Osman",
    "Andrés",
    "Roxana",
    "Kevin",
    "Jairo",
    "Alejandro",
    "David",
    "Jesús"
]

# salida ejemplo
# [("David", "Jairo", "Osman"), ("Jorge", "Kevin", "Roxana"), ...]


# TIP 
# descomenta este codigo para que veas lo que hace la funcion batched
# salida = batched(estudiantes, n=3)
# print(salida)

