import os

class Persona:

    contador_personas = 0

    def __init__(self, nombre, apellido):
        # Incrementamos el valor del atributo de clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

    @staticmethod
    def get_contador_personas_estatico():
        print(f'Metodo estatico')
        return Persona.contador_personas

    @classmethod # Esta practica es mas recomendada
    def get_contador_personas_clase(cls):
        print(f'Metodo de Clases')
        return cls.contador_personas

if __name__ == '__main__':
    print(f'*** Ejemplo contador dde objetos de tipo persona ***')
    # Creamos el primer objeto
    persona1 = Persona('Gerardo', 'Perez')
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona('Daniel', 'Sanchez')
    persona2.mostrar_persona()

#     Imprimir el valor del contador de objetos persona
    print(f'Contador objetos Persona: {Persona.contador_personas}')
    print(f'Contador objeots personas (persona1): {persona1.contador_personas}')
    print(f'Contador objetos personas (personas2): {persona2.contador_personas}')
    print(f'Contador de objetos personas (staticmethod): {Persona.get_contador_personas_estatico()}')
    print(f'Contador de objetos personas (classmethod): {Persona.get_contador_personas_clase()}')
