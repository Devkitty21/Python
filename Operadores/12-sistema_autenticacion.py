print('*** Sistema de Autenticacion ***')

# Definimos las constantes
USUARIO_VALIDO = "admin" # No se deben de cambiar estos valores
PASSWORD_VALIDO = "123"

# Definimos los inputs y las variables

usuario = input('Cual es tu usuario? ')
password = input('Cual es tu contrasena? ')

# Definimos la condicion

son_datos_correctos = USUARIO_VALIDO == usuario.strip() and PASSWORD_VALIDO == password.strip()

# Imprimos los valores en pantalla
print(f'Datos correctos? {son_datos_correctos}')