print('*** Comprension de listas ***')

# Una lista para generar el cuadrado de cada numero

numeros = [1,2,3,4,5]
cuadrados = [numero**2 for numero in numeros]
print(cuadrados)

# Lista de numeros pares

numeros = [1,2,3,4,5]
numeros = range(10+1)

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Lista saludando a cada nombre
nombres = ['Ana','Jeronimo','Carlos']
saludando = [f'Hola {nombre}' for nombre in nombres]
print(saludando)

# Suma de valores dentro de una lista

nusmero = [1,2,3,4,5,6]
suma = 0
resultado = []

for n in numeros:
    suma += n
    resultado.append(suma)
print(resultado)
