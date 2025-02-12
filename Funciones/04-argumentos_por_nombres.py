print('*** Funcion con argumentos por nombre ***')

def imprimir_persona(nombre, apellido='', edad =0): # Agregamos valores por default aqui y no son obligatorios ahora
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# Primero llamamos la funcion pasando los argumentos de manera posicional

imprimir_persona('Roman','Hernandez',15)

# Llamar la funcion usando argumentos por nombre

imprimir_persona(nombre = 'Roman', edad = 15, apellido = 'Hernandez')

# Llamar la funcion usando argumentos por nombre pero intercambiando el orden
imprimir_persona(edad = 15, apellido = 'Rojas', nombre = 'Carlos')

# Argumentos con valor por default

imprimir_persona(nombre='Carlos')
imprimir_persona(nombre='Carlos',apellido='Rojas') # Sobreescribe los valores por default en el caso de que los pongamos como parametros en la funcion
imprimir_persona(apellido='Rojas',nombre='Carlos')