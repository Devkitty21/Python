print('*** Manejo de listas ***')

mi_lista = [1, 2, 3, 4, 5]
print(f'{mi_lista} ->  Lista original')

# Obtener el largo de una lista
print(f'Largo de una lista: {len(mi_lista)}')

# Acceder a los elementos de la lista por indice

print(f'Accedemos al elemento almacenado en el indice 4: {mi_lista[4]}')
print(f'Accedemos al elemento almacenado en el ultimo indice: {mi_lista[-1]}')

# Modificar los elementos de una lista
mi_lista[1] = 10
print(f'Modificamos el valor de el indice 1 de nuestra lista: {mi_lista[1]}')

# Agregar un nuevo elemento al final de la lista

mi_lista.append(6)
print(f'Agregando el valor de 6 en la lista: {mi_lista[5]}')

# Agregar un nuevo elemento en un indice especifico

mi_lista.insert(2, 15) # Primero indicamos el indice donde lo queremos colocar y despuyes el valor
print(f'Agregando un valor en el indice 2: {mi_lista}')

# Eliminar elementos de una lista

# Usando el metodo remove
mi_lista.remove(5) # Directamente borramos el elemento que queremos eliminar
print(f'Se ha eliminado el elemento 5 de la lista: {mi_lista}')

# Remover por indice con el metodo pop
mi_lista.pop(1) # Remueve el elemento por el indice
print(f'Removiendo el elemento de la lista en el indice 1: {mi_lista}')

# Eliminar usando la palabra del
del mi_lista[2] # Se le debe de indicar el indice del elemento que queremos eliminar
print(f'Se elimino el indice 2 con la palabra del: {mi_lista}')

# Obtener sublistas

sublista =   mi_lista[1:3] # Genera una sublista del indice 1 al 2 (El valor de 3 no se incluye)
print(f'De la lista: {mi_lista} creamos una sublista: {sublista}')

# Imprimir cada elemento de una lista
numeros = [1,2,3,4,5]
for numero in numeros:
    print(f'El numero es {numero}', end=' ')

