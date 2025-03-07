# Bool contiene los valores de True y False

# Tipos numericos, False para 0, True demas valores
valor = 0.0
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
valor = 5.00
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

# Tipo str, False para '', True demas valores
valor = ''
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
valor = 'Hola'
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')

# Tipo colecciones, False para colecciones vacias, True para todas las demas colecciones
# Lista
valor = []
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
valor = [1,2,3,4,5]
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# Tupla
valor = ()
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
valor = (1,2,3,4)
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')

# Diccionario
valor = {}
resultado = bool(valor)
# print(f'Valor {valor}, resultado: {resultado}')
valor = {
    'nombre':'diogo',
    'edad':17,
    'altura': 2.00
}
resultado = bool(valor)
# print(f'Valor: {valor}, resultado: {resultado}')


variable = 10
if bool(variable):
    print('Regreso Verdadero')
else:
    print('Regreso falso')

if variable:
    print('Regreso Verdadero')
else:
    print('Regreso falso')

while variable:
    print(f'Ejecucion ciclo while')
    break
else:
    print(f'fin ciclo while')

