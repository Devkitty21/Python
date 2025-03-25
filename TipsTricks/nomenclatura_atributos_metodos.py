from mi_modulo import _funcion_protegida # Con * importamos todos los atributos/metodos disponibles
from mi_modulo import  funcion_publica


class MiClase:
    def __init__(self):
        self.mi_variable_publica = 10
        # No debemos acceder directamente a este atributos ya sea para leerlo o modificarlo
        self._mi_variable_protegida = 11  # Esta variable se deberia de usar solo de forma interna

# Creamos la prueba de la clase
if __name__ == '__main__':
    objeto = MiClase()
    print(objeto.mi_variable_publica)
    # Esto NO es una buena practica
    print(objeto._mi_variable_protegida) # Esta variable no deberiamos estar accediendola de esta forma aunque podamos hacerlo

    # Accedemos a las funciones del modulo importado
    funcion_publica()
    # Si utilizamos el import * no se puede acceder a funciones con guion bajo al principio porque son funciones protegidas
    _funcion_protegida() # Estas solo deben ser usadas dentro del mismo modulo/clase

# El guion bajo al final se usa para evitar conflictos con nombres (keywords)
# Ej. class, def, pass, try etc...
def funcion1(nombre, class_): # Usamos el guion bajo para usar un nombre similar
    print('Funcion que recibe una clase y un nombre:', nombre, class_)

# Llamamos a la funcion
funcion1('Juan',None)




