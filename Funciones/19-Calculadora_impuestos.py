print(f'*** Calculadora de impuestos ***')

# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto  * (impuesto/100)

def calculadora_impuesto(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Definimos los inputs
pago_sin_impuesto = float(input('\nIntroduce el pago sin impuesto: '))
impuesto = float(input('Introduce el monto del impuesto: '))

resultado = calculadora_impuesto(pago_sin_impuesto, impuesto)
print(f'\nPago con impuesto: ${resultado:.2f}')