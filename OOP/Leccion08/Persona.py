class Personas:
    def __init__(self, nombre,edad, lista):
        self.nombre = nombre
        self.edad = edad
        self.lista = lista


    def __add__(self, other):
        return f'{self.nombre} {other.nombre} -> Esta es la concatenacion de el los objetos persona1 y persona2'

    def __sub__(self, other):
        return f'Esta es la resta de las edades: {self.edad - other.edad}'

    # def __add__(self,other):
    #     return f'Las dos listas juntadas son: {self.lista + other.lista}'


persona1 = Personas('Juan',28, [1,2,3,4])
persona2 = Personas('Roman',20, [6,7,8,9])
print(persona1 - persona2)
print(persona1 + persona2)

# obj1 + obj2
# obj1.__add__(obj2)

# obj1 - obj2
# obj1.__sub__(obj2)