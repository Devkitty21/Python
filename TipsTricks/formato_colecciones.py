# Tip. Dar formato consistente a diccionarios, listas, o cualquier otra coleccion
# en python

# Definicion de una lista en una sola linea
mi_lista = ['Juan','Laura','Guadalupe']

# Dar formato a nuestra lista
mi_lista = [
    'Juan',
    'Laura',
    'Guadalupe'
]

# Dar formato a nuestra lista pero con posibles errores
mi_lista = [
    'Juan',
    'Laura',
    'Guadalupe' # Tenemos que tener cuidado con este tipo de errores, si no agregamos , se concatenan
    'Pedro'
]

# Formato consistente de colecciones implica agregar una coma al final
mi_lista = [
    'Juan', # Por cada elemento que agregamos en una nueva linea, agregamos una coma
    'Laura',
    'Guadalupe',
    'Pedro',
]

mi_tupla = (
    'Juan',
    'Laura',
    'Guadalupe',
    'Pedro',
)


print(mi_tupla)
print(mi_lista)