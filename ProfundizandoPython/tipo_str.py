import math
import os

from mi_clase import MiClase
# Profundizando en el tipo str

# Concatenacion automatica en python
# variable = 'Adios'
# mensaje = 'Hola' 'Mundo' + variable
# mensaje += 'Universidad' 'Python' # Aqui tenemos la concatenacion automatica
# print(mensaje,'\n')


# Metodo help por si necesitas ayuda en alguna funcion/clase/objeto...
# help(math.isnan)
# help(str.capitalize) # En el caso de que necesitemos ayuda en un metodo especifico simplemente se pone el nombre del metodo
# help(math)
# help(str)


# Docstring no solo sirve para hacer strings de varias lineas. Aqui abajo unos ejemplos para lo que puede servir

# help(MiClase)
# print(MiClase.__doc__) # Solo llama el docstring de la clase, no de los metodos o de los atributos a diferencia del metodo help
# print(MiClase.__init__.__doc__) # Quitar los parentesis, porque sino estamos llamando a la funcion y no queremos eso
# print(MiClase.mi_metodo.__doc__) # Llamamos a la documentacion de mi metodo
# print(MiClase.mi_metodo)
# print(type(MiClase.mi_metodo)) # Type lo usamos para saber de que tipo es alguna cosa en python

# Las cadenas son inmutables = No se pueden modificar

# mensaje1 = 'hola mundo'
# mensaje2 = mensaje1.capitalize()
# print(f'Mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')
# print(f'Mensaje2: {mensaje2}, id: {hex(id(mensaje2))}')
# mensaje1 += 'adios'
# print(f'Mensaje1: {mensaje1}, id: {hex(id(mensaje1))}')

# Cualquier modificacion que le hagamos a un str se va a crear un nuevo objeto en memoria


# help(str.join)

# Usando el metodo .join()
# tupla_str = ('Hola','Mundo','Universidad','Python')
# mensaje = ' '.join(tupla_str)
# print(f'Mensaje: {mensaje}')
#
# lista_cursor = ['Java','Python','Anuglar','Spring']
# mensaje = ', '.join(lista_cursor)
# print(f'Mensaje: {mensaje}')
#
# cadena = 'HolaMundo'
# mensaje = '.'.join(cadena)
# print(f'Mensaje: {mensaje}')
#
# diccionario = {
#     'Nombre':'Juan',
#     'Apellido':'Perez',
#     'Edad':'18' # Tenemos que ponerlo como si fuera un str por que sino dara error ya que estamos trabajando con tipo str
#                }
# llaves = ' '.join(diccionario.keys())
# valores = ' '.join(diccionario.values())
# print(f'Llaves: {llaves}, type: {type(llaves)}')  # Al usar el metodo join todo pasa a ser un str
# print(f'Valores: {valores}, type: {type(valores)}')

# help(str.split)

# cursos = 'Java Python Javascript Angular Spring Excel'
# lista_cursos = cursos.split()
# # print(f'Lista cursos: {lista_cursos}')
# # print(type(lista_cursos))
#
# cursos_separados_coma = 'Java, Python, Javascript, Angular, Spring, Excel'
# lista_cursos = cursos_separados_coma.split(', ')
# # print(f'Lista cursos: {lista_cursos}')
# # print(len(lista_cursos))
#
# lista_cursos = cursos_separados_coma.split(', ',3)
# print(f'Lista cursos: {lista_cursos}')
# print(len(lista_cursos))


# Dar formato a un string
# nombre = 'Juan'
# edad = 28
# mensaje_con_formato = 'Mi nombre es %s y mi edad %d' %(nombre,edad)
# print(mensaje_con_formato)

# persona = ('Karla','Gomez',5000.00)
# mensaje_con_formato = 'Hola %s %s, Tu sueldo es: %.2f'%persona # Se le pasa primero los valores y luego se imprime
# print(mensaje_con_formato)
# mensaje_con_formato = 'Hola %s %s, Tu sueldo es: %.2f'
# print(mensaje_con_formato %persona) # Se le pasa directamente en el print los valores


# Dar formato con el metodo format

nombre = 'Juan'
edad = 28
sueldo = 5000.0
mensaje = 'Nombre {}, edad {}, Sueldo: {:.2f}'.format(nombre,edad,sueldo)
# print(mensaje)
# print('Nombre {}, edad {}, Sueldo: {:.2f}'.format(nombre,edad,sueldo)) # Si no la vamos a reutilizar el mensaje podemos imprimirlo directamente

# mensaje = 'Sueldo {2:.2f}, Edad {1}, Nombre {0}'.format(nombre,edad,sueldo)
# print(mensaje)

# mensaje = 'Nombre {n}, Edad {e}, Sueldo {s:.2f}'.format(n=nombre,e=edad,s=sueldo)
# print(mensaje)

# diccionario = {
#     'Nombre':'Ivan',
#     'Edad':35,
#     'Sueldo':8000.0
# }
# mensaje = 'Nombre {dic[Nombre]}, Edad {dic[Edad]}, Sueldo {dic[Sueldo]:.2f}'.format(dic=diccionario)
# print(mensaje)


# Usando f-string

nombre = 'Juan'
edad = 28
sueldo = 5000.0
mensaje = f'Nombre {nombre}, edad {edad}, Sueldo: {sueldo:.2f}'
# print(mensaje)

# Metodo print
print(nombre, edad, sueldo, sep=', ')

