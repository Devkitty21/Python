print('*** Juego de adivinanzas ***')

# Imports
from random import randint

numero_secreto = randint(1,50)
numero_ingresado = int(input('Ingresa el numero: '))
intento = 0
INTENTO_MAXIMO = 10


while numero_ingresado != numero_secreto:
    intento += 1
    print(f'\nEl numero que has introducido no es el correcto!')
    numero_ingresado = int(input('Ingresa el numero: '))
    if intento > INTENTO_MAXIMO:
        print('Has llegado al maximo de intentos, vuelve a jugar mas tarde!')
        break
    elif numero_ingresado < numero_secreto:
        print("El numero secreto es mayor")
    elif numero_ingresado > numero_secreto:
        print('El numero secreto es menor')
else:
    print(f'Felicidades! Has adivinado el numero secreto! Era el numero {numero_secreto}. Has hecho {intento} intentos.')


