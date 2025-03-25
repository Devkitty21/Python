# Dunder significa = Double underscore
# A Estos tipos de metodos tambien se le llaman metodos Magicos


class Padre:
    def __init__(self):
        # Al usar dunder (double underscore) al incio y al final,
        # No se aplica el concepto de name mangling
        self.__variable__dunder =  10
        self.__variable_dunder__ = 15

if __name__ == '__main__': # __name__ y __main__ son variables de tipo Dunder
    padre = Padre()
    print(dir(padre))
    print(f'Accediendo a la variable privada: {padre._Padre__variable__dunder}')
    print(f'Accediendo a la variable dunder: {padre.__variable_dunder__}')