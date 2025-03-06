# Profundizando en diccinarios

# Los dic guardan un orden (a diferencia de un set)
diccionario = {'Nombre':'Juan','Apellido':'Perez','Edad':28}
print(diccionario)

# Los diccionarios son mutables, pero las llaves deben ser inmutables
# diccionario = {[1,2]:'Valor'} # No podemos usar una lista como una llave por que es mutable
# diccionario = {(1,2):'Valor'}
print(diccionario)

# Se agrega una llave si no se encuentra
diccionario['Departamento'] = 'Sistemas'
print(diccionario) # Como en este caso el diccionario no tiene la llave Departamento la agrega + su valor, en el caso de que si este esa llave, remplaza su valor por el que hayamos proporcionado

# No hay valores duplicados en las llaves de un diccionario (La llave es unica, si ya existe se remplaza)
diccionario['Nombre'] = 'Juan Carlos' # No se crea una nueva llave, sino que se remplaza el valor de Juan por Juan Carlos
print(diccionario)

# Recuperar un valor indicando una llave
print(f'Valor recuperado por la llave: {diccionario["Nombre"]}')
# print(diccionario['nombre']) # En el caso de que la llave no exista, nos devuelve un error de tipo KeyError

# Metodo get recupera una llave, y sino existe NO lanza una excepcion
# Ademas podemos regresar un valor en caso de que no exista la llave
print(diccionario.get('Nombre','No se encontro la llave')) # Si usamos una llave NO existente mandara el mensaje por default de No se encontro la llave
# print(diccionario)

# setdefault si modifica el diccionario, ademas se agrega un valor por default
nombre = diccionario.setdefault('Nombres', 'Valor por default') # En este caso si la llave no existe, se agrega con el valor indicado que en este caso es 'Valo por default'
print(nombre)
print(diccionario)

# Imprimir con pprint
from pprint import pprint as pp
# help(pp)
pp(diccionario, sort_dicts=False) # Por default viene con ordenamiento ascendente para el diccionario, en el caso de que no queramos se usa el parametro sort_dicts=False
