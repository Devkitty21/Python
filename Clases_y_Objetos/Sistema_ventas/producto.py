class Producto:
    cantidad_productos = 0

    def __init__(self, nombre: str, precio:int):
        Producto.cantidad_productos += 1
        self.id_producto = Producto.cantidad_productos
        self._nombre = nombre
        self._precio = precio

    def __str__(self):
        return f'Producto: {self.id_producto}, Nombre: {self._nombre}, Precio: {self._precio}'

    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalon', 150.00)
    print(producto1)
    print(producto2)
