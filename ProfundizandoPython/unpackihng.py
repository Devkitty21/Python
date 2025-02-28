# Unpacking - Desempaquetado

# valores = 1,2,3
# print(valores)
# print(type(valores))
# valor1, valor2, valor3 = 1,2,3
# print(valor1, valor2, valor3)
#
# valor1, _, valor3 = 1,2,3 # No nos interesa el valor 2 por lo que no se toma en cuenta y se pone un _
# print(valor1, valor3)
#
# valor1, valor2, *valor3 =  1, 2, 3, 4, 5, 6, 7, 8, 9 # Asignamos los valores restantes a la variable valor3 como si fuera el metodo *args
# print(valor1,valor2, valor3)
#
#
# valor1, valor2, *valor3, valor4, valor5 =  1, 2, 3, 4, 5, 6, 7, 8, 9  # Asignamos los valores restantes a la variable valor3 como si fuera el metodo *args
# print(valor1,valor2, valor3, valor4, valor5)
# print(type(valor3))
#
# valor1, valor2, *valor3, valor4, valor5 =  [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(valor1,valor2, valor3, valor4, valor5)
# print(type(valor3))
#
# def regresa_varios_datos():
#     return 1,2,3 # Esto devuelve una tupla
#
# valor1, *valores_restantes = regresa_varios_datos() # Simplemente le agregamos el 1 a la variable valor1 y los demas no nos interesan por lo cual se pone * y una _ como nombre de la variable
# print(valor1, valores_restantes)

# help(str.partition)

hora,separador,minutos = '17:20'.partition(':')
# print(type(variable))
print(hora,separador,minutos)
