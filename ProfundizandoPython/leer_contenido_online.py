# Leer contenido online
from urllib.request import urlopen

# with urlopen('https://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
#     # contenido = mensaje.read()
#     contenido = mensaje.read().decode('utf-8') # Decodeamos el mensaje ya que viene codificado
#     print(contenido) # Podemos ver que es una cadena de bytes porque tiene una b al inicio de bytes
#
# with open('nuevo_archivo.txt','w',encoding='utf8') as archivo:
#     archivo.write(contenido)

# palabras = []
# with urlopen('https://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
#     for linea in mensaje: # Primero recorremos todas las lineas y las spliteamos + decodificamos
#         palabras_por_linea = linea.decode('utf8').split()
#         for palabra in palabras_por_linea: # Ahora que esta todo spliteado y decodificado todas las palabras las agregamos a la lista
#             palabras.append(palabra)
#
# print(palabras)


with urlopen('https://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
    contenido = mensaje.read().decode('utf8')

# Contar ocurrencias de una cadena
print('Numero de veces que aparece la palabra Universidad:',contenido.count('Universidad'))

# Metodo upper
# print(contenido.upper()) # Convierte a mayusculas un str (No modifica el texto original, genera una nueva cadena)
# print(contenido)

# Metodo lower
# print(contenido.lower()) # Convierte a minusculas un str

# Buscamos la cadena Python en el contenido
# print('Existe Python?:','python'.lower() in contenido.lower()) # Todo en minusculas
# print('Existe Python?:','python'.upper() in contenido.upper()) # Todo en mayusculas

# Startswith - Inicia con...
# print('Inicia con:',contenido.startswith('En GlobalMentoring.com.mx'))

# endswith - Termina con...
# print('Termina con:',contenido.lower().endswith('Fundador de GlobalMentoring.com.mx'.lower()))

mensaje = 'Hola Mundo'
# print(mensaje.lower().islower()) # Primero lo pasamos todo a minusculas para luego preguntar si esta cadena esta toda en minusculas
# print(mensaje.upper().isupper()) # Primero todos los caracteres los convertimos en mayusculas y luego preguntamos si esta cadena esta toda en mayuscula


# Alinear cadenas

# Centrar cadena - center
titulo = 'Sitio Web de GlobalMentoring.com.mx'
# print(len(titulo))
# print(titulo.center(10,'*')) # Si ponemos menos caracteres de los que tiene el titulo los caracteres de relleno no se aplican
# print(len(titulo.center(50,'*'))) # Si solo pasamos la variable titulo cojera el titulo original ya que apunta a otro objeto en memoria
# print(titulo.center(len(titulo)+10,'-'))

# ljust - alinea a la izquierda

# print(titulo.ljust(50,'*'))
# print(titulo.ljust(len(titulo)+10,'-'))

# rjust - alinea a la derecha
# print(titulo.rjust(50,'*'))
# print(titulo.rjust(len(titulo)+10,'-'))

# Reemplazar contenido en un str - replace
print(contenido.replace(' ','-')) # Los strings son inmutables por lo cual se crea un nuevo str para estas modificaciones

# Eliminar caracteres al inicio y al final de un str - Strip
titulo = ' *** GlobalMentoring.com.mx *** '
print(f'Cadena original: {titulo}, {len(titulo)}')
titulo = titulo.strip()
print(f'Cadena modificada: {titulo}, {len(titulo)}')


titulo = '***GlobalMentoring.com.mx***'.strip('*')
print('Cadena modificada:',titulo, len(titulo))
titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
print('Cadena modificada:',titulo)
titulo = '***GlobalMentoring.com.mx***'.rstrip('*')
print('Cadena modificada:',titulo)

titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print(f'Cadena modificada: {titulo}')