class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Sobreescritura del metodo __str__
    def __str__(self):
        return f"""Persona: 
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Dir. Memoria {super.__str__(self)}
        """


# Codigo principal
persona1 = Persona('Juan', 'Perez')
print(persona1) # El metodo __str__ se ejecuta automaticamente desde print
# print(persona1.__str__()) # Explicitamente llamamos al metodo __str__ es opcional

