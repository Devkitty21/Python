from Excepciones.NumerosIdenticosException import NumerosIdenticosException
resultado = None
try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))

    if a == b:
        raise NumerosIdenticosException('Numeros Identicos')
    resultado = a/b

except ZeroDivisionError as e: # Importante usar Exception por que asi podemos hacer catch de todos los tipos de errores
    print(f'ZeroDivisionError: Ocurrio un error: {e}, {type(e)}')
except TypeError as e:
    print(f'TypeError: Ocurrio un error: {e}, {type(e)}')
except Exception as e:
    print(f'Exception: Ocurrio un error: {e}, {type(e)}') # La clase con mas jerarquia en este caso debe ir mas abajo que las clases mas especificas, sino, no se ejecutan los errores especificos

else:
    print('No se ha encontrado ninguna excepcion')
finally:
    print('Ejecucion del bloque finally')

print(f'Resultado de la division: {resultado}')
print('Continuamos...')

