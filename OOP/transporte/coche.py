from OOP.transporte.vehiculo import Vehiculo
from OOP.transporte.motor import Motor

class Coche(Vehiculo, Motor):
    def __init__(self,tipo_vehiculo,tipo_motor):
        Vehiculo.__init__(self,tipo_vehiculo)
        Motor.__init__(self,tipo_motor)

    def __str__(self):
        return f"El tipo de vehiculo es: {self.vehiculo} y el tipo de motor es: {self.motor}"



coche = Coche('Coche','Gasolina')
print(coche)
