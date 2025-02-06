print(f'*** Potencia de un Numero usando funciones recursivas ***')

def potencia_recursiva(base, potencia):
    # Caso base
    if potencia == 0:
        return 1
    else: # Caso recursivo
        return base * potencia_recursiva(base, potencia - 1)

print(potencia_recursiva(2,3))


print(f'2 Elevado a la 3 es: {potencia_recursiva(2,3)}')
print(f'2 Elevado a la 5 es: {potencia_recursiva(2,5)}')
print(f'5 Elevado a 0 es: {potencia_recursiva(5,0)}')