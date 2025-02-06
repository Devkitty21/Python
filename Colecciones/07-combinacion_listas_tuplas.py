from idlelib.outwin import file_line_progs

print('*** Combinacion de Listas y Tuplas ***')

# Definir una lista que almacena tuplas de productos

productos = [
    ("P001","Camiseta", 20.0),
    ("P002","Jeans",30.0),
    ("P003", "Sudadera", 40.0)
             ]

# Imprimir la informacion de cada producto
# y ademas calculamos el precio total

precio_total = 0

print(f'Informacion de los productos: ')
for producto in productos:
    # print(producto)
    id,descripcion,precio = producto #unpacking
    print(f'Producto: id = {id}, descripcion = {descripcion}, precio = ${precio}')
    precio_total += precio #producto[2]

print(f'\nEl precio total de los productos es: ${precio_total}')
