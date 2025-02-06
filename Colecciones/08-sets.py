print('*** Manejo de sets ***')
# Crear un conjunto
mi_set = {1, 2, 3, 4, 5, 4}
print(f"Mi set: {mi_set}")

# Agregfar elementos al set
mi_set.add(6)
mi_set.add(7)
# print(f"Mi set modificado: {mi_set}")

# Intentamos agregar un elemento duplicado
mi_set.add(3)
# print(f"Mi set modificado: {mi_set}")

# Eliminar un elemento
mi_set.remove(4)
print(f'Mi set modificado: {mi_set}')

# Iterar los elementos del set
for elemento in mi_set:
    print(elemento, end=" ")

# Comprobar si existe un elemento en el set
print(f'\nExiste le valor de 1 en el set? {1 in mi_set}')

# Obtener la longitud del set
print(f"Longitud del set: {len(mi_set)}")