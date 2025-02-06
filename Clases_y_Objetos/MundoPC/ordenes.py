from Clases_y_Objetos.MundoPC.computadora import Computadora

class Ordenes:
    contador_ordenes = 0

    def __init__(self,computadoras):
        Ordenes.contador_ordenes += 1
        self.id_orden = Ordenes.contador_ordenes
        self.computadoras = computadoras

    def agregar_computadora(self, *args):
        for computador in args:
            self.computadoras.append(computador)

    def __str__(self):
        computadoras_str = ''
        for computadora in self.computadoras:
            computadoras_str += '\n' + computadora.__str__()
        return f'Orden: {self.id_orden}, Computadoras: {computadoras_str}'

if __name__ == '__main__':
    computadora1 = Computadora('HP','Monitor HP','Teclado HP', 'Raton HP')
    computadora2 = Computadora('Acer','Monitor Acer','Teclado Acer', 'Raton Acer')
    computadora3 = Computadora('HP','Monitor HP','Teclado HP', 'Raton HP')
    orden1 = Ordenes([computadora1, computadora2, computadora3])
    print(orden1)

