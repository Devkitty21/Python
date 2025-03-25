# Diferencia entre variables de clase y de instancia (objeto)

class Perro:
    numero_patas = 4 # Variable de clase

    def __init__(self,nombre):
        self.nombre = nombre # <- Variable de instancia

# Definimos algunos objetos
layla = Perro('Layla')
venus = Perro('Venus')
# Cada objeto tiene su propio atributo de nombre
print(layla.nombre, venus.nombre)

# La variable se puede acceder con el nombre de la clase o con los objetos
print(layla.numero_patas, venus.numero_patas, Perro.numero_patas) # En todos los casos estamos accediendo al mismo valor

# Si tratamos de acceder la variable de instancia desde la clase no es posible
# print(Perro.nombre) # Esto solo es parte de los objetos que se van a crear para esta clase

# Si queremos modificar el numero_patas para todos los perros
Perro.numero_patas = 5
print(layla.numero_patas, venus.numero_patas, Perro.numero_patas)

# Si queremos modificar el numero_patas para un solo perro
venus.numero_patas = 6 # Se crea una variable de instancia y por eso oculta a la variable de clase
print(layla.numero_patas, venus.numero_patas, Perro.numero_patas)

# Imprimimos el valor de la variable de instancia y ademas la variable de clase
print(venus.numero_patas, venus.__class__.numero_patas)

# Si creamos una variable desde clase
Perro.nombre = 'Clase Perro' # Esta variable se asigna al vuelo
print(layla.nombre, venus.nombre, Perro.nombre) # Las variables de los objetos toman mas valor que los valores de clase por lo cual se ocultan

# Si definimos una variable de clase que no esta en los objetos
Perro.numero_orejas = 2
print(layla.numero_orejas, venus.numero_orejas, Perro.numero_orejas)