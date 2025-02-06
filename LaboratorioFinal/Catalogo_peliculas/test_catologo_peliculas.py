from LaboratorioFinal.Catalogo_peliculas.dominio.pelicula import Pelicula
from LaboratorioFinal.Catalogo_peliculas.servicio.catalogo_peliculas import CatalogoPeliculas as cp

salir = False
catalogo = cp()


while not salir:
    try:
        print(f'Bienvenido al catologo de peliculas!')
        menu = (f'\n1) Agrega Peliculas\n'
                f'2) Listar Peliculas\n'
                f'3) Eliminar archivo de Peliculas\n'
                f'4) Salir')
        print(menu)
        opcion = int(input('\nIntroduce la opcion que deseas (1-4): '))
        if opcion == 1:
            nombre_pelicula = input('Introduce el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
            print()
        elif opcion == 2:
            cp.listar_peliculas()
            print()
        elif opcion == 3:
            cp.eliminar_lista_peliculas()
            print()
        elif opcion == 4:
            salir = True
        else:
            print(f'\nEsta opcion no esta disponible, elija otra opcion!')
    except Exception as error:
        print(f'Ha ocurrido un error al ejecutar el programa: {error}')

else:
    print(f'Has salido del sistema con exito!')