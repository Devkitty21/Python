# Distintas formas de dar formato a cadenas en Python
# 1. Estilo Antiguo
nombre = 'Juan'
mi_cadena = 'Hola, %s' % nombre # % -> Para remplazar un valor 's' -> Indicar el tipo de valor (string)
print(mi_cadena)

# Podemos convertir enteros a hexadecimales
error = 500
cadena_hexadecimal = 'Error en hexadecimal: %x' % error
print(cadena_hexadecimal)

# Si queremos pasar varios valores, tenemos que usar una tupla
cadena = 'Hola %s hay un error: %x' % (nombre,error)
print(cadena)

# Podemos referenciar por sustitucion de variables usando un diccionario
cadena = 'Hola %(nombre)s hay un error: %(error)x' % {'nombre':nombre,'error':error}
print(cadena)

float = 14.5
cadena = 'El 14.5 redondeado es: %i' % float # Usamos I para referirnos a un valor de tipo int
print(cadena)


