# Profundizando en tuplas

# Las tuplas son inmutables

# Declarar variables
a,b = 'Hola','Adios' # Unpacking
print(a,b)

# Swap (intercambio)
a,b = b,a # Intercambiamos los valores
print(f'Valores intercambiados: {a} {b}')

# Regresar multiples valores en una funcion
def minmax(elementos):
    return min(elementos), max(elementos)

elementos = [1,2,3,4,5]
min, max = minmax(elementos) # Tambien se puede pasar la lista directamente en vez de pasar el argumento elementos
print(f'Valor Minimo: {min}, Valor Maximo: {max}')

# Regresar la suma de una tupla
# Cualquiera de estas dos opciones es valida
resultado = sum((range(1,6)))
print(f'Resultado: {resultado}')

def sumar(*args):
    return sum(args)

resultado = sumar(1,2,3,4,5)
print(f'Resultado: {resultado}')
