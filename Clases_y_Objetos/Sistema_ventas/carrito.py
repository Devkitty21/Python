from Clases_y_Objetos.Sistema_ventas.producto import Producto

class Carrito:
    contador_carrito = 0

    def __init__(self, productos):
        Carrito.contador_carrito += 1
        self.id_carrito = Carrito.contador_carrito
        self.productos = productos

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def __str__(self):
        productos_str = ''
        for producto in self.productos:
            productos_str += '\n' + producto.__str__()
        return f'Carrito ID: {self.id_carrito}, Productos: {productos_str}'



if __name__ == '__main__':
    producto1 = [Producto('Camisa', 100.00)]
    producto2 = [Producto('Pantalon', 150.00)]
    producto3 = [Producto('Calcetines', 50.00)]
    producto4 = [Producto('Camiseta', 20.00)]
    carrito1 = Carrito(producto1 + producto2)
    print(carrito1)