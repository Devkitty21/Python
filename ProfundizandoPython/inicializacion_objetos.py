# Orden de inicializacion de objetos

class Padre:
    def __init__(self):
        print('Inicializador Padre')

    def metodo(self):
        print('Metodo Padre')

class Hijo(Padre):

    # Se manda a llamar el metod __init__ de la clase padre
    # siempre y cuando la clase hija no definna su propio metodo init

#     Definimos el metodo init
    def __init__(self):
        # De manera opcional podemos llamar al metodo __init__ de la clase padre (super)
        print('Inicializando hijo')
        super().__init__() # Con el metodo super podemos mandar a llamar al inicializador padre

#     Sobreescribimos el metodo heredado de la clase padre
    def metodo(self):
        print('Metodo sobreescrito hijo')
        super().metodo()

# padre1 = Padre()
# padre1.metodo()
hijo = Hijo()


