"""Una funcion anidada es definir una funcion dentro de otra funcion"""

# Funciones anidadas

def calculadora(a,b, operacion='sumar'):
    # 1. Definir Funcion anidada
    def sumar(a,b):
        return a+b

    def restar(a,b):
        return a-b

    # 2. Llamamos a la funcion anidada (Sino la llamamos no se va a ejecutar nunca)
    if operacion == 'sumar':
         print(f'El resultado de sumar: {sumar(a,b)}')
    elif operacion == 'restar':
        print(f'El resultado de restar: {restar(a,b)}')

calculadora(5,6)
calculadora(4,3,operacion=input('Introduce la operacion que deseas realizar: ')) # Cambiamos el valor por default de operacion y le damos el valor de restar para que llame la funcion restar
