# Decoradores de Clase
# Permiten transformar de manera programatica nuestra clase
# Es similar a los decoradores de funciones (es metaprogramacion)
import inspect

def decorador_repr(cls):
    print('1. Se ejecuta decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')


    atributos = vars(cls) # Con el metodo vars obtenemos el diccionario de los atributos de un objeto

    # Revisamos si se ha sobreescrito el metodo __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el metodo __init__')

    firma_init = inspect.signature(cls.__init__)
    print(f'Firma metodo __init__  {firma_init}')
    # Recuperamos los parametros, excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parametros init: {parametros_init}')

    # Revisamos si cada parametro tiene un parametro property asociado
    for parametro in parametros_init:
        # Property es un valor de tipo built-in para preguntar
        # si se esta utilizando el decorador property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un metodo property para el parametro: {parametro}')

    # Crear el metodo repr dinamicamente
    def metodo_repr(self):
        #Obtenemos el nombre de la clase dinamicamente
        nombre_clase = self.__class__.__name__
        # Obtenemos los nombres de las propiedades y sus valores
        # Expresion generadora, crear nombre_atr=valor_atr
        generador_arg = (f'{nombre}={getattr(self,nombre)!r}' for nombre in parametros_init)
        # Lista del generador
        lista_arg = list(generador_arg)
        # Creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_arg)
        # Creamos la forma del metodo __repr__ sin su nombre
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'
        return resultado_metodo_repr


    # Agregar dinamicamente el metodo repr a nuestra clase
    setattr(cls,'__repr__',metodo_repr)

    return cls # Debe enviarse para poder terminar la creacion de la persona


@decorador_repr
class Persona:

    def __init__(self,nombre, apellido,edad):
        print('2. Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad
    # def __repr__(self):
    #     return f'{__class__.__name__}(nombre={self.nombre}, apellido={self.apellido})'

persona1 = Persona('Juan','Perez',28)
print(persona1)
persona2 = Persona('Karla','Gomez',30)
print(persona2)
# Tiene los metodos de propiedad, nombre, apellido, repr
print(dir(Persona))
# Tiene el metodo repr sobreescrito
codigo_repr = inspect.getsource(Persona.__repr__)
print(codigo_repr)