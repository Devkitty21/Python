print('*** Regresar una Tupla de valores desde una funcion ***')

# Definicion de nuestra funcion

def persona_mayuscula(nombre, apellido, edad):
    print(f'Esta funcion regresa varios valores, es decir una (tupla)')
    return nombre.upper(), apellido.upper(), edad

# Programa principal

# nombre, apellido, edad = persona_mayuscula('Sandra', 'Jimenez', 42) # Aqui tenemos el concepto unpacking
# print(f'Resultado de la persona: Nombre: {nombre}, apellido: {apellido}, edad: {edad}')

resultado = persona_mayuscula('Sandra', 'Jimenez', 42)
nombre, apellido,edad = resultado # Aqui hacemos tambien un unpacking a la tupla
print(f'El nombre es: {nombre}, apellido: {apellido}, y la edad: {edad}')
print(f'Resultado: {resultado}') # Siempre que devolvemos varios valores de una funcion se hacen una tupla

def persona_separada(nombre, apellido):
    print(f'Esta funcion regresa el nombre y el apellido separados y los mete en una tupla')
    return nombre, apellido

resultado_persona_separada = persona_separada(apellido='Suarez',nombre='Luis')
nombre, apellido = resultado_persona_separada
print(f'El nombre de la persona es: {nombre}, y el apellido de la persona: {apellido}')

