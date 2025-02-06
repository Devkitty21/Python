# Definimos la clase Coche
class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca # Atributo protegido
        self._modelo = modelo # Atributo protegido
        self._color = color # Atributo protegido

    def conducir(self):
        print(f"""Conduciendo el coche:
        Marca: {self._marca} 
        Modelo: {self._modelo}
        Color: {self._color}""")

    # def get_marca(self):
    #     return self._marca

    @property
    def marca(self): # Otra forma de definir el metodo get mas pythonica
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


# Programa pricinapl
if __name__ == '__main__':
# Creacion de un primer coche
    coche1 = Coche('Toyota','Yaris','Azul')
    print(f'\n')
    coche1.marca = 'Toyota 3'
    print(f'Atributo marca coche1: {coche1.marca}')
    coche1.modelo = 'Yaris 3'
    print(f'Atributo modelo coche1: {coche1.modelo}')
    coche1.color = 'Azul 3'
    print(f'Atributo color coche1: {coche1.color}')

    # Intentar agregar un nuevo atributo
    setattr(coche1, 'nuevo_atributo', 'Valor nuevo atributo') # Solo se agrega al objeto que le asignamos
    print(f'\n{coche1.nuevo_atributo}')
    print(f'Atributos del coche1: {coche1.__dict__}')
    # Segundo objeto
    coche2 = Coche('Chevrolet', 'Trax', 'Blanco')
    coche2.conducir()
    print(f'Atributos del coche2: {coche2.__dict__}')

