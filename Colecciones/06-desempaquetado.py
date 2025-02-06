print('*** Desempaquetado de tuplas ***') # Unpacking

producto = ('P001', "Camisa", 20.00)

# Desempaquetado
id, descripcion, precio = producto

# Imprimir los valores
print(f'Tupla completa: {producto}')
# Valores indepentiendes ya desempaquetados
print(f'Producto: id = {id}, descripcion = {descripcion}, precio = {precio}')