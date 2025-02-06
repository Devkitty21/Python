class Libro:
    contador_libros = 0

    def __init__(self, titulo, autor, genero):
        Libro.contador_libros += 1
        self.id_libro = Libro.contador_libros
        self.titulo = titulo
        self.autor = autor
        self.genero = genero

    def __str__(self):
        return f'ID: {self.id_libro}, Titulo: {self.titulo}, Autor: {self.autor}, Genero: {self.genero}'

