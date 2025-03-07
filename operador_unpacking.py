# * Desempaquetar
numeros = [1,2,3,4]
print(numeros)
print(*numeros) # Se imprimen cada uno de los elementos de nuestra lista (los estamos desempaquetando)
print(*numeros, sep=' - ') # Este metodo aplica para cualquier iterable menos a diccionarios

# Desempaquetando al momento de pasar un parametro a una funcion
def sumar(a,b,c,d):
    print(f'Resultado de la suma: {a + b + c + d}')

sumar(*numeros) # Utilizamos el operador unpacking para poder pasar 3 argumentos

# Extraer algunas partes de una lista
mi_lista = [1,2,3,4,5,6]
a,*b,c,d = mi_lista
print(a,b,c,d)

# Unir listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1,lista2]
print(f'Lista de listas: {lista3}')
lista3 =[*lista1, *lista2]
print(f'Unir listas: {lista3}')

# Unir diccionarios
dic = {
    'A':1,
    'B':2,
    'C':3
}
dic2 = {
    'D':4,
    'E':5
}

dic3 = {**dic, **dic2} # Desempaquetamos todos los elementos de los diccionarios, y lo almacenamos en la variable 3
print(f'Unir diccionarios: {dic3}')

# Construir una lista a partir de un str
lista = [*'HolaMundo'] # Convertimos la cadena en una lista
print(lista) # Imprimimos la lista
print(*lista, sep='') # Desempaquetamos la lista y quitamos los espacios quitando el separador por default que es un espacio




