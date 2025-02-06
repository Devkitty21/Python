print('*** Valor dentro de rango ***')
VALOR_MINIMO = 0
VALOR_MAXIMO = 5

# Definimos los inputs y variables
numero_rango = int(input(f'Introduce un numero entre el {VALOR_MINIMO} y {VALOR_MAXIMO}: '))

# Comprobacion de si esta dentro del rango o no

dentro_rango = numero_rango >= VALOR_MINIMO and numero_rango <= VALOR_MAXIMO
# dentro_rango = VALOR_MINIMO <= numero_rango <= VALOR_MAXIMO

# Imprimos los valores

print(f'Valor dentro de rango: {dentro_rango}')