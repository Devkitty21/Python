# Las funciones en python son ciudadanos de primera clase
def mayusculas(texto):
    return texto.upper()


# Uso normal de una funcion

# No es posible mandar a llamar la funcion antes de definirla
print(mayusculas('Hola'))

# Uso de una funcion como un objeto
# Asignar la referencia de la funcion a una variable, sin los parentesis
variable_funcion = mayusculas
print(f'Funcion mayusculas: {mayusculas}')
print(f'Variable funcion: {variable_funcion}') # Ambas apuntan al mismo objeto

# Utilizamos la variable_funcion en cualquier momento
print(variable_funcion('Nuevo Texto'))

# Para demostrar que las funciones son objetos eliminamos la referencia original
# del mayusculas

# Aun asi, podemos utilizar la funcion con la variable funcion
print(variable_funcion('Saludos...'))
# print(mayusculas('Ya se elimino...'))

# Podemos saber el nombre por default que se le asigna a una funcion
print(f'Nombre por default de la funcion: {variable_funcion.__name__}') # De esta forma podemos ver que es mayusculas el nombre por default
print(mayusculas('Nombre por default'))

# Como almacenar una funcion en una estructura de datos (list)
lista_funciones = [mayusculas, variable_funcion, str.upper] # Solo estamos la referencia no estamos llamando el metodo
print(lista_funciones)

for funcion in lista_funciones:
    print(funcion, funcion('Saludos desde el bucle for'))

# Podemos acceder directamente a la funcion que deseemos
print(f'Accediendo a la segunda funcion de la lista: {lista_funciones[1]("Saludos desde variable_funcion")}')

############################
# Podemos pasar funciones a otras funciones
# Este tipo de funciones se conocen como higher-order functions

def saludar(argumento_funcion):
    # Usamos la funcion que recibos como argumento y devolvemos la referencia de esta funcion
    referencia_funcion_retornada = argumento_funcion('Hola, Saludos desde mi funcion')
    print(referencia_funcion_retornada)

# Podemos pasar una nueva implementacion de la funcion que pasamos como argumento
def minusculas(texto):
    return texto.lower()

def capitalizar(texto):
    return texto.capitalize()

# Llamamos a la funcion saludar, pasamos la referencia de uan funcion como argumento
saludar(minusculas)

# El clasico ejemplo de higher-order functions es la funcion map
# Esta funcion toma una funcion como referencia y un iterable, llama a la funcion referencia y le aplica en cada
# elmento del iterable proporcionadoe
print(list(map(mayusculas, ['texto1','texto2','texto3']))) # La funcion le afecta a cada uno de los elementos
print(list(map(minusculas,['texto1','texto2','texto3'])))


########################
# Funciones anidadas (Una funcion dentro de otra)

def mostrar(texto):
    # Definicion de la funcion interna o anidada
    def convertir_mayusculas(t):
        return t.upper()
    # Una vez definida la funcion anidada la mandamos a llamar
    return convertir_mayusculas(texto) # Desde aqui devolvemos el texto que recibimos de convertir_mayusculas


# Cada vez que se llama la funcion mostrar
# se crea la funcion anidada convertir_mayusculas
print(mostrar('Desde funcion anidada...'))

# No podemos utilizar la funcion anidada desde fuera de la funcion externa
# convertir_mayusculas('texto1') Esto nos va a dar un error porque es una funcion local
# mostrar.convertir_mayusculas('texto1') Tampoco podemos acceder de esta forma

# Devolver la funcion anidada
# Observar que en ningun momento se llama a la funcion anidada desde la funcion externa
def hablar(volumen):
    def minusculas(texto):
        return texto.lower()
    def mayusculas(texto):
        return texto.upper()
    if volumen >= 0.5:
        return mayusculas
    else:
        return minusculas

# Utilizamos la funcion anidada
print(hablar(0.6)('Estas hablando demasiado alto...')) # Llamamos a la funcion desde fuera
print(hablar(0.4)('Hablo Suave....'))

variable_minusculas = hablar(0.4)
print(f'Usando la funcion anidada desde una variable: {variable_minusculas("Hablo suave Nuevamente...")}')


######################
# Closure
# Las funciones internas pueden capturar y guardar el estado de la funcion externa (padre)
def hablar(texto, volumen):
    # La funcion interna ya no recibe parametros
    # Utiliza el estado de la funcion externa
    def minusculas():
        return texto.lower()
    def mayusculas():
        return texto.upper()
    if volumen >= 0.5:
        return mayusculas() # En este caso ya llamamos a las funciones porque no tienen parametros
    else:
        return minusculas()

print(hablar('Hablo fuerte (desde un closure...)',0.6)) # Se devuelve la funcion mayusculas
print(hablar('Hablo suave (desde un closure...)',0.4)) # Se devuelve la funcion minusculas

# Otro ejemplo de closure
# Podemos preconfigurar una funcion
def mostrar(titulo):
    # Definimos la funcion anidada
    def saludar(mensaje): # Que sea un closure no quiere decir que no pueda recibir otro parametro la funcion anidada
        return titulo + '. ' + mensaje
    return saludar

mostrar_ing = mostrar('Ingeniero')
mostrar_lic = mostrar('Licenciado')


# Podemos seguir usando el estado de la funcion previamente configurada
# aunque el valor de titulo ya esta fuera del alcance (scope out)
print(mostrar_ing('ALvaro Ruiz'))
print(mostrar_lic('Carlos Esparza'))

################################
# La funcion callable nos permite saber si un objeto se puede llamar o no
# Todas las funciones en python son objetos, pero no todas los objetos son funciones
print(f'Se puede llamar el objeto mostrar como funcion: {callable(mostrar)}') # Se pasa la referencia no se llama a la funcion
print(f'Se puede llamar el objeto hablar como funcion: {callable(hablar)}')
print(f'Se puede llamar el objeto mostrar_ing como funcion: {callable(mostrar_ing)}')
print(f'Se puede llamar el objeto str como funcion: {callable("cualquier texto")}') # Esto quiere decir que no se puede llamar a este objeto (str) como una funcion

# Si queremos que una clase defina objetos que se puedan llamar como funciones
# tenemos que sobreescribir el metodo dunder __call__
class Mostrar:
    def __init__(self, titulo):
        self.titulo = titulo

    def __call__(self, mensaje):
        return self.titulo + '. ' + mensaje

mostrar_doc = Mostrar('Doctor')
print(mostrar_doc('Carlos Ugalde'))
print(f'Se puede llamar el objeto mostrar_doc como una funcion: {callable(mostrar_doc)}')

