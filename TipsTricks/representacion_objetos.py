# __str__ su objetivo es que la informacion sea legible para el usuario
# __repr__ su objetivo es que la informacion no sea ambigua
# se utiliza para hacer debugging (formato tipo constructor)
# La implementacion por default del metodo str llama al metodo repr

class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color




# Por default solo se muestra el nombre de la clase y el id del objeto (direccion de memoria)
audi_a3 = Auto('Audi','A3','Rojo')
print(f'Audi: {audi_a3}')

class AutoStr:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f'str: Marca: {self.marca}, modelo: {self.modelo} y color: {self.color}'

    # def __repr__(self):
    #     return f'repr: Marca: {self.marca}, modelo: {self.modelo} y color: {self.color}'

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.marca!r}, {self.modelo}, {self.color})')

audi_a1 = AutoStr('Audi','A1','negro')
# Tenemos diferentes formas de imprimir el objeto:
print(audi_a1)
print(audi_a1.__str__())
print(str(audi_a1))
print('{}'.format(audi_a1))
print(f'{audi_a1}')

# Sin embargo es mas recomendable usar __repr__ en lugar de str (esto es porque el metodo __str__ por default llama al metodo
# Ej. Cualquier coleccion utiliza repr en lugar de str para mostrar la informacin
print([audi_a1])
# Tambien usando !r
print(f'{audi_a3!r}')

# Tambien manualmente podemos escoger que metodo usar
print(str(audi_a1))
print(repr(audi_a1))
