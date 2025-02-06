print('*** Sistema de Inventarios ***')

productos_disponibles = []

cantidad_productos = int(input('Introduce la cantidad de productos que quieras: '))

for indice in range(cantidad_productos):
    print(f'Proporciona los valores del producto {indice +1}')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    producto = {"id":indice,"nombre":nombre,"precio":precio,"cantidad":cantidad}
    productos_disponibles.append(producto)


print(f'\nInventario incial: {productos_disponibles}')

# Buscar producto id
id_buscar = int(input('\nIngresa ID del producto a buscar: '))
producto_encontrado = None
for producto in productos_disponibles:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print('Informacion del producto encontrado')
    print(f"""ID: {producto_encontrado.get('id')}
nombre: {producto_encontrado.get('nombre')}
Precio {producto_encontrado.get('precio')}
Cantidad {producto_encontrado.get('cantidad')}
""")
else:
    print(f'Producto con ID {id_buscar} no encontrado!')

# Mostrar el inventario detallado
for producto in productos_disponibles:
    print(f"""ID: {producto.get('id')}
nombre: {producto.get('nombre')}
Precio {producto.get('precio')}
Cantidad {producto.get('cantidad')}""")