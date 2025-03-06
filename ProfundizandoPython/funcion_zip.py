# print(dir(__builtins__))
# help(zip)

# Zip - comprimir
numeros = (1,2,3)
letras = ['a','b','c','d']
identificadores = 321, 322, 323, 324, 325 # Va a usar todos los iterables que tengamos pero el zip se va a deter en el objeto con menos elementos
conjunto = {6,4,0,9,8,15,10}
mezcla = zip(numeros,letras, identificadores, conjunto)
# print(mezcla) # Hay que convertirlo en una tupla o lista
print(list(mezcla))
# print(tuple(zip(numeros,letras))) # Si queremos volver a leer el zip tenemos que volver a generarlo por que ya lo hemos consumido arriba
# print(type(mezcla))

# Iterar en paralelo
for numero,letra,id,aleatorio in zip(numeros,letras,identificadores,conjunto):
    print(f'Numero: {numero}, letra: {letra}, id: {id}, Aleatorio: {aleatorio} ')

nueva_lista = []
for numero,letra,id,aleatorio in zip(numeros,letras,identificadores,conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')

print(nueva_lista)

# unzip

mezcla = [(1,'a'),(2,'b'),(3,'c')]

numeros, letras = zip(*mezcla) # Definimos las variables de numeros letras, hacemos un zip para comprimirlo todo en una misma lista y aplicamos unpacking a mezclas para que este todo en lo mismo
print(f'Numeros: {numeros}, Letras: {letras}')

# Ordenamiento usando zip
letras = ['c','d','a','e','b']
numeros = [3,2,4,1,0]
mezcla = zip(letras,numeros)
# Sin orden
print(tuple(mezcla)) # Si mandamos a imprimir aqui este zip ya lo hemos usado por lo cual luego hay que volver a generarlo
# Ordenar por letra (primer iterable)
print(sorted(zip(numeros,letras))) # Estamos ordenando de manera ascendente que es por default
# Depende del orden en el que creemos el zip se hara el orden de los elementos

# Crear un diccionario con zip y dos iterables
llaves = ['Nombre','Apellido','Edad']
valores = ['Juan','Perez',18]
diccionario = dict(zip(llaves,valores))
print(diccionario)

# Actualizar un elemento de un diccionario
llave = ['Edad']
nueva_edad = [28]
diccionario.update(zip(llave,nueva_edad))

print(diccionario)

# Creamos un diccionario con dos listas y el metodo zip

llaves = ['Nombre','Edad']
key = ['Juan',18]
diccionario = dict(zip(llaves,key))
print(f'Lista original: {diccionario}')

# Cambiamos el valor de edad y de nombre
llave = ['Nombre','Edad']
key_nueva = ['Diogo','quince']
diccionario.update(zip(llave,key_nueva))
print(f'Lista modificada: {diccionario}')



