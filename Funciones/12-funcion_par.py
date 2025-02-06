print(f'*** Funcion Par ***')

# Funcion para saber si un numero es par o no

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# Llamamos a la funcion

if __name__ == '__main__':
    numero = int(input('Proporciona un valor numerico: '))
    print(f'Numero par? {es_par(numero)}')