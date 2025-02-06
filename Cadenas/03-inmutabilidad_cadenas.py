# Inmutabilidad en cadenas

cadena1 = 'Hola Mundo'
# cadena1[0] = "h" No podemos modificar ninguno de esos elementos y nos dara un error de "TypeError"
cadena2 = cadena1
cadena3 = cadena2
cadena1 = "Adios"
print(cadena1)
print(cadena3)

