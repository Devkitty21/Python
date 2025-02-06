# Revisar si una variable se encuentra dentro de rango

dato = int(input('Proporciona un dato: '))

# Revisamos si esta dentro de un rango

# esta_dentro_rango = 1 <= dato <= 10
# print(f'Variable esta dentro de rango (entre 1 y 10): {esta_dentro_rango}')

# Revisamos la logica inversa para ver si el dato esta fuera de rango

esta_fuera_rango = not(1 <= dato <= 10)

print(f'Variable esta fuera de rango: {esta_fuera_rango}')