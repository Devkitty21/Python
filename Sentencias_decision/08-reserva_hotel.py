print('*** Sistema de Reserva de Hotel')
print("\n-------- Tarifas Disponibles -------- ")
print('Cuarto sin vista al mar: $ 150.50 por dia')
print('Cuarto con vista al mar: $ 190.50 por dia')

nombre_cliente = input('\nIntroduce tu nombre: ')
dias_estadia = int(input('Introduce los dias de estadia en el hotel: '))
vista_al_mar = input('Quieres vistas al mar? (Si/No) ')


precio_mar_no = 150.50
precio_mar_si = 190.50

# Condiciones
precio_estadia = 0

if vista_al_mar.strip().lower() == 'si':
    precio_estadia = precio_mar_si * dias_estadia
else:
    precio_estadia = precio_mar_no * dias_estadia

print('\n -------- Detalles de la reservacion --------')
print(f'Cliente: {nombre_cliente}')
print(f'Dias de estadia: {dias_estadia}')
print(f'Precio: ${precio_estadia:.2f}')
print(f'Habitacion con vista al mar? {vista_al_mar}')