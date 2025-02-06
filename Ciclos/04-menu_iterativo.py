print('*** Sistema de administracion de cuentas ***')

salir = False

while not salir:
    print(f"""Menu:
    1. Crear Cuenta
    2. Eliminar Cuenta
    3. Salir
""")
    opcion = int(input("Elije una opcion: "))
    if opcion == 1:
        print('Creando tu cuenta...\n')
    elif opcion == 2:
        print('Eliminando tu cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema... Hasta pronto!\n')
        salir = True
    else:
        print('La opcion no es valida! Vuelve a elegir una opcion valida!\n ')
else:
    print("Terminando el sistema de administracion de cuentas")