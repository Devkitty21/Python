# Generador de numeros del 1 al 5

def generador_numeros():
    for numero in range(1,6):
        yield numero
        print(f'Se reanuda la ejecucion de la funcion')

# Utilizamos el generador
generador = generador_numeros()
print(f'Objeto generado: {generador}')
print(f'Tipo de objeto: {generador}')

# Consumir los valores del generador
for valor in generador_numeros():
    print(f'Numero producido: {valor}')

# Consumir a demanda

generador = generador_numeros() # Hay que volver a llamar a la funcion porque no tenemos mas valores para consumir
try:
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
except StopIteration as error:
    print(f'Error al consumir: {error}, {type(error)}')

# Otra forma de consumir un generador
generador = generador_numeros() # Hay que volver a llamar porque hemos consumido todos sus valores
while True:
    try:
        valor = next(generador)
        print(f'Impresion del valor generado: {valor}')
    except StopIteration as error:
        print(f'Error ocurrido: {error}, {type(error)}')
        break

