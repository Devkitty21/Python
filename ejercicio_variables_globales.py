# Definir una variable global


contador = 0


def mostrar_contador():
    print(f'Valor del contador: {contador}')

def modificar_contador(c):
    global contador # Agregamos el global contador, porque como lo estamos modificando es necesario agregarlo, si simplemente lo vamos a leer no es necesario
    contador = c # En el caso de que no se agrege 'global contador' lo unico que estamos haciendo es crear otra variable local llamada contador

modificar_contador(10)
mostrar_contador()