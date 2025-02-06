# Separar cadenas, usando el metodo .split()

datos = "Hola Mundo"
lista = datos.split() # por default separa cada elemnto por espacios en blanco
print(lista)

datos = "Juan,30,Mexico"
lista = datos.split(',')
print(lista)