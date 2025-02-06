from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, alto, ancho):
        if 0 < ancho < 10:
            self.ancho = ancho
        else:
            print('Valor erroneo, ancho no puede ser mayor a 10 ni menor a 0')
            self.ancho = 0

        if 0 < alto < 10:
            self.alto = alto
        else:
            self.alto = 0

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f'El valor de alto es: {self.alto} y el valor de ancho es: {self.ancho}'

    @property
    def get_alto(self):
        return self._alto

    @get_alto.setter
    def set_alto(self, alto):
        self._alto = alto

    @property
    def get_ancho(self):
        return self._ancho

    @get_ancho.setter
    def set_ancho(self, ancho):
        self._ancho = ancho