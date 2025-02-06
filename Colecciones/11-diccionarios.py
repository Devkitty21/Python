print('*** Diccionarios en Python ***')

# Creamos un dict de persona con clave y valor
persona = {
    "nombre": "Sergio",
    'edad': 30,
    'ciudad': 'Mexico'
}

print(f'Diccionario de persona original: {persona}')

# Acceder a los elementos de el diccionario
print(f'Nombre: {persona["nombre"]}')
print(f'Edad: {persona.get("edad")}') # Es el mismo resultado simplemente usando el metodo get
print(f'Ciudad: {persona["ciudad"]}')


# Modificar un valor de un diccionario
persona['edad'] = 35 # Se puede usar esta forma tanto para modificar como para agregar un nuevo valor
print(f'Diccionario de persona modificada: {persona}')

# Agregar un nuevo elemento
persona['profesion'] = "ingeniero"
print(f'Diccionario de persona modificada: {persona}')

# Eliminar un elemento usando la palabra del
del persona['ciudad']
print(f'Diccionario de persona modificada: {persona}')

persona.pop('profesion')
print(f'Diccionario de persona modificada: {persona}')

# Iterar los elementos de un diccionario (llave,valor)
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')

# Obtener los valores

print('\n')
print(f'Valores del diccionario:')
for valor in persona.values():
    print(f'-- Valor: {valor}')

# Obtener las llaves

print('\n')
print('Llaves del diccionario')
for llaves in persona.keys():
    print(f'-- Llave: {llaves}')