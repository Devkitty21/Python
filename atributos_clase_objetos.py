class Persona:
    contador_personas = 0
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Mostrar los atributos de un objeto
persona1 = Persona('Juan','Perez')
print(persona1.__dict__)

# Crear un atributo al vuelo (Quiere decir crearlo al momento)
print(persona1.contador_personas) # Accediendo al atributo de clase
# Pero no es posible modificarlo con el objeto, sino con la clase
persona1.contador_personas = 10 # Se a asociado una variable al vuelo (Solo se asocia a este objeto)
print(persona1.__dict__)

# El atributo anterior oculta al atributo de clase
print(Persona.contador_personas) # Accedemos al atributo de clase
print(persona1.contador_personas) # Accedemos al atributo del objeto 1

# Un segundo objeto
persona2 = Persona('Karla','Gomez')
print(persona2.__dict__) # El atributo de contador_persona solo se aplica para la persona1, los nuevos objetos
# solo tienen los atributos definidos en la plantilla
print(persona2.contador_personas)

# Asociar un atributo de clase al vuelo
Persona.contador2 = 20
print(Persona.contador2)
