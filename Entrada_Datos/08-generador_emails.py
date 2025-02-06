print("*** Sistema Generador de Emails ***")

#Definimos las variables y inputs

nombre = input('Introduce tu nombre: ')
apellido = input('Introduce tu apellido: ')
nombre_empresa = input('Introduce el nombre de la empresa: ')
extension_dominio = input('Introduce la extension del dominio: ')

# Normalizacion de las variables

nombre_modificado = nombre.strip().lower().replace(" ",".")
apellido_modificado = apellido.strip().lower().replace(" ",".")
nombre_empresa_modificado = nombre_empresa.strip().lower().replace(" ","")
extension_dominio = extension_dominio.strip().lower().replace(" ","")
# Email completo

email = f'{nombre_modificado}.{apellido_modificado}@{nombre_empresa_modificado}{extension_dominio}'

# Imprimos los valores

print(f'\nNombre: {nombre}')
print(f'Apellido: {apellido}')
print(f'Nombre de la empresa: {nombre_empresa}')
print(f'Extension dominio: {extension_dominio}')
print(f'\nEl email completo es:\n{email}')