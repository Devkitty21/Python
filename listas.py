# Profundizando en listas

# Las listas son mutables (Modificar, eliminar agregar...)

nombres1 = ['Pedro','Juan','Karla']
nombres2 = 'Laura Maria Gonzalo Ernesto'.split(' ')
# Sumar listas
print(f'Sumar listas: {nombres1 + nombres2}')

# Extender una lista con otra lista
nombres1.extend(nombres2) # Agregamos los elementos de la lista nombres2 a nombres1
print(f'Extender la lista1 con la lista2: {nombres1}')

# Lista de numeros
numeros = [10, 40, 15, 4, 20, 90, 4]
print(f'Lista original: {numeros}')
# Obtener el indice del primer elemento encontrado en una lista
# help(list.index)
print(f'Indice del elemento 4: {numeros.index(4)}')

# Invertir el orden de los elementos de una lista
numeros.reverse()
print(f'Lista invertida: {numeros}')

# Ordenar los elemetos de una lista de forma ascendente
numeros.sort()
print(f'Lista ordenada (ascendente): {numeros}')

# Ordenar de manera descendente una lista
numeros.sort(reverse=True) # Para que se ordenen de mayor a menor ya que invertimos
print(f'Lista ordenada (descendente): {numeros}')

# Obtener valor minimo y maximo de una lista
print(f'Valor minimo: {min(numeros)}')
print(f'Valor maximo: {max(numeros)}')

# Copiar los elementos de una lista
# numeros2 = numeros.copy() # Asignamos los valores de la lista numeros y la copiamos en la variable numeros dos
# print(f'Lista copiada: {numeros2}') # Solo va a copiar las referencias pero esta almacenada en otro lugar de la memoria
# print(f'Misma referencia? {numeros is numeros2}, Id numeros: {hex(id(numeros))}, Id numeros2: {hex(id(numeros2))}')
# print(f'Mismo contenido? {numeros == numeros2}')

# Podemos usar el constructor de la lista
# numeros2 = list(numeros) # Creamos un nuevo objeto en memoria con el mismo contenido pero diferente referencia
# print(f'Misma referencia? {numeros is numeros2}, Id numeros: {hex(id(numeros))}, Id numeros2: {hex(id(numeros2))}')
# print(f'Mismo contenido? {numeros == numeros2}')

# Slicing

# numeros2 = numeros[:]
# print(f'Misma referencia? {numeros is numeros2}, Id numeros: {hex(id(numeros))}, Id numeros2: {hex(id(numeros2))}')
# print(f'Mismo contenido? {numeros == numeros2}')

# Multiplicacion listas
lista_multiplicacion = 5*[[2,5]]
print(lista_multiplicacion[0])
# print(f'Misma referencia?: {lista_multiplicacion[0] is lista_multiplicacion[1]}') # Apuntan al mismo objeto en memoria
# print(f'Mismo contenido?: {lista_multiplicacion[0] == lista_multiplicacion[1]}')
lista_multiplicacion[2].append(10) # Se le modifica a todas las listas de lista, esto pasa por que todas las listas apuntan al mismo objeto en memoria
print(lista_multiplicacion)

# Matrices en python (Lista de listas)
matriz = [[10,20],[30,40,50],[60, 70, 80, 90]]
print(f'Matriz original: {matriz}')
print(f'Renglon 0, Columna 0: {matriz[0][0]}')
print(f'Renglon 2, Columna 2: {matriz[2][2]}')
matriz[2][0] = 65 # Modificamos el valor de 60
print(f'Matriz modificada: {matriz}')

lista_listas = [[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
lista_listas.sort(key=len)
print(f'Ordenar lista: {lista_listas}')

# sorted Built-in
# help(sorted)
nombres1 = ['Juan Carlos','Karla','Pedro','Esperanza']
nombres1 = sorted(nombres1) # Ordena de forma ascendente
print(nombres1)

# Ordenar de manera descendente
nombres1 = ['Juan Carlos','Karla','Pedro','Esperanza']
nombres1 = sorted(nombres1,reverse=True)
print(nombres1)

# Ordenar por la cantidad de caracteres
nombres1 = ['Juan Carlos','Karla','Pedro','Esperanza']
nombres1 = sorted(nombres1, key=len)
print(nombres1)

# Built-in reversed
nombres1 = reversed(nombres1)
print(list(nombres1)) # Hay que convertirlo a una lista o a una tupla


