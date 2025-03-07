class Clase1:
    def __init__(self):
        print('Clase 1.__init__')

    def metodo(self):
        print('Metodo clase1')


class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')
        super().__init__()

    def metodo(self):
        print('Metodo clase2')
        super().metodo()

class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')
        super().__init__()

    def metodo(self):
        print('Metodo clase3')
        super().metodo()

class Clase4(Clase2,Clase3):
    def metodo(self):
        print(f'Metodo clase4')
        super().metodo()

# Creamos objeto clas4


clase4 = Clase4()
# __bases__
print(Clase4.__bases__)
# MRO
print(Clase4.mro())
# Cual metodo se ejecuta
clase4.metodo()



