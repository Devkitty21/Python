# Un closure es una funcion que define a otra, y ademas la regresa
# La funciona anidada pueda acceder a las variables locales definidas
# en la funcion principal o externa

# Funcion principal (externa)
# def operacion(a,b):
#     # Definimos una funcionn interna o anidada
#     def sumar():
#         return a + b
#
#     # Retornamos la funcion
#     return sumar
#

# Funcion principal 2
def operacion(a,b):
    # 1. Definimos una funcion lambda interna o anidad
    return lambda: a+b

mi_funcion_closure = operacion(5,2)
print(f'Resultado de la funcion closure: {mi_funcion_closure()}')


# Llamar la funcion regresada al vuelo
print(f'Resultado de la funcion closure al vuelo: {operacion(2,3)()}') # Primero ejecutamos la funcion operacion y poniendo unos () se llama a la funcion sumar


# Ejemplos de llamar la funcion al vuelo

# Ejemplo sin "al vuelo"
mi_funcion = operacion(2,3)  # Guardamos la función
print(mi_funcion())  # Luego la ejecutamos

# Ejemplo con "al vuelo"
print(operacion(2,3)())  # Se ejecuta en una sola línea

# La diferencia principal es que en vez de guardarlo en una variable para despues imprimir directamente
# lo ejecutamos en una linea


