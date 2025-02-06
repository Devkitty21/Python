print('*** Creacion de Password ***')

password = input('Crea una contraseña: ')

# Validacion de la contraseña
while len(password) < 6:
    print('La contraseña debe tener almenos 6 caracteres\n')
    password = input('Crea una contraseña: ')
else:
    print(f'\nLa contraseña: \'{password}\' es valida.')




