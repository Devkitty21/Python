# 2. Nuevo Estilo de formato de cadenas en Python

nombre = 'Juan'
mi_cadena = 'Hola, {}'.format(nombre) # El valor de la variable se sustituye donde encuentre las {}
print(mi_cadena)

# Podemos convertir enteros a hexadecimales
error = 500
cadena_hexadecimal = 'Error en hexadecimal: {error:x}'.format(error=error) # Despues de : se pone el tipo de dato que queremos convertir
print(cadena_hexadecimal)
# Ejemplo entero a flotante
entero = 50
cadena_flotante = 'Numero flotante: {entero:.2f}'.format(entero=entero) # Convertimos el valor a flotante y le damos un formato
print(cadena_flotante)

# Podemos hacer lo mismo, pero de manera simplificada usando String Interpolation (f-string literal)
mi_cadena = f'Hola, {nombre}'
# print(mi_cadena)
# Mandar a imprimir directamente
print(f'Hola, {nombre}')
# Este es el mismo ejemlo de hexadecimal con String Interpolation
print(f'Error en hexadecimal: {error:x}') # Se usa ":" seguido del tipo de conversión, en este caso "x" para hexadecimal
# El mismo ejemplo de impresion de entero a flotante
print(f'Numero flotante: {entero:.2f}')  # ":.2f" formatea el número como flotante con 2 decimales
# Podemos incluir expresiones o llamadas a funciones
a = 10
b = 3
print(f'Dividimos y damos formato: {a/b:.2f}')