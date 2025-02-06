from Clases_y_Objetos.Sistema_bibliotecas.libro import Libro

class Estanteria:
    contador_estanteria = 0

    def __init__(self,libros):
        Estanteria.contador_estanteria += 1
        self.id_estanteria = Estanteria.contador_estanteria
        self.libros = libros

    def __str__(self):
        libro_str = ''
        for libro in self.libros:
            libro_str += '\n' + libro.__str__()
        return libro_str

    def agregar_libro(self,capacidad, libro):
            self.libros.append(libro)

    def eliminar_libro(self, libro):
        self.libros.remove(libro)

if __name__ == '__main__':
    libro1 = Libro('El principito', 'Antoine de Saint-Exupéry', 'Infantil')
    libro2 = Libro('El señor de los anillos', 'J.R.R. Tolkien', 'Fantasía')
    estanteria1 = Estanteria([libro1, libro2])
    print(estanteria1)