print('*** Sistema de Autenticacion ***')

# Constantes
USUARIO_VALIDO = 'admin'
PASSWORD_VALIDA = '123'

# Inputs

usuario = input('Introduce el usuario para iniciar sesion: ')
password = input('Introduce el usuario para iniciar sesion: ')

if usuario == USUARIO_VALIDO and password == PASSWORD_VALIDA:
    print(f'Bienvenido, {usuario} al sistema!')
elif usuario == USUARIO_VALIDO:
    print(f'La password no es correcta, favor de corregirla!')
elif password == PASSWORD_VALIDA:
    print('El usuario no es correcto, favor de corregirlo!')
else:
    print("El usuario y la password no son correctos, favor de corregirlo!")

