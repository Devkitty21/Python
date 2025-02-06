# Metodos de cadenas

cadena1 = "Hola Mundo"
print(f'Cadena original: {cadena1}')

mayusculas = cadena1.upper() # .upper() para convertir a mayusculas
print(f"Cadena en mayusculas: {mayusculas}")
print(f"Cadena en minusculas {cadena1.lower()}") # podemos convertir directamente a minusculas sin tener que definir una variable de mas

cadena2 = " Juan Perez "
print(f'Cadena con espacios: {cadena2}')
print(f"Cadena sin espacios: {cadena2.strip()}") #Eliminar espacios del principio y del final