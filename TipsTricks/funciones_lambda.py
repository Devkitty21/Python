# Las funciones lambda nos permiten declarar funciones anonimas
# en una sola linea de codigo

# Ejemplo de funcion normal
def sumar(a,b):
    return a+b

print(sumar(5,10))

# Funcion lambda
# Sintaxis: variable = lambda (parametros): codigo
sumar_lambda = lambda a,b: a + b
print(sumar_lambda(2,4))

# Con las funciones lambda NO podemos agregar ningun decorador ni mas lineas de codigo
# despues de la funcion lambda

# Utilizando una sola linea de codigo (No es necesario agregar la funcion lambda a una variable)
print(f'Suma de la funcion lambda en una sola linea: {(lambda a,b: a + b)(2,2)}') # Llamamos en esta misma linea de codigo, primero definimos al funcion y luego la mandamos a llamar

# Podemos usar una funcion lambda siempre que necesitemos una funcion muy concreta
# Ej. Ordenar Una lista de tuplas, por su segundo valor, proporcionando una key
lista_tuplas = [(1,'a'),(3,'c'),(2,'b'),(5,'f')]
# lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda tupla: tupla[0], reverse=True)
lista_tuplas_ordenada = sorted(lista_tuplas, key=lambda tupla: tupla[1])
print(lista_tuplas_ordenada)

# Otro ejemplo de ordenamiento usando una expresion lambda
print(list(range(-3,4)))
# Si queremos ordenador por el valor absoluto (sin considerar signo)
for valor in range(-3,4):
    print(valor, valor*valor)

# Ahora lo aplicamos a una expresion lambda
lista_ordenada = sorted(range(-3,4), key=lambda valor: valor*valor)
print(lista_ordenada)

# Las funciones lambda tambien podemos aplicar el concepto de closure
def mostrar(titulo):
    return lambda mensaje: titulo + '. ' + mensaje

mostrar_ing = mostrar('Ingeniero')
mostrar_lic = mostrar('Licenciado')

print(mostrar_ing('Alvaro Dominguez'))
print(mostrar_lic('Pablo motos'))
# Podemos hacer esto tambien al vuelo
print(mostrar('Developer')('Ubaldo Acosta'))

##########################
# Malos usos de las funciones lambda:

# Ejemplos de casos de funciones lambda no recomendables
class Prueba:
    mostrar = lambda self: print('Funcion mostrar desde clase')
    saludar = lambda self: print('Funcion saludar desde clase')

prueba = Prueba()
prueba.mostrar() # Estos casos se pueden usar pero no son recomendables
prueba.saludar()

# Otro ejemplo donde una expresion lambda agregaria complejidad innecesaria al codigo
lista_pares = list(filter(lambda valor: valor % 2 == 0, range(10))) # Esta funcion podria ser compleja para la gente que no ha tratado con este tipo de expresiones
print(f'Lista pares desde expresion lambda: {lista_pares}')

# Resolviendo el mismo ejercicio con list comprehensions
lista_pares_modificada = [valor for valor in range(10) if valor % 2 == 0] # Esta sintaxis puede ser mas clara para gente que ha trabajado con list comprehensions
print(f'Lista pares desde expresion lambda: {lista_pares_modificada}')
