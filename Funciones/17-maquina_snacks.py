
# 2. Comprar snacks (Que snack quieres comprar? (funciona con el ID) )
# 3. Mostrar tickets  (En una lista agregar productos_comprados  y luego sumar el total de todo lo que ha comprado)
# 4. Salir  (salir)

print(f'*** Maquina de snacks con funciones ')

snacks = [ # Lista que dentro tiene 3 diccionarios con los snacks disponibles
    {'ID': 1, 'Producto': 'Papas', 'Precio': 30},
    {'ID': 2, 'Producto': 'Refresco', 'Precio': 50},
    {'ID': 3, 'Producto': 'Sandwich', 'Precio': 120}
]

productos_comprados = []
salir_programa = False


def mostrar_snack():
    print(f'---- Snacks Disponibles ----')
    for snack in snacks:
        print(f'\tID: {snack.get("ID")} -> {snack.get("Producto")} - ${snack.get("Precio")}')


def comprar_snack():
    comprar_producto = int(input('Que snack quieres comprar? (ID) '))
    producto_comprado = None
    for snack in snacks:
        if snack.get('ID') == comprar_producto:
            producto_comprado = snack
            productos_comprados.append(producto_comprado)
            print(f'Snack agregado: {producto_comprado}')
            break
    else:
        print(f'\nSnack no encontrado con el id: {comprar_producto}')


def mostrar_ticket():
    total = 0
    print(f'\t--- Ticket de Venta ---')
    for producto in productos_comprados:
        print(f'\t- {producto.get("Producto")} - ${producto.get("Precio")}')
    for precio in productos_comprados:
        numeros = precio.get('Precio')
        total += numeros
    print(f'\tTOTAL -> {total}')

def salir():
    global salir_programa
    salir_programa = True
    print(f'\nSaliendo de la maquina de snacks...')
    print(f'\nHasta la proxima!')


def menu():
    while not salir_programa:
        print(f"""\n---- Menu ----\n
1. Mostrar snacks
2. Comprar snacks
3. Mostrar tickets
4. Salir""")
        opcion = int(input('\nIntroduce la opcion que deses: '))
        if opcion == 1:
            mostrar_snack()
        elif opcion == 2:
            comprar_snack()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            salir()
        else:
            print(f'La opcion que has introducido no es valida')

menu()