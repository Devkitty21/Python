# Generadores
# Es una funcion especial, retorna una secuencia de valores
# Suspende la ejecucion de la funcion por medio de la palabra reservada yield (producir) (No se usa return)

def generador():
    yield 1 # Estamos produciendo el valor de 1
    print('Se reanuda la ejecucion')
    yield 2 # Produciendo el valor de 2
    print('Se reanuda la ejecucion')
    yield 3 # Produciendo el valor de 3


# Consumimos el generador a demanda
gen = generador()
#  Con cada llamada consumimos un valor

print(next(gen))
print(next(gen))
print(next(gen))
# Si tratamos de consumir mas valores de los que produce el generador
# nos va a saltar un error de tipo "StopIteration"
# print(next(gen))

# Consumiendo los valores del generador con un ciclo for

for valor in generador():
    print(f'Numero producido: {valor}')