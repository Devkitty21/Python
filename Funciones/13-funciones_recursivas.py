print('*** Imprimir del 1 al 5 de forma recursiva ***')

# Definir nuestra funcion recursiva

def funcion_recursiva(numero):
    # Caso base
    if numero == 1:
        print(numero, end= " ") # 1
    else: # Caso recursivo
        print(numero, end=' ')
        funcion_recursiva(numero - 1)


# Programa principal
funcion_recursiva(5)
