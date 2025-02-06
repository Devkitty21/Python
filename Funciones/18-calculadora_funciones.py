print(f'*** Calculadora con Funciones ***')

salir_programa = False

def suma(valor1,valor2):
    print(f'\nLa suma es: {valor1 + valor2:.2f}')

def resta(valor1,valor2):
    print(f'\nLa resta es: {valor1 - valor2:.2f}')

def multiplicacion(valor1,valor2):
    print(f'\nLa multiplicacion es: {valor1 * valor2:.2f}')

def division(valor1,valor2):
    print(f'\nLa division es: {valor1 / valor2:.2f}')

def salir():
    global salir_programa
    salir_programa = True
    print(f'\nSaliendo de la calculadora... Hasta pronto!')

if __name__ == "__main__":
    while not salir_programa:
        print("""\n--- Menu ---\n
1. Suma
2. Resta
3. Multplicacion
4. Division
5. Salir""")
        opcion = int(input('\nIntroduce la operacion que deses: '))
        if opcion == 1:
            valor1 = float(input('Introduce el valor 1: '))
            valor2 = float(input('Introduce el valor 2: '))
            suma(valor1,valor2)
        elif opcion == 2:
            valor1 = float(input('Introduce el valor 1: '))
            valor2 = float(input('Introduce el valor 2: '))
            resta(valor1,valor2)
        elif opcion == 3:
            valor1 = float(input('Introduce el valor 1: '))
            valor2 = float(input('Introduce el valor 2: '))
            multiplicacion(valor1,valor2)
        elif opcion == 4:
            valor1 = float(input('Introduce el valor 1: '))
            valor2 = float(input('Introduce el valor 2: '))
            division(valor1,valor2)
        elif opcion == 5:
            salir()
        else:
            print(f'La operacion que has introducido no es correcta...')