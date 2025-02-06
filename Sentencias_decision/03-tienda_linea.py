print('*** Tienda en Linea ***')

# Definimos las constantes
MONTO_MINIMO = 1000 # No se debe de modificar este valor

monto_comprado = float(input('Cuanto monto has comprado hoy? '))
eres_miembro = input('Eres miembro de la tienda? (Si/No) ')

# Definimos los descuentos
descuento1 = 10
descuento2 = 5

# Descuento del 10% aplicado

descuento_aplicado = monto_comprado * (descuento1/100)

# descuento del 5% aplicado

descuento_aplicado2 = monto_comprado * (descuento2/100)


if monto_comprado >= MONTO_MINIMO and eres_miembro.strip().lower() == 'si':
    print(f'\nFelicidades, Has obtenido un descuento del {descuento1}%')
    print(f'Monto de la compra: ${monto_comprado:.2f}')
    print(f'Monto del descuento: ${descuento_aplicado:.2f}')
    print(f'Monto de la compra con descuento: ${monto_comprado - descuento_aplicado:.2f}')

elif eres_miembro.strip().lower() == "si":
    print(f'Felicidades, Has obtenido un descuento del {descuento2}%')
    print(f'Monto de la compra: ${monto_comprado:.2f}')
    print(f'Monto del descuento ${descuento_aplicado2:.2f}')
    print(f'Monto de la compra con descuento: ${monto_comprado - descuento_aplicado2:.2f}')
else:
    print("No has obtenido ningun descuento")
    print("Te invitamos a hacerte miembro de la tienda")
    print(f'Monto final de la compra: {monto_comprado}')
