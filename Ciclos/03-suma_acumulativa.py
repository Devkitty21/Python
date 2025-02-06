print('*** Suma Acumulativa ***')

# Sumar los primeros 5 numeros usando un ciclo while

MAXIMO = 5
numero = 1
acumulador_suma = 0


# Empezamos a iterar

while numero <= MAXIMO:
    print(f'(acumulador_suma + numero) -> {acumulador_suma} + {numero}')
    acumulador_suma += numero
    numero += 1

    print(f'Suma parcial acumuluda: {acumulador_suma}\n')
print(f'\nResultado de la suma acumulada: {acumulador_suma}')

