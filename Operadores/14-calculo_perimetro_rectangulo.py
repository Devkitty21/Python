print('*** Calculo de area y perimetro de un rectangulo ***')

base_rectangulo = float(input('Introduce cual es la base del rectangulo: '))
altura_rectangulo = float(input('Introduce cual es la altura del rectangulo: '))

# Realizamos los calculos
area = base_rectangulo * altura_rectangulo
perimetro = 2 * (base_rectangulo + altura_rectangulo) # Hemos aplicado la preferencia de operadores usando ()

# Imprimimos en pantalla
print(f'El area del rectangulo es: {area:.2f}\nEl perimetro es: {perimetro:.2f}')