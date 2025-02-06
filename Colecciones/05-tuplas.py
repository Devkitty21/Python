print('*** Manejo de Tuplas/Tuples ***')

mi_tupla = (1, 2, 3, 4, 5)

print(mi_tupla)
# No podemos modificar una tupla

# Iteramos los elementos de una tupla

for elemento in mi_tupla:
    print(elemento, end=" ")

# Crear una tupla para una cordenada x,y

coordenadas = (3,5)

# Accedemos a cada elemento de la tupla
print(f'\nCoordenada en el eje x: {coordenadas[0]}')
print(f'Coordeanada en el eje y: {coordenadas[1]}')

# Crear una tupla unitaria

tupla_un_elemento = 10,
print(f'Tupla de un elemento: {tupla_un_elemento}')

# Definir una tupla anidada

tuplas_anidada = (1, (2,3), (3,4))
print(f'Segundo elemento de la tupla anidada: {tuplas_anidada[1]}')