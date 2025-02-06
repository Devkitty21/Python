print('*** Agenda de Contactos ***')

agenda = {
    'Carlos':{
        'telefono': '55667711',
        'email': 'carlos@gmail.com',
        'direccion': "Calle principal 132",
    },
    'Maria': {
        'telefono': '99887733',
        'email': 'maria@gmail.com',
        'direccion': 'Avenida central 456',
    },
    'Pedro': {
            'telefono': '55139078',
            'email': 'pedro@gmail.com',
            'direccion': 'Playa Mayor 789'
    }
}

print(agenda)

# Acceder a la informacion de un contacto en especifico

print(f"""Informacion del contacto de maria:
    Telefono: {agenda['Maria']['telefono']}
    Email: {agenda['Maria']['email']}
    Direccion: {agenda.get('Maria').get("direccion")}
""")

# Agregar un nuevo contacto
agenda['Ana'] = {
    'telefono': '55667781',
    'email': 'ana@gmail.com',
    'direccion': 'Martina Maiz n7'
                 }

# print(agenda)

# Eliminar un contacto existente
del agenda['Maria']
# Tambien podemos usar agenda.pop('Nombre')
print(agenda)

# Mostramos los contactos de la agenda

print('\n*** Contactos de la agenda ***\n')

for nombre, detalles in agenda.items():
    print(f"""Nombre: {nombre}
    Telefono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Direccion: {detalles.get('direccion')}
""")
