from cliente import Cliente
from cliente_dao import ClienteDAO
import sys

print(f'Made With Love by DevKitty'.center(30,'-'))
opcion = None

while opcion != 5:
    print(f"""\nBienvenido a la AppZonaFit""")
    print(f"""\n1. Listar clientes
2. Agregar cliente
3. Modificar cliente
4. Eliminar cliente
5. Salir""")
    opcion = int(input('\nQue operacion desea realizar? Elija [1-5] >> '))

    if opcion == 1: # Listar clientes
        clientes = ClienteDAO.seleccionar()
        print(f'\n*** Listado de clientes ***')
        for cliente in clientes:
            print(cliente)
        print("\n")
    elif opcion == 2: # Insertar cliente
        nombre = input('Introduce el nombre del cliente: ')
        apellido = input('Introduce el apellido del cliente: ')
        membresia = int(input('Introduce la membresia: '))
        cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes insertados: {clientes_insertados}\n')
    elif opcion == 3: # Modificar cliente
        id = int(input('Introduce el id del cliente a modificar: '))
        nombre = input('Nuevo nombre para el cliente: ')
        apellido = input('Nuevo apellido para el cliente: ')
        membresia = int(input('Nueva membresia: '))
        cliente = Cliente(nombre=nombre, apellido=apellido, membresia=membresia, id=id)
        clientes_actualizado = ClienteDAO.actualizar(cliente)
        print(f'Clientes actualizados: {clientes_actualizado}\n')
    elif opcion == 4: # Eliminar cliente
        id = int(input('Introduce el id del cliente que deseas eliminar: '))
        id_cliente = Cliente(id=id)
        cliente_eliminado = ClienteDAO.eliminar(id_cliente)
        print(f'Clientes eliminados: {cliente_eliminado}\n')

    else:
        print(f'Saliendo de la aplicacion... Hasta la proxima!')