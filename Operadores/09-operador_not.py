print("*** Operador logico NOT ***")
condicion1 = True
resultado = not condicion1 # Cada vez que usamos not es como decir si mi condicion es True, con not estoy diciendo que mi condicion no es verdadera not True
print(f'Al aplicar not sobre {condicion1}: {resultado}')

# Revisar si una variable es cadena vacia

nombre = ""
es_cadena_vacia = not nombre
print(f"\nLa variable no tiene ningun valor: {es_cadena_vacia}")

# Revisar si una variable no tiene ningun valor asignado

variable = None
es_variable_sin_valor = not variable
print(f'\nLa variable no tiene ningun valor asignado: {es_variable_sin_valor}')