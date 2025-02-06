print(f'*** Obtener coordenadas x, y, z ***')

def obtener_coordenadas():
    x,y,z = 10, 20, 30
    return x,y,z

# Llamamos la funcion

resultado = obtener_coordenadas()

print(f'Las coordenadas son {resultado}')

# Unpacking de tupla

x1, y1, z1 = resultado
print(f'Coordenada x: {x1}, y: {y1} y z: {z1}')