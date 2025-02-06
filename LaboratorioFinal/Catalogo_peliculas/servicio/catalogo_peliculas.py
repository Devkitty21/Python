import os
from LaboratorioFinal.Catalogo_peliculas.dominio.pelicula import Pelicula

class CatalogoPeliculas:

    ruta_archivo = 'c:\\Users\\vieir\\PycharmProjects\\PythonProject\\LaboratorioFinal\\Catalogo_peliculas\\Pelicula.txt'

    @classmethod
    def agregar_pelicula(cls, peliculas):
         with open(cls.ruta_archivo, 'a+', encoding='utf8') as pelicula:
            pelicula.write(f'-- {peliculas.nombre}\n')
            print(f'La pelicula \'{peliculas.nombre}\' se ha agregado perfectamente!')

    @classmethod
    def listar_peliculas(cls):
        print(f'Aqui tienes toda la lista de peliculas actuales:\n'.center(50,'-'))
        with open(cls.ruta_archivo, 'r') as archivo_pelicula:
            contenido = archivo_pelicula.read()
            print(contenido)


    @classmethod
    def eliminar_lista_peliculas(cls):
        print(f'Eliminando la lista con las peliculas...\n')
        os.remove(cls.ruta_archivo)
        print(f'Lista eliminada con exito! {cls.ruta_archivo}')


