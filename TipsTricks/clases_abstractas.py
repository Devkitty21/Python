# ABC - Abstract Base Class
# Nos permite asegurar que las clases que heredan implementen los metodos
from abc import ABCMeta, abstractmethod


# Ej. Sin usar ABC y los posibles problemas
class ClaseBase1:
    def metodo1(self):
        raise NotImplementedError('No hemos implementado el metodo')

    def metodo2(self):
        raise NotImplementedError('No hemos implementado el metodo')

class ClaseConcreta1(ClaseBase1):
    # Implementacion de la clase padre
    def metodo1(self):
        print('Metodo 1 implementado....')

    # El metodo 2 no se va a implementar
    # Esto ya es un problema por que no se reporta la falta de implementacion

# Hay un problema, se puede isntanciar la clase Base
clase_base = ClaseBase1()
# clase_base.metodo1() # Esto podia ser un comportamiento no deseado

# Esto funciona segun lo esperado
clase_concreta = ClaseConcreta1()
# clase_concreta.metodo1()
# El metodo2, se llama heredado
# clase_concreta.metodo2()

# Vamos a resolver los detalles anteriores usando ABC (Abstract Base Class)

class ClaseBase2(metaclass=ABCMeta):
    # No tenemso que agregar la implementacion al ser un metodo abstracto
    @abstractmethod
    def metodo_1(self):
        pass

    @abstractmethod
    def metodo_2(self):
        pass

class ClaseConcreta2(ClaseBase2):
    def metodo_1(self):
        print('Metodo 1 implementado...')

    # Dejamos sin implementar el metodo_2
    # Estamos obligados a implementar todos los metodos abstractos
    def metodo_2(self):
        print('Metodo 2 implementado...')


# Intentamos crear un objeto de la clase base
# Esto no es posible
# clase_base = ClaseBase2() # En el ejemplo anterior si que podiamos crear una instancia de la ClaseBase1

# Instanciamos la clase concreta 2
clase_concreta = ClaseConcreta2() # Sino agregamos todos los metodos abstractos dara un error
clase_concreta.metodo_1()
clase_concreta.metodo_2()

# ABC permite escribir una jerarquia de clases mas robustas y escribir codigo tambien mas mantenible