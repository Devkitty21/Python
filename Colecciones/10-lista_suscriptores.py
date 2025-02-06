print('*** Lista de suscriptores ***')

# Definimos el set inicial
# suscriptores = {} # Aqui se define un diccionario vacio, no un set vacio
suscriptores  = set()

numeros_suscriptores = int(input('Proporciona el numero de suscriptores iniciales: '))
for _ in range(numeros_suscriptores):
    suscriptores.add(input('Nuevo suscriptor (email): '))

# suscriptores = {"luisa@mail.com","marcos@mail.com","elena@mail.com"}
print(f'Lista de suscriptores inicial: {suscriptores}')

nuevo_suscriptor = input('Proporciona el nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya esta en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado a la lista de suscriptores correctamente! {nuevo_suscriptor}')
    print(suscriptores)

# Eliminamos un suscriptor
suscriptor_eliminar = input('Introduce el correo que quieres eliminar: ')
if suscriptor_eliminar in suscriptores:
    suscriptores.remove(suscriptor_eliminar)
    print(f'El suscriptor se ha eliminado correctamente: {suscriptor_eliminar}')
    print(suscriptores)
else:
    print(f'El suscriptor no se ha podido eliminar, No existe en la lista de suscriptores!')

# Verificamos la cantidad total de suscriptores
print(f'Cantidad de suscriptores: {len(suscriptores)}')

# Mostramos todos los suscriptores
print(f'\n --------- Lista de suscriptores --------')
for suscriptor in suscriptores:
    print(f'-- {suscriptor}')