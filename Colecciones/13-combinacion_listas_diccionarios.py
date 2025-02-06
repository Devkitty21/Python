print('*** Listas y Diccionarios ***')

personas = [{
    'nombre': 'regina',
    'apellido': 'Flores',
    'edad': 32
    },
    {
    'nombre': 'Alejandro',
    'apellido': 'Reyes',
    'edad': 32

    }]

# Acceder a un diccionario desde una lista

print(f'Detalle del primer elemento: ')
print(f"""Nombre: {personas[0].get('nombre')}
Apellido: {personas[0].get('apellido')}
Edad: {personas[0].get('edad')}
""")

# Recorrer los elementos de la lista
print()
for contador, persona in enumerate(personas):
    print(f'{contador} - Persona: {persona}')
    # print(f'Detalle: Nombre: {persona.get("nombre")}, Apellido: {persona.get("apellido")}, Edad: {persona.get("edad")}')