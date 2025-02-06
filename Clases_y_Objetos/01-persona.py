class Persona:

    # Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f"""Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}""")
        print(f'Direccion de memoria del objeto self: {id(self)}')
        print(f'DIreccion de memoria del objeto self hexadecimal: {hex(id(self))}')



# Creacion de los objetos

if __name__ == "__main__":
    persona1 = Persona('Diogo','Roman') # Crea un objeto vacio en la memoria
    persona1.mostrar_persona()
    print(f'Direccion de memoria del objeto persona 1: {id(persona1)}')
    print(f'DIreccion de memoria del objeto persona 1 hexadecimal: {hex(id(persona1))}')

# Creamos un segundo objeto
    persona2 = Persona('Diogo', 'Vieira') # Creamos un objeto vacio en la memoria
    persona2.mostrar_persona() # En el caso de que lo mandemos antes de inicializar_persona, nos dara un error
    print(f'Direccion de memoria del objeto persona 2: {id(persona2)}')
    print(f'DIreccion de memoria del objeto persona 2 hexadecimal: {hex(id(persona2))}')



