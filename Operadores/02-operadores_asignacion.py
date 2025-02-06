print('*** Operadores de asignacion ***')
numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Valor de numero: {numero}')
cadena = 'Saludos desde Python'
print(f'Valor de la cadena: {cadena}')

# Asignacion multiple
x, y, z = 5, "Hola", -9.15
print(f"Valor de x = {x}, y = {y}, z = {z}")

# Asignacion encadenada
a = b = c = 10
print(f'Valor a = {a}, b = {b}, c = {c}')

# Intecambio de valores de una variable sin utilizar variables temporales
x, y  = 5,10
print(f'Valores iniciales de x = {x}, y = {y}')
# Aplicando el concepto de asignacion multiple intercambiamos valores
x, y = y, x
print(f'Invertir los valores de x = {x}, y = {y} ')

# Recibir multiples valores de la entrada del usuario
nombre, apellido = input("Introduce tu nombre y apellido separa los valores por coma: ").split(",") # Si no separamos usando el metodo split, solo estaremos dando un valor a las variables nombre y apellido y nos dara un error de tipo ValueError
print(f'Nombre = {nombre.strip()}, apellido = {apellido.strip()}')