# Namedtuples son una extension del tipo tupla
# Son una alternativa para escribir clases (atributos tipos inmutables)
# Asignar un identicador a cada elemento de la tupla
from collections import namedtuple
# Definimos una clase con atributos inmutables pero usando namedtuple

Persona1 = namedtuple('Persona1', 'nombre apellido edad')
# Creamos una instancia de la clase (se agrega un constructor por default con los atributos indicados)
persona1 = Persona1('Juan','Perez',28)
# Enn automatico se crea un metodo __repr__ con los atributos que hemos proporcionado
print(persona1)

# Creamos nuestra clase con los atributos usando una lista
Persona2 = namedtuple('Persona2',['nombre','apellido','edad']) # Esta sintaxis es mas limpia y bonita
persona2 = Persona2('Karla','Gomez',30)
print(persona2) # Se agrega un metodo __repr__ de manera automatica

# Podemos acceder a los atributos de manera individual por nombre
print(f'Nombre: {persona2.nombre}, '
f'Apellido: {persona2.apellido}, '
f'Edad: {persona2.edad}')

# Acceder a los atributos por indice
print(f'Nombre: {persona2[0]}')
print(f'Apellido: {persona2[1]}')
print(f'Edad: {persona2[2]}')
# Podemos convertir los valores a unta tupla
print(tuple(persona2))
# Podemos hacer unpacking de los elementos de nuestra tupla
nombre, apellido,edad = persona2
print(f'Valores tupla persona: {nombre}, {apellido}, {edad}')
# Podemos hacer unpacking pasando como argumento
print(*persona2)
# Las tuplas son inmutables al igual que namedtuple
# persona2.edad = 30

# Subclases de namedtuples
class Persona3(Persona2):
    # Agregamos un nuevo metodo a la clase hija
    def convertir_mayusculas(self):
        return f'Nombre Completo: {self.nombre.upper()} {self.apellido.upper()}'

persona3 = Persona3('Saioa','Aldasoro',30)
print(persona3.convertir_mayusculas())

# Existe otra forma de hacer extends de la clase (la forma recomendada con namedtuple)
Persona4 = namedtuple('Persona4',Persona2._fields + ('email',)) # _fields nos da una tupla con los atributos
# Creamos un obejeto persona4 con el nuevo atributo de email
persona4 = Persona4('Saioa','Aldasoro',30,'saldasoro@gmail.com')
print(persona4) # Se genera el metodo __repr__ automaticamente para este objeto

# Metodos de ayuda (built-in) en namedtuple
print(persona4._fields)
# Ej. Convertir a un diccionario
diccionario_persona4 = persona4._asdict() # Convertimos los atributos como si fuera un diccionario
print(diccionario_persona4)