# Valores aleatorios con la funcion randint()

# Importacion de modulos

# import random, en el caso de hagamos eso tenemos que indicar siempre nombre_modulo.funcion()
from random import randint

# Generar un numero aleatorio entre 1 y 10

numero = randint(1,10)
print(f'Numero aleatorio entre 1 y 10: {numero}')

# Simular un dado de 6 caras

dado = randint(1, 6)
print(f'Resultado de lanzar el dado {dado}')
