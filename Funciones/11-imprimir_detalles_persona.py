print(f'*** Imprimir detalles de una persona usando **kwargs ***')

# Funcion que acepta argumentso variables en forma de llave:valor

def persona_detalles(**kwargs): # No tiene porque ser el nombre de "kwargs" pero es recomendacion de python
    print(f'\nValores recibidos de la persona: ')
    for llave, valor in kwargs.items():
        print(f'{llave.title()}: {valor}')

# Llamamos a la funcion
persona_detalles(nombre='Roman', edad=15, ciudad = 'Spain')
persona_detalles(nombre="Carlos", edad=28, ciudad= "Guadalajara", puesto= 'Gerente')
