class Cliente:
    def __init__(self,id=None,nombre=None,apellido=None,membresia=None):
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia
        self.id = id

    def __str__(self):
        return f'Cliente = ID: {self.id} Nombre: {self.nombre}, Apellido: {self.apellido}, Membresia: {self.membresia}'
