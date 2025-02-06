from Clases_y_Objetos.MundoPC.monitor import Monitor
from Clases_y_Objetos.MundoPC.teclado import Teclados
from Clases_y_Objetos.MundoPC.raton import Raton


class Computadora:
    contador_computadoras = 0

    def __init__(self,nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self. raton = raton

    def __str__(self):
        return f"""
        {self.nombre}: {self.id_computadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}"""

# Codigo principal

if __name__ == '__main__':
    teclado = Teclados("USB", "HP")
    raton1 = Raton("USB", "HP")
    monitor = Monitor("HP", 15)
    computadora1 = Computadora("HP", monitor, teclado, raton1)
    print(computadora1)

    teclado2 = Teclados("USB", "Acer")
    raton2 = Raton("USB", "Acer")
    monitor2 = Monitor("Acer", 27)
    computadora2 = Computadora("Acer", monitor2, teclado2, raton2)
    print(computadora2)