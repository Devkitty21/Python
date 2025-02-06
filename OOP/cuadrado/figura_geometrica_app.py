from cuadrado import Cuadrado
from rectangulo import Rectangulo
from FiguraGeometrica import FiguraGeometrica
from color import Color
print('*** Sistema de Figuras Geometricas ***')

# # No se puede instanciar una clase abstracta
# figura = FiguraGeometrica(12,12)

# Definimos un cuadrado
print(f'Creacion Objeto Cuadrado'.center(50,'-'))
cuadrado = Cuadrado(ancho=4, alto=6, color='Rojo')
print(cuadrado)
# Imprimos los valores con el metodo get creado
print(f'Color: {cuadrado.get_color}')

# Modificamos el cuadrado
cuadrado.set_alto = 4
cuadrado.set_ancho = 4
print(cuadrado)
print(f'Color: {cuadrado.get_color}')
print('\n')

# Creamos un objeto rectangulo
print(f'Creacion Objeto Rectangulo'.center(50,'-'))
rectangulo = Rectangulo(ancho=4,alto=5,color='Verde')
print("Rectangulo:")
print(f'El area del rectangulo es: {rectangulo.calcular_area} y su color es: {rectangulo.get_color}')
print(rectangulo)

# Method Resolution Order
print(Cuadrado.mro())