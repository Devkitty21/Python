# Mas de funciones anidadas y alcance de variables

def funcion_externa():
    variable_local_externa = 'Variable local externa'

    # Al momento de terminar esta funcion, automaticamente la variable 'variable_local_anidada' se destruye
    def funcion_anidada():
        variable_local_anidada = 'Variable local anidada'

        # No se crea una nueva variable, trabajamos con la variable mas externa (Es similar a global)

        nonlocal variable_local_externa  # En el caso de que queramos modificar la misma variable sin tener que crear una nueva, usamos nonlocal
        variable_local_externa = 'Nuevo valor de variable local externa'

    funcion_anidada()

    print(f'Valor variable local externa: {variable_local_externa}')
    print(f'Valor variable local anidada: {variable_local_anidada}') # Debido a que estamos fuera de la funcion anidada, no se puede acceder a una variable local mas interna

funcion_externa()