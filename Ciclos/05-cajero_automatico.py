print('*** Aplicacion de Cajero Automatico')
saldo_actual = 1000.00
salir = False
saldo_retirar = 0
saldo_depositar = 0
no_poder_retirar = None

while not salir:
    print(f"""Operaciones a realizar:
    1. Consultar saldo
    2. Retirar saldo
    3. Depositar
    4. Salir
""")
    opcion = int(input('Escoje una opcion: '))
    if opcion == 1:
        print(f'Tu saldo actual es de: ${saldo_actual:.2f}\n')
    elif opcion == 2:
        saldo_retirar = float(input('Ingresa cuanto quieres retirar: $ '))
        if not saldo_retirar < saldo_actual:
            print(f'Lo siento, No puedes retirar esta cantidad. Tu saldo actual es: ${saldo_actual:.2f}\n')
        else:
            saldo_actual -= saldo_retirar
            print(f'Tu nuevo saldo es: {saldo_actual:.2f}\n')
    elif opcion == 3:
        saldo_depositar = float(input(f'Ingresa cuanto quieres depositar: $ '))
        saldo_actual += saldo_depositar
        print(f'Tu nuevo saldo es: ${saldo_actual:.2f}\n')
    elif opcion == 4:
        print('Saliendo del sistema... Hasta pronto!')
        salir = True
    else:
        print("La opcion que has elegido no es valida, porfavor introduce una opcion valida\n")
else:
    print('Terminando la aplicacion del cajero automatico...')