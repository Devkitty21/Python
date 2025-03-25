# Con el metodo unpacking podemos desempaquetar cualquier iterable

def imprimir_vector(x,y,z):
    print(f'<{x}, {y}, {z}>')

imprimir_vector(10,3,12)

# Desempaquetar un iterable (tupla, list, set...)
tupla_vector = (8,2,15)
imprimir_vector(*tupla_vector) # Aplicamos Unpacking a una tupla para que 8 se agrege a X 2 -> Y, 15 -> z

lista_vector = [4,2,7]
imprimir_vector(*lista_vector) # Aplicamos unpacking a una lista

# Desempaquetando una expresion generadora
expresion_generador = (x * x for x in range(3))
imprimir_vector(*expresion_generador)

# Desempaqeutar un diccionario
diccionario_vector = {
    'x':10,
    'y':15,
    'z':3
}
imprimir_vector(**diccionario_vector) # Al ser un diccionario tenemos que aplicar **kwargs ya que esto nos da argumentos en forma de diccioanrios
# Se pasan los valores no las llaves

# En el caso de que quisieramos pasar las llaves solo ponemos un *
imprimir_vector(*diccionario_vector)
