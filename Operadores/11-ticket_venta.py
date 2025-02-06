print('*** Generacion Ticket de venta ***')

precio_leche = float(input('Introduce el precio de la leche: '))
precio_pan = float(input('Introduce el precio del pan: '))
precio_lechuga = float(input('Introduce el precio de la lechuga: '))
precio_platanos = float(input('Introduce el precio de los platanos: '))
descuento_porcentaje = int(input('Deseas aplicar algun descuento (%)? '))


# Calculo del subtotal (sin impuestos)

subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

# Calculo con los impuestos (16%)

impuesto = subtotal * 0.16

# Descuento
descuento = subtotal * (descuento_porcentaje/100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Calculo total de la compra (con impuestos)
precio_total_compra = subtotal_con_descuento + impuesto


print(f""""
Subtotal: ${subtotal:.2f}
Subtotal con descuento: {subtotal_con_descuento:.2f}
Impuesto (16%): {impuesto:.2f}
Descuento (%): {descuento} {descuento_porcentaje}%
Precio total de la compra: ${precio_total_compra:.2f}
""")