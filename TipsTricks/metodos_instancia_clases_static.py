# Metodos de intancia, clase y static y sus diferencias
class MiClase:

    # Reciben los metodos y atributos de la instancia
    def metodo_instancia(self):
        # Retornamos una taupla
        return 'Metodo de instancia ejecutado...', self

    # Reciben los metodos y atributos de la clase
    @classmethod # Usamos el decorador classmethod para definir el metodo de clase
    def metodo_clase(cls): # Usa cls para hacer referencia a la clase
        # Retornar una tupla
        return 'Metodo de clase ejecutado...', cls

    # No reciben ningun parametro, no tienen acceso ni a la instancia ni a la clase
    @staticmethod
    def metodo_estatico(): # Estos metodos se van a ejecutar pero no pueden modificar ni los metodos de la instancia ni de la clase
        return 'Metodo estatico ejecutado...' # Se usa para metodos de utileria o de ayuda!



if __name__ == '__main__':
    miclase = MiClase()

    # Caso 1. Ejecutamos el metodo de instancia de manera implicita
    print(miclase.metodo_instancia())
    # Caso 1.1. Ejecutamos el metodo de instancia de manera explicita
    print(MiClase.metodo_instancia(miclase)) # Si lo hacemos de esta manera hay que pasar el objeto como referencia
    # Caso 1.2. Ejecutamos el metodo de instancia desde la clase
    print(MiClase.metodo_instancia(MiClase))
    # Caso 2. Ejecutamos el metodo de clase
    print(MiClase.metodo_clase())
    # Caso 2.1. Desde la instancias podemos acceder a los metodos de clase
    print(miclase.metodo_clase()) # Coje el tipo de objeto y se pasa como argumento automaticamente
    # Caso 3. Ejecutamos el metodo estatico
    print(MiClase.metodo_estatico()) # Este metodo se le manda una informacion y devuelve informacion pero no modifica nada
    print(miclase.metodo_estatico()) # Se puede llamar de las dos formas al metodo estatico


