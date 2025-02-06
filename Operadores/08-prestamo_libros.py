print('*** Sistema de Prestamo de Libros ***')
DISTANCIA_PERMITIDA_KM = 3
tienes_credencial = input('Tienes credencial de estudiante? Si/No ')
distancia_biblioteca_km = int(input('A cuantos km vives de la biblioteca? '))

es_elegible_prestamo = (distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM
                  or tienes_credencial.strip().lower() == "si")

print(f'Eres elegible para el prestamo de libros? {es_elegible_prestamo}')