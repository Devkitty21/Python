print(f'*** Lista de Reproduccion')
# Creamos la lista vacia
playlist = []

numero_canciones = int(input('Cuantas canciones deseas agregar: '))

# Iteramos cada elemnto de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Proporciona la cancion {indice + 1}: ')
    playlist.append(cancion)

# # Empezamos a agregar canciones
# playlist.append("Hotel California - Eagles")
# playlist.append("Staying alive - Bee Gees")
# playlist.append("Dream on - Aerosmith")

# Ordenar la lista en orden alfabetico .sort
# playlist.sort(reverse=True)
playlist.sort()

# Mostrar la lista de canciones

print(f'\nLista de reproduccion en orden alfabetico: {playlist}')

# Mostrar la lista iterando sus elementos
print('\nIteramos el playlist')
for cancion in playlist:
    print(f'- {cancion}')

