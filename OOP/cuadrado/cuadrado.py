from OOP.cuadrado.FiguraGeometrica import FiguraGeometrica
from OOP.cuadrado.color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self,alto, ancho)
        Color.__init__(self,color)


    @property
    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'El area de el cuadrado es: {self.calcular_area} y su color es: {self._color}'

