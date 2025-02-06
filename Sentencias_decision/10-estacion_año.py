print('*** Identificador de la Estacion del año')

mes = int(input('Introduce un numero del 1 al 12: '))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = "Invierno"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Verano"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otono'
else:
    print('Estacion desconocida')

# Imprimir el resultado
print(f'La estacion en el mes {mes} es {estacion}')