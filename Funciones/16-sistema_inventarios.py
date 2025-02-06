print(f'*** Sistema de inventarios con funciones ***')

salir_programa = False
productos = [{
        "ID":"1",
        'Nombre': 'Camisa',
        'Precio': 25.99,
        'Cantidad': 50
    },
{
        "ID":"2",
        'Nombre': 'Pantalones',
        'Precio': 39.99,
        'Cantidad': 30
    },
{
        "ID":"3",
        'Nombre': 'Zapatos',
        'Precio': 49.99,
        'Cantidad': 20
    }
]

# Vamos a definir las funciones

def mostrar_inventario():
    print(f'\nInventario en el almacen:\n')
    for producto in productos:
        print(f'ID: {producto.get("ID")}, Nombre: {producto.get("Nombre")}, Precio: {producto.get("Precio")}, Cantidad: {producto.get("Cantidad")}')


def agregar_producto():
    print(f'\nRellene la informacion:\n')
    identificador = int(input('ID: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))

    nuevo_producto = {'ID': identificador, "Nombre": nombre, "Precio": precio, "Cantidad": cantidad}
    productos.append(nuevo_producto)

    # productos.append({
    #     'ID': identificador,
    #     'Nombre': nombre,
    #     'Precio': precio,
    #     'Cantidad': cantidad
    # })
    print('Producto agregardo al inventario!')


def buscar_producto():
    buscar = int(input('Introduce el id del producto que quieres buscar: '))
    producto_encontrado = None
    for producto in productos:
        if producto.get("ID") == buscar:
            producto_encontrado = producto
            break
    if producto_encontrado is not None:
        print(f'\nInformacion del producto:\n')
        print(f"""Nombre: {producto_encontrado.get('Nombre')}
Precio: {producto_encontrado.get('Precio')}
Cantidad: {producto_encontrado.get('Cantidad')}""")
    else:
        print(f'Producto no encontrado! Vuelva a introducir un ID valido')

def salir():
    global salir_programa
    salir_programa = True
    print('\nSaliendo del sistema de inventarios...')


def menu():
    while not salir_programa:
        print(f'\n---- Menu ----\n')
        print(f'''1. Mostrar inventario
2. Agregar nuevo producto
3. Buscar producto por ID
4. Salir''')
        opcion = int(input('\nIntroduce la opcion que deses (1-4): '))
        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            buscar_producto()
        elif opcion == 4:
            salir()
        else:
            print(f'El numero {opcion}, no es una opcion! Introduce una opcion valida!')



menu()
