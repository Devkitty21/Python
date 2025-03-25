# Con doble guion bajo, no solo es una convencion
# sino que afecta la forma en que se acceden los atributos o metodos

class Padre:
    def __init__(self):
        self.variable_publica = 1
        self._variable_protegida = 2
        self.__variable_privada = 3

    def get_variable_privada(self):
        return self.__variable_privada # Aqui si podemos acceder al atributo ya que estamos dentro de la clase


    def __metodo_privado(self):
        print('Accediendo metodo privado padre...')


class Hijo(Padre):
    def __init__(self):
        super().__init__()
        self.variable_publica = 'sobreescrita 1'
        self._variable_protegida = 'sobreescrita 2'
        self.__variable_privada = 'sobreescrita 3'

    def __metodo_privado(self):
        print('Accediendo metodo privado hijo...')


# Prueba usando una variable global
_Prueba__variable_global = 10 # Estamos respetando la sintaxis de name mangling

class Prueba:
    def obtener_variable(self):
        return _Prueba__variable_global




if __name__ == '__main__':
    padre = Padre() # Creamos una instancia de nuestra clase

    # Imprimir todos los atributos de la clase
    print(dir(padre))
    # Accedemos a los atributos de la clase
    print(f'Variable publica: {padre.variable_publica}')
    print(f'Variable protegida: {padre._variable_protegida}') # No debemos de acceder de esta forma
    # print(f'Variable privada: {padre.__variable_privada}') Esto nos manda un error de tipo AtributeError
    print(f'Variable privada usando name mangling: {padre._Padre__variable_privada}') # Para acceder a este valor tenemos que usar name manglin
    # Sintaxis de Name mangling: objeto._ClassName__atributo

    # Name mangling es transparente para el programador
    print(f'Acceso por medio del metodo get: {padre.get_variable_privada()}')

    # Prueba clase hijo
    hijo = Hijo()
    print(f'Acceso publico desde hijo: {hijo.variable_publica}')
    print(f'Acceso protegido desde hijo: {hijo._variable_protegida}') # No se recomienda accederlo fuera de la clase/modulo
    # print(f'Acceso privado desde hijo: {hijo.__variable_privada}') Esto dara un error
    # utilizando name mangling desde la clase hija
    print(f'Acceso privado desde hijo con name mangling: {hijo._Hijo__variable_privada}') # Desde aqui accedemos al atributo privado definido en la clase hijo
    print(f'Acceso privada desde hijo a la clase padre: {hijo._Padre__variable_privada}') # Desde aqui accedemos al atributo privado definido en la clase Padre

    # Tambien podemos usar metodos con doble _ bajo
    # padre.__metodo_privado() Esto nos va a dar un error, no podemos acceder directamente a este metodo

    padre._Padre__metodo_privado() # Usamos tambien name mangling para acceder
    # Ahora desde la clase hijo
    hijo._Hijo__metodo_privado()
    hijo._Padre__metodo_privado()

    # Accediendo a la variable global
    print(f'Accediendo variable global: {_Prueba__variable_global}') # No es parte de ninguna clase asi que podemos acceder directamente
    # Usando name mangling y la clase para acceder a la variable global
    prueba = Prueba()
    print(f'Accediendo variable global desde una clase: {prueba.obtener_variable()}')


