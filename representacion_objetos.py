# Representacion de objetos (__str__, __repr__, __format__) son funciones dunder
# print(dir(object)) # Asi podemos saber que metodos tenemos disponibles en object

class Persona:
    def __init__(self, nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    # repr, mas enfocado a los programadores (Informacion para los programadores y mas enfocado al codigo)
    def __repr__(self):
        return f'{self.__class__.__name__}(nombre={self.nombre}, apellido={self.apellido})'


    # __str__ es mas para el usuario final u otros sistemas
    # la implementacion por default llama a el metodo __repr
    def __str__(self):
        return f'{self.__class__.__name__}: {self.nombre} {self.apellido}'

    # __format__ su implementacion por default es el metodo __str__ y se manda a llamar
    # al usar un f-string (Es un poco mas detallado y mas extenso)
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}'


persona1 = Persona('Juan','Perez')
# repr (!r)
print(f'Mi objeto persona1: {persona1!r}') # De esta forma nos aseguramos de que se llama al metodo repr y no llama a
# a otro metodo como str

# str
print(persona1) # El metodo print por default manda a llamar el metodo __str__

# format
print(f'{persona1}')
