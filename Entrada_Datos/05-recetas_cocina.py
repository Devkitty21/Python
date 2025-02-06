# Receta de cocina
print('*** Receta de Cocina ***')

# Definimos los inputs y las variables

nombre_receta = input("Introduce el nombre de la receta: ")
ingredientes = input("Introduce los ingredientes: ")
tiempo_preparacion = int(input("Ingresa el tiempo de preparacion (min): "))
dificultad_receta = input("Dificultad de la receta: ")

# Imprimos todos los valores

print("-------------------")
print(f'Nombre de la receta: {nombre_receta}')
print(f'Ingredientes: {ingredientes}')
print(f'Tiempo de preparacion en minutos: {tiempo_preparacion}')
print(f'Dificultad: {dificultad_receta}')
