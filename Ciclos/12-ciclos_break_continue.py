print('*** Break y Continue ***')

# Ejemplo con break
print('\nPalabra break:')
for numero in range(1,10): # Basicamente, en el momento que encuentre el primer numero par, con break rompemos el bucle y directamente se para
    if numero % 2 == 0: # numero par
        print(numero)
        break # Salimos del ciclo inmediatamente, se rompe completamente

# Ejemplo con continue
print("\nPalabra continue:")
for numero in range(1,10):
    if numero % 2 == 1: # Numero impar
        continue
    print(numero) # Numeros pares