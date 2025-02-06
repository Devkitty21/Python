print('*** Sistema de descuentos vip ***')

NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input('Cuantos productos compraste hoy? '))
tienes_membresia = input('Tienes membresia de la tienda? (Si/No) ')

es_elegible_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO and
                         tienes_membresia.strip().lower() == 'si')

print(f'Tienes acceso al descuento vip? {es_elegible_descuento}')

# print('*** Sistema de entradas gratis ***') Prueba hecha por mi mismo
# FAMILIARES = 4
# cantidad_tickets = int(input('Cuantos tickets has comprado? '))
# familia_numerosa = input('Eres familia numerosa? (Si/No) ')
#
# entrada_gratis = (cantidad_tickets >= FAMILIARES
#                   and familia_numerosa.strip().lower() == 'si')
#
# print(f'Tienes acceso a las entradas gratis? {entrada_gratis}')
