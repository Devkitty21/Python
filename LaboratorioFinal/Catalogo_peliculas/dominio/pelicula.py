class Pelicula:

    def __init__(self, nombre : str):
        self._nombre = nombre # Atributo protegido

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre


    def __str__(self):
        return f'La pelicula es: {self.nombre}'

# Todo correcto, funciona perfectamente