class Vehiculo:

    def __init__(self,tipo_vehiculo):
        self.vehiculo = tipo_vehiculo

    def __str__(self):
        return f'El tipo de vehiculo es: {self.vehiculo}'

