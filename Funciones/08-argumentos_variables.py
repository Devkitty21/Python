print(f'*** Argumentos Variables ***')

def superheroe_superpoderes(superheroe, nombre, *args): #*args debe ir siempre al final nunca ni al principio ni en la mitad
    print(f'Superherore: {superheroe} - {nombre} - {args}')
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')
# Llamamos la funcion
superheroe_superpoderes('Spiderman', 'Peter Parker', "Instinto Aracnido", 'Telarana')
superheroe_superpoderes('Ironman', 'Tony Stark', "Armadura", "Playboy", 'Millonario')

# Es opcional pasarle argumentos al parametro de *args
superheroe_superpoderes('Mi vecino', 'Juan Perez')