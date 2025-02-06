print('*** Bienvenidos al Sistema Bancario ***')

salir = input('Deseas salir del sistema? (Si/No) ')

if not salir.strip().lower() == "si":
    print('Continuamos dentro del sistema...')
else:
    print('Saliendo del sistema....')