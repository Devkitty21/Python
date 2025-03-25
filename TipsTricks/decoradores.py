# 1. Definimos el decorador que va a recibir como parametro una funcion
# 2. Definimos una funcion
# 3. Hace return de la funcion con sus cambios respectivos

# Los decoradores permiten extender y modificar el comportamiento de las funciones
# Ejemplos comunes: logging, seguridad, caching
# Un decorador es codigo reutilizable

# Primer ejemplo de un decorador

def decorador_envolvente(funcion_a_decorar):
    # Recibir la funcion y regresearla
    print('Estamos dentro de la funcion decoradora')
    return funcion_a_decorar

# Ahora utilizamos el decorador

def saludar():
    return 'Saludos desde mi funcion...'

# Hacemos una llamda manual a este decorador (No es lo comun usar los decoradores asi)
funcion_retornada = decorador_envolvente(saludar)
print(funcion_retornada)

@decorador_envolvente
def saludar_funcion_a_decorar():
    return 'Saludos desde decorador_envolvente a vosotros'

print(saludar_funcion_a_decorar())

# Prueba de DevKitty -> Ejemplo 1
# Creamos el decorador
def mi_decorador(funcion_a_decorar): # Parametro -> Una funcion que definimos mas tarde
    def funcion_modificada(): # -> Closure
        print('Entrando en la modificacion')
        funcion_a_decorar()
        print('Saliendo de la modificacion')
    return funcion_modificada

@mi_decorador
def saludar():
    print('La universidad python es lo mejor')

saludar()

# Decorador que convierte el texto a mayusculas

def mayusculas(funcion_a_decorar):
    def envolvente():
        print('Antes de la llamada a la funcion de decorar...')
        # Mandamos a llamar la funcion original (closure)
        resultado_original = funcion_a_decorar()
        print('Despues de la llamada a la funcion a decorar...')
        resultado_modificado = resultado_original.upper()
        return resultado_modificado
    return envolvente

@mayusculas
def saludar_minusculas():
     print('hola...')  # Antes de la llamada a la funcion de decorar
     return 'hola...' # Despues de la llamada a la funcion de decorar

print(saludar_minusculas())

###############################
# Uso de Decoradores Multiples
# <strong><em>Hola</em></strong>

def negritas(funcion):
    def funcion_envolvente():
        return '<strong>' + funcion() + '</strong>'
    return funcion_envolvente

def enfatizar(funcion):
    def enfatizado():
        return '<em>' + funcion() + '</em>'
    return enfatizado

@negritas # Los decoradores se ejecutan de abajo hacia arriba
@enfatizar # Tambien conocido como From bottom to top = De abajo hacia arriba
def saludar_html():
    return 'Hola con HTML'

print(saludar_html())

########################
# Decoradores con argumentos
# *args y ##kwargs (Argumentos de tipo tupla y de tipo diccionarios)

def decorador_con_argumentos(funcion):
    def funcion_envolvente(*args, **kwargs):
        print('Se esta ejecutando decorador')
        print('args:',args)
        print('kwargs:',kwargs)
        # Modificar los argumentos antes de enviarlos
        lista_arg = []
        for indice, valor_tupla in enumerate(args):
            lista_arg.append(args[indice].upper())
        # Agregamos mas elementos a la lista
        lista_arg.append('nuevo argumento 1')
        lista_arg.append('nuevo argumento 2')
        # Agregamos informacion al diccionario
        kwargs['key1'] = 'Nuevo valor 1'
        kwargs['key2'] = 'Nuevo valor 2'
        # Propagamos los parametros a la funcion original
        # return funcion(*args, **kwargs)
        # Propagar los valores modificados
        return funcion(*lista_arg, **kwargs)
    return funcion_envolvente

@decorador_con_argumentos
def funcion_saludar(titulo, nombre,*args, **kwargs):
    # Imprimir titulo con el nombre
    print(f'{titulo}. {nombre}')
    # Imprimos los argumentos variables
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')

funcion_saludar('Ingeniero','Ubaldo Acosta')


