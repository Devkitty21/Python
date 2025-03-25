# Comparacion del usop del operador == o el operador is en POO

# El operador == compara el contenido de 2 objetos (contenido igual)
# No necesariamente son el mimso objeto (Pueden apuntar a objetos distintos)

# Operador is revisa si dos objetos son iguales (objetos identicos)
# Ambos deben estar apuntando a la misma direccion de memoria para considierarse iguales

# Ejemplo de una lista
lista_a = [1,2,3]
lista_b = lista_a

# En este caso tanto la lista a y b tienen el mimso contenido (== es True)
# y tambien apuntan a la misma referencia (is regresa True)
print(f'Lista a y b tienen el mimso contenido: {lista_a == lista_b}')
print(f'Lista a y b son el mimso objeto: {lista_a is lista_b}')

# Sin embargo, si creamos un nuevo objeto
lista_c = list(lista_a)
# En este caso la lista a tiene el mimso contenido que c (== es True)
# pero... lista c apunta a un objeto distinto en memoria (is regresara False)
print(f'Lista a y c tienen el mimso contenido: {lista_a == lista_c}')
print(f'Lista a y c son el mismo objeto: {lista_a is lista_c}')