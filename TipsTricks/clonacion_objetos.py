import copy

# Clonacion (copia) de objetos
# Copia superficial (shallow) o copia poco profunda

lista_a = [[1,2],[3,4],[5,6]]
# Copia superficial (shallow)

lista_b = list(lista_a) # El constructor list crea un nuevo objeto
# Las listas son dos objetos distintos apuntan a diferente posicion en memoria
# pero los niveles internos solos e copio la referencia, no se crearon nuevos objetos para las sublistas
print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')
# Comprobacion de que los objetos son distintos (a nivel superior)
# Un cambio en el nivel superior, no afecta a la otra lista
lista_a.append([7,8])
print('Son distintos objetos (nivel superior)')
print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')

# Comprobacion de que los objetos internos tienen la misma referencia (copai superficial)
# un cambio en uhn elemento de una sublista, afecta a la otra sublista de la otra lista
lista_a[0][1] = 'A'
print(f'La copia fue superficial, los elementos internos solo se copio la referencia')
print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')

# Crear copias profundas (import copy)
lista_c = [[1,2],[3,4],[5,6]]
lista_d = copy.deepcopy(lista_c)

# Comprobacion de que son objetos distintos
lista_c.append([7,8])
print(f'Son distintos objetos (nivel superior)')
print(f'Lista c: {lista_c}')
print(f'Lista d: {lista_d}')
# Ahora si, los elementos internos son nuevos objetos, no solo se copio la referencia
lista_c[0][1] = 'A'
print(f'Lista c: {lista_c}')
print(f'Lista d: {lista_d}')
# El metodo copy sirve para realizar copias poco profundas (shallow)


