# Expresion generadora (Es un generador anonimo)
# Sintaxis: (expresion for var in coleccion if condicion) # La parte de if es OPCIONAL


multiplicacion = (valor*valor for valor in range(4))
print(f'Multiplicacion: {multiplicacion }{type(multiplicacion)}')
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
# print(next(multiplicacion))

# Tambien se puede pasar una expresion generadora a una funcion sin utilizar parentesis
import math
suma = sum(valor+valor for valor in range(4))
print(f'Resultado de la suma: {suma}')

# Tambien podemos usar una lista o cualquier otro iterador
lista = ['Juan','Perez']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

# Crear un string a a partir de un generador creado a partir de una lista
lista = ['Karla','Gomez',22]
contador = 0
# Definimos una funcion para incrementar el contador
def incrementar():
    global contador
    contador += 1
    return contador

# La primera parte es el yield, la segunda es el for, entre parentesis
generador = (f'{incrementar()}. {elemento}' for elemento in lista)
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(f'Cadena generada: {cadena}')