# Funciones lambda
# Son funciones anonimas (no tienen un nombre asignado), y son pequeñas (una linea de codigo)

# No es posible asignar una funcion a una variable (Refiriendonos a la sintaxis mostrada)
# mi_funcion = def sumar(a,b): return a + b

# Con una funcion lambda la funcion es anonima (sin nombre) y una sola linea de codigo
# No se necesita agregar parentesis para los parametros
# No se necesita usar la palabra return, pero si debe regresar una expression valida

mi_funcion_lambda = lambda a,b : a+b  # Se devuelve lo que esta despues de :, no hace falta usar la palabra return
resultado = mi_funcion_lambda(4,6)
print(f'Resultado de sumar con funcion lambda: {resultado}')

# Funcion lambda que no recibe argumentos (debe devolver una expression valida)
mi_funcion_lambda = lambda : 'Funcion sin argumentos'
print(f'Llamar funcion lambda sin argumentos: {mi_funcion_lambda()}')

# Funcion lambda con parametros por default
mi_funcion_lambda = lambda a=2, b=3: a+b
print(f'Resultado argumentos por default: {mi_funcion_lambda()}') # De manera opcional podemos pasar valores o no

# Funcion lambda con argumentos variables *args y **kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Resultado de argumentos variables: {mi_funcion_lambda(1,2,3,a=5,b=6)}')

# Funciones lambda con argumentos, argumentos variables y valores por default
mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado de la funcion lambda: {mi_funcion_lambda(1,2,4,5,6,7,e=5,f=7)}')