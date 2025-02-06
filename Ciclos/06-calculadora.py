print('*** Calculadora en Python ***')

salir = False

while not salir:
    print("""Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir
    """)
    opcion = int(input('Escoje una opcion: '))
    numero1 = float(input('Ingresa el valor 1: '))
    numero2 = float(input('Ingresa el valor 2: '))
    if opcion == 1:
        numero1
        numero2
        suma = numero1 + numero2
        print(f'El resultado de la suma es: {suma:.2f}\n')
    elif opcion == 2:
        numero1
        numero2
        resta = numero1 - numero2
        print(f'El resultado de la resta es: {resta:.2f}\n')
    elif opcion == 3:
        numero1
        numero2
        multiplicacion = numero1 * numero2
        print(f'El resultado de la multiplicacion es: {multiplicacion:.2f}\n')
    elif opcion == 4:
        numero1
        numero2
        division = numero1 / numero2
        print(f'El resultado de la division es: {division:.2f}\n')
    elif opcion == 5:
        print('Saliendo de la aplicacion calculadora... Hasta pronto!')
        salir = True
    else:
        print('Opcion invalida. Porfavor elige una opcion valida!\n')

