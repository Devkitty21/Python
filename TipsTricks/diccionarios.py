# Diccionarios - dicts
# En otros lenguajes de programacion existen otros nombres: maps, hashmaps, lookup tables, etc...
# (llave-valor)

# Ejemplo clasico: Directorio (llave=nombre, valor=telefono)
directorio = {
    'Juan': 55689001,
    'Alicia': 56432217,
    'Carlos': 56772345
}

# Imprimimos el diccionario
print(directorio)

# Recuperar un elemento
print(directorio['Juan']) # Recupera el valor de la llave 'Juan'

# Manda un error de tipo KeyError al no encontrar una llave
# print(directorio['juan'])

# Podemos utilizar una expresion para crear un diccionario
valores_al_cuadrado = {x: x*x for x in range(5)} # Mezclandolo con List comprehension
print(valores_al_cuadrado)

# Los tipos mutables no pueden ser llaves de un diccionario
lista = [1,2,3]
# diccionario_erroneo = {lista: 'A'} # Una lista debido a que es mutable nos da error
# print(diccionario_erroneo) # No podemos agregar objetos mutables a un diccionario, deben ser Inmutables

# Los tipos inmutables pueden ser llaves de un diccionario
tupla = (1,2,3)
diccionario_correcto = {tupla: 'A'}
print(diccionario_correcto)

# Si queremos garantizar un orden de insercion, OrderedDict()
from collections import OrderedDict

diccionario_ordenado = OrderedDict(uno=1,dos=2,tres=3) # (Key-valor)
print(diccionario_ordenado)
# Agregamos un nuevo elemento
diccionario_ordenado['cuatro'] = 4
print(diccionario_ordenado)
# Obtenemos las llaves
print(diccionario_ordenado.keys())
# Obtenemos los valores
print(diccionario_ordenado.values())

# Si cambiamos elgun valor de alguna llave
diccionario_ordenado['uno']=-1
print(diccionario_ordenado)

# Eliminamos alguna llave
diccionario_ordenado.pop('tres')
#
# Volvemos a insertar el elemento eliminado
diccionario_ordenado['tres'] = 3
print(diccionario_ordenado)

# Dedfaultdict es una subclase de dict
from collections import defaultdict # Esta linea deberia ir ensi al principio del programa
diccionario_default = defaultdict(lambda: 'Esta key no existe!')
diccionario_default['a'] = 1
diccionario_default['b'] = 2
print(diccionario_default.items())
# Imprimir un elemento no existente
print(diccionario_default['c'])

# Podemos crear valores por default como una lista
diccionario_default_lista = defaultdict(list)
# Si accedemos a una llave no existente, la crea y los valores se asignan como una lista
diccionario_default_lista['nombre'].append('Juan')
diccionario_default_lista['nombre'].append('Karla')
diccionario_default_lista['nombre'].append('Laura')
print(diccionario_default_lista)
print(diccionario_default_lista.items())
print(diccionario_default_lista.keys())
print(diccionario_default_lista.values())

###################
# Buscar en multiples diccionarios como si fuera un diccionario unico
from collections import ChainMap
diccionario1 = {'uno':1, 'dos':2, 'tres':3, 'cinco': 'A'}
diccionario2 = {'cuatro':4, 'cinco':5}

# Combinar los dos diccionarios como si fueran uno
combinacion_diccionarios = ChainMap(diccionario1,diccionario2) # Si encuentra un elemento antes que otro elije el que primero encuentra
print(combinacion_diccionarios)
# Buscamos en todos los diccionarios (de izquierda a derecha)
print(combinacion_diccionarios['cinco'])
# Una llave no existente manda un KeyError
# print(combinacion_diccionarios['seis'])

# Crear diccionarios de solo lectura (Readonly)
from types import MappingProxyType
diccionario_modificable = {'uno':1, 'dos':2, 'tres':3}
diccionario_solo_lectura = MappingProxyType(diccionario_modificable)
# Leemos el valor del diccionario
print(diccionario_solo_lectura)
print(diccionario_solo_lectura['uno'])
# Manda un error si queremos modificar el valor de diccionario de solo lectura
# diccionario_solo_lectura['uno'] = -1 # No podemos modificar ningun valor de este diccionario
# Si modificamos el diccionario mutable, afecta al de solo lectura
diccionario_modificable['dos'] = 22
# Veamos los cambios en los diccionarios
print(diccionario_modificable)
print(diccionario_solo_lectura) # Tambien se modifica

