print(f'*** Alcance de Variables ***')

# Variable global
contador_global = 0

def incrementar_contador():
    contador_local = 0 # Solo puede ser usada detro de la funcion es una variable local.
    global contador_global
    contador_global += 1
    contador_local += 1

    # Imprimos = ambos contandores

    print(f'Conatdo local: {contador_local}')
    print(f'Contador global: {contador_global}\n')

# Llamamos varias veces a la fuincion

# llamamos al contador
incrementar_contador()
incrementar_contador()
incrementar_contador()

# Terminando el programa
print(f'El valor de la variable global es: {contador_global}')
