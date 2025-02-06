import math

print("*** Constantes en python ***")
PI = 3.14159
print("El valor de pi es:", PI)

NOMBRE_BASE_DATOS = "Clientes_db"
print("Nombre de la base de datos:", NOMBRE_BASE_DATOS)

# Esto NO se debe hacer, no se debe modificar el valor de una constante
NOMBRE_BASE_DATOS = "listado_clientes_db"

print("No cambiar el valor de una constante:",NOMBRE_BASE_DATOS)

# Python permite cambiar el tipo de dato y modificar el valor pero no se debe hacer, es una recomendacion de los programadores

# usar una constante del lenguaje python, aunque en este caso no esta en mayusculas
print("Valor de math.pi", math.pi)