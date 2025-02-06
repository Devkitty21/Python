print(f'*** Convertidor de temperaturas ***')

def convertir_fahrenheit(grados):
    return (grados * 1.8) + 32

    # conversor_fahrenheit = (grados * 1.8) + 32
    # return conversor_fahrenheit
# Se puede hacer direcamente return (grados * 1.8) + 32

def convertir_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8

#     conversor_celsius = (fahrenheit - 32) / 1.8
#     return conversor_celsius
# Se puede hacer directamente return (fahrenheit - 32) / 1.8

# Definicion de los imputs

grados = float(input('\nIntroduce la temperatura en grados: '))
fahrenheit = float(input('Introduce la temperatura en fahrenheit: '))

print(f'\n{grados} C en F son: {convertir_fahrenheit(grados):.2f}')
print(f'\n{fahrenheit} F en C son: {convertir_celsius(fahrenheit):.2f}')