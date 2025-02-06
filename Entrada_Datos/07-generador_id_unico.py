# Importacion de modulo

# import random
from random import randint

# Generador de identificacion unico
print('*** Sistema Generador de ID unico ***')


nombre = input('Cual es tu nombre? ')
apellido = input('Cual es tu apellido? ')
anio_nacimiento = input('Cual es tu año de nacimiento (YYYY)? ') # Y - year

# Normalizar los valores

nombre_modificado = nombre[0:2].strip().upper()
apellido_modificado = apellido[0:2].strip().upper()
anio_nacimiento2 = anio_nacimiento[2:].strip() # Tambien puede ser el indice [2:4]

# Generar valor aleatorio
identificador = randint(1000,9999)

# Generar id
id_unico = f"{nombre_modificado}{apellido_modificado}{anio_nacimiento2}{identificador}"

# Imprimimos los valores

print(f"Hola {nombre},")
print('\tTu nuevo numero de identificacion (ID) generado por el sistema es:')
print(f'\t{id_unico}')
print('\tFelicidades!')
