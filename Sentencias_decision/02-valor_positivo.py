print(f'**** Revision de valor positivo ***')

numero = int(input('Proporciona un numero: '))

if numero > 0:
    print(f"Es un numero positivo {numero}")
elif numero < 0:
    print(f'Es un numero negativo {numero}')
else:
    print(f'Es cero {numero}')