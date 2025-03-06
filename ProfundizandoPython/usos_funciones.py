# Las funciones en python son ciudadanas de primera clase
# First class citizens


# Definimos la funcion

def sumar(a,b):
    return a + b

# 1. Asignar una funcion a una variable (No se usan parentesis)
mi_funcion = sumar # SIN PARENTESIS!!
# Verificar el tipo de la variable
print(type(mi_funcion))

# Llamamos la funcion a traves de la variable
resultado = mi_funcion(5,6)
print(f'Resultado: {resultado}')

# 2. Funcion como argumento
def operacion(a,b, sumar_arg):
    print(f'Resultado de sumar: {sumar_arg(a,b)}')

operacion(4,5,mi_funcion)


# 3. Podemos devolver una funcuion
def devolver_funcion():
    # Devolvemos una funcion
    return sumar

mi_funcion_devuelta = devolver_funcion()
print(f'Resultado de la funcion devuelta: {mi_funcion_devuelta(5,6)}')

# Esto son los tres usos que le podemos dar a una funcion


