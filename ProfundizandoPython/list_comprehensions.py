numeros = range(10)
lista_pares = []

# Creamos una nueva lista con los valores pares multiplicados por si mismos
for numero in numeros:
    # Revisamos si es un numero par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)

print(f'Lista de pares: {lista_pares}')

# Hacemos lo mismo pero con list comprehensions
# [expresion for var in coleccion if condicion]
# La parte del if es OPCIONAL
lista_pares = []
# Antes de que se agrege el numero a lista se comprueba la condicion 'if numero % 2 == 0'
lista_pares = [numero*numero for numero in numeros if numero % 2 == 0] # Es lo mismo que el de arriba pero todo esto simplifica nuestro codigo
print(f'Lista de pares con list comprehensions: {lista_pares}')

# Un ejemplo similar con dos condiciones (las condiciones son opcionales)
# Solo se agrega el valor a la lista cuando el valor cumple ambas condiciones (and)
# Es decir, debe ser divisible entre 2 y divisble entre 6
pares = [numero for numero in range(50) if numero % 2 == 0 and numero % 6 == 0]
print(f'Lista divisible entre 2 y entre 6: {pares}')

# Agregando if else
lista_pares = []
lista_impares = []
for numero in range(10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
print(f'Lista de pares: {lista_pares}')
print(f'Lisat de impares: {lista_impares}')

# El mismo ejercicio pero usando list comprehension

lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero % 2==0 else lista_impares.append(numero)
for numero in range(10)]
print(f'Lista de pares usando list comprehension: {lista_pares}')
print(f'Lisat de impares usando list comprehension: {lista_impares}')

# Lista de listas
lista_listas = [[1,2,3],[4,5,6],[7,8,9,10]]
# Convertimos la lista de listas en una sola lista
lista_simple = [valor
                for sublista in lista_listas # Primero obtenemos cada sublista
                for valor in sublista] # De cada sublista obtenemos los elementos y lo agregamos todo a la lista_simple

print(f'Lista Simple: {lista_simple}')

# Ahora creamos una lista de numeros pares a partir de la lista_listas
# Sin list comprehension, usamos ciclos for anidados
lista_pares = []
for sublista in lista_listas:
    for valor in sublista:
        if valor % 2 == 0:
            lista_pares.append(valor)

print(f'Lista pares: {lista_pares}')

# Con list comprehension, en una sola linea de codigo
# No es necesario separar las lineas, solo es para mejor lectura de codigo
lista_pares = []
lista_pares = [valor
               for sublista in lista_listas
               for valor in sublista if valor % 2 == 0]
print(f'Lista pares con list comprehension: {lista_pares}')
