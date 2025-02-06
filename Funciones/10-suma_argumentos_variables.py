print(f'*** Suma con Argumentos variables ***')

# Funcion sumar que acepta argumentos variables

def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado_suma = sumar(1,2,3,4,5,6,7,8,9,10)
print(f'El resultado de la suma es: {resultado_suma}')