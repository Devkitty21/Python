# Este tipo de clases se usan cuando el atributo es bastante directo y con una funcionalidad
# bastante simple y facil, en el caso de que se necesitara agregar varios metodos y demas es
# mas recomendable usar una clase normal

from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True,frozen=True) # En el caso de que quitemos el frozen=True pasaria a ser mutable por lo cual no podriamos agregarlo a la coleccion
class Domicilio:
    calle: str
    numero: int = 0 # Agregamos un valor por default en este caso 0



# Este tipo de clases es conveniente cuando es bastante simple y no tiene muchos metodos
@dataclass(eq=True, frozen=True) # Con el parametro frozen hacemos que los objetos sean inmutables
class Persona:
    nombre: str # Podemos asignar un valor por default
    apellido: str
    contador_personas: ClassVar[int] = 0 # Creamos una variable de clase, indicamos de que tipo es y su valor por default
    domicilio: Domicilio


    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor de nombre: {self.nombre}') # Verificar que se rellenen los valores


domicilio1 = Domicilio('Saturno',15)
persona1 = Persona('Juan','Perez',domicilio1) # Le pasamos el nuevo objeto domicilio1
print(f"{persona1!r}")
# Variable de clase
print(f'Variable de clase: {Persona.contador_personas}')
# Variables de instancia
print(f'Variables de instancia: {persona1.__dict__}') # Nos podemos fijar que no incluye el atributo de contador_persona
# Variable con valores vacios
persona_vacia = Persona('Karla','',None)
print(f'Persona vacia: {persona_vacia}')
# Revisar igualdad entre objetos (__eq__)
persona2 = Persona('Juan','Perez', Domicilio('Saturno',15)) # Le pasamos el objeto al vuelo
print(f'Objetos iguales?: {persona1 == persona2}') # Apuntan al mismo objeto en memoria
# Agregar esta clase a una colecciones
coleccion = {persona1,persona2}
print(f'Coleccion: {coleccion}')
# Frozen = True
# coleccion[0].nombre = 'JuanCarlos'
# persona1.nombre = 'JuanCarlos'