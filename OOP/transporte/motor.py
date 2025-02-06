class Motor:
    def __init__(self, tipo_motor):
        self.motor = tipo_motor

    def __str__(self):
        return f'El tipo de motor es: {self.motor}'