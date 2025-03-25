# El guion bajo simple se usa por convencion, se usa para indicar
# que una variable es temporal o sin importancia

# Ejemplo 1.
for _ in range(3): # Consideramos que es una variable temporal/sin importancia
    print('Hola...')

# Tambien lo podemos utilizar cuando trabajamos con tuplas
valores = ('Juan','Perez',31)
# Unpacking
nombre, _, edad = valores # En este caso el apellido no nos interesa
print(f'Nombre: {nombre}')
print(f'Edad: {edad}')
# print(f'Apellido: {_}') No se recomendaria acceder a esta variable

# Se puede usar como variable temporal de cualquier tipo

_ = list()
_.append(1)
_.append(2)
_.append(3)
print(f'Variable temporal que apunta a una lista: {_}')