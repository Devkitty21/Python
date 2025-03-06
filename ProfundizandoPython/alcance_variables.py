# Alcance de variables (scope)

var_global = 'Variable Global'

def imprimir():
    global var_global # Si solamente es para leer, no hace falta agregar global var_global, en el caso de que fueramos a trabajar con ella y a modificar esta variable si que hay que usar la palabra reservada global
    # Acceder a una variable global
    print(f'Variable global desde una funcion: {var_global}')
    # Definicion de variable local
    var_local = 'Variable Local' # Esta variable solo se puede usar en este bloque en este caso
    print(f'Variable local desde una funcion: {var_local}')
    var_global = 'Nuevo valor de la variable global'

    # Las variables locales si que se pueden usar dentro de las funciones anidadas
    def funcion_anidada():
        print(f'Variable local desde una funcion anidada: {var_local}')

#   Llamamos a la funcion anidada
    funcion_anidada()


# Aqui fuera ya no podemos llamar a la varible local
# var_local

imprimir()
print(f'Variable global fuera de la funcion: {var_global}')
# No es posible acceder a variables locales fuera del bloque donde se definieron
# print(f'Var local fuera de la funcion: {var_local}')