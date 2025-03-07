import math
from decimal import Decimal

# NaN - Not a number (no es un numero)
# NaN no es sensible a mayusculas/minusculas
# NaN es un tipo de dato numerico indefinido
a = float('NaN')
# print(f'a: {a}')
# print(f'Es NaN (not a number)?: {math.isnan(a)}')

# Modulo decimal
a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN (not a number)?: {math.isnan(a)}')
