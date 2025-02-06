print('*** Aplicacion de Salud y Fitness ***')

# Definimos las constantes, estos valores no se deben de modificar
META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04 # Valor aproximado, son kilocalorias

nombre_usuario = input('Introduce tu nombre: ')
pasos_diarios = int(input('Cuantos pasos has caminado hoy? '))

calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

# Verificamos si se cumplio la meta de pasos diarios

meta_alcanzada = pasos_diarios >= META_PASOS_DIARIO
meta_alcanzada_txt = "Si" if meta_alcanzada else "No"

print(f'\nNombre: {nombre_usuario}')
print(f'Pasos dados: {pasos_diarios}')
print(f'Has quemado {calorias_quemadas} calorias')
print(f'Has llegado a la meta de pasos diarios? {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es de: {META_PASOS_DIARIO} pasos')