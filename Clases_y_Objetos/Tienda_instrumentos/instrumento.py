class Instrumento:
    contador_instrumento = 0

    def __init__(self, nombre, marca, precio):
        Instrumento.contador_instrumento += 1
        self.id_instrumento = Instrumento.contador_instrumento
        self.nombre = nombre
        self.marca = marca
        self.precio = precio

    def __str__(self):
        return f"""
{self.nombre} : ID {self.id_instrumento}
Marca: {self.marca}
Precio: {self.precio}"""

# Codigo principal

if __name__ == '__main__':
    instrumento1 = Instrumento("Guitarra", "Fender", 1000)
    instrumento2 = Instrumento("Bateria", "Yamaha", 2000)
    print(instrumento1,'\n', instrumento2)