from Clases_y_Objetos.Tienda_instrumentos.instrumento import Instrumento


class Ventas:

    contador_ventas = 0

    def __init__(self):
        Ventas.contador_ventas += 1
        self.id_venta = Ventas.contador_ventas
        self.instrumento = []

    def agregar_instrumento(self, *args):
        for instrumento in args:
            self.instrumento.append(instrumento)

    def __str__(self):
        instrumento_str = ''
        for instrumento in self.instrumento:
            instrumento_str += '\n' + instrumento.__str__()
        return instrumento_str

if __name__ == '__main__':
    instrumento1 = Instrumento("Guitarra", "Fender", 1000)
    instrumento2 = Instrumento("Bateria", "Yamaha", 2000)
    venta1 = Ventas()
    venta1.agregar_instrumento(instrumento1, instrumento2)
    print(venta1)