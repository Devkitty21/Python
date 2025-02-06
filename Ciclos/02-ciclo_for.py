print('*** Ciclo FOR ***')

print('Recorremos los caracteres de una cadena')
cadena = 'Hola mundo'

# Iteramos/recorremos cada uno de los caracteres

for letra in cadena:
    print(letra, end=' ')

print('\n\nRecorremos la lista de frutas')

frutas = ['Platano','Fresa','Mango']

for fruta in frutas:
    print(fruta, end=' ')

numeros = [1,2,3,4,5]
resultado = []
for numero in numeros:
    if numero % 2 == 0:
        resultado.append(numero ** 2)
    else:
        resultado.append(numero * 2)

print(resultado)