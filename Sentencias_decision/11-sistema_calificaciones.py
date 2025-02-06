print('*** Sistema de Calificaciones ***')

calificacion_numerica = float(input('Introduce una calificacion del 1 al 10: '))
calificacion_letra = None

if 9 <= calificacion_numerica <= 10:
    calificacion_letra = "A"
elif 8 <= calificacion_numerica <= 9:
    calificacion_letra = "B"
elif 7 <= calificacion_numerica <= 8:
    calificacion_letra = "C"
elif 6 <= calificacion_numerica <= 7:
    calificacion_letra = "D"
elif 0 <= calificacion_numerica <= 6:
    calificacion_letra = "F"
else:
    print('Este valor es desconocido')

# Imprimos los valores

print(f'Calificacion {calificacion_numerica} equivalente a: {calificacion_letra}')
