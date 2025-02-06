class Persona:

    atributo_clase = 0 # Los atributos de clase hay que definirlos fuera de los metodos/funciones

    def __init__(self,atributo_instancia):
        self.atributo_instancia = atributo_instancia


# Programa principal

if __name__ == '__main__':
    print(f'*** Atributos de clase ***')
    print(f'Atributo de clase: {Persona.atributo_clase}')
    # Modificar el atributo de clase
    Persona.atributo_clase = 10
    print(f'Atributo de clase: {Persona.atributo_clase}')

    # Creamos un objeto persona1
    persona1 = Persona(15)
    print(f'Atributo de Clase desde persona1: {persona1.atributo_clase}') # No es recomendable hacerlo de esta forma, es mas recomendable hacerlo llamando a la Clase y posteriormente agregando el nombre del atributo_clase
    print(f'Atributo de instancia desde persona1: {persona1.atributo_instancia}')

    # Creamos un objeto persona2
    persona2 = Persona(30)
    print(f'Atributo de Clase desde persona2: {persona2.atributo_clase}') # No es recomendable hacerlo de esta forma, es mas recomendable hacerlo llamando a la Clase y posteriormente agregando el nombre del atributo_clase
    print(f'Atributo de instancia desde persona2: {persona2.atributo_instancia}')

# Cada objeto tiene su valor de atributo_instancia pero comparten el valor de atributo_clase el cual si se modifica, se modifica para los dos objetos
# Esto pasa porque el atributo_clase se asocia con la clase Persona y no con el metodo