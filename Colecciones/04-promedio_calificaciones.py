print('*** Promedio de Calificaciones ***')

calificaciones = []
numero_calificaciones = int(input('Proporciona el numero de calificaciones a evaluar: '))

# Hacemos la iteracion de calificaciones

for calificacion in range(numero_calificaciones):
    nota = float(input(f'Calificacion[{calificacion + 1}]: '))
    calificaciones.append(nota)


print('\n')
print(f'Las calificaciones proporcionadas son: {calificaciones}')

# Suma de todos los valores
# sum()
suma = sum(calificaciones)

# suma = 0
# for nota in calificaciones:
#     suma += nota


print(f'\nPromedio de las calificaciones: {suma/numero_calificaciones:.2f}')


