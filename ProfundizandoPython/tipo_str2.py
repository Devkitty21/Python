# Profundizando en el tipo str

# Multiplicacion str
# resultado = 3 * 'Hola'
# print(f'Resultado: {resultado}')

# Multiplicacion de tuplas
# resultado = 5 * ('Hola', 10)
# print(f'Resultado: {resultado}')

# Multiplicacion de listas
# resultado = 10 * [0]
# print(f'Resultado: {resultado}, largo: {len(resultado)}')

# Caracteres de escape
# resultado = 'Hola \' Mundo'
# print(f'Resutaldo: {resultado}')

# resultado = 'Se va a eliminar el punto.\b'
# print(f'Resultado: {resultado}')

# Caracter de \
# resultado = 'c:\\directorio\\juan'
# print(f'Resultado: {resultado}')

# raw string
# resultado = r'Cadena con \n salto de linea' # Si ponemos una r los caracteres de \ se procesan de una manera como si fueran parte de la cadena de texto
# print(f'Resultado: {resultado}')

# ruta con raw string
# resultado = r'c:\directorio\juan'
# print(f'Resultado: {resultado}')

# Caracteres unicode
# print('Hola\u0020Mundo')
# print(f'Notacion simple:', '\u0041') # Con \u indicamos la unidad de escape para unicode
# print(f'Notacion extendida:','\U00000041') # Es lo mismo pero la notacion extendida (8 Dijitos)
# print(f'Notacion hexadecimal:','\x41') # La misma letra con notacion hexadecimal
# print(f'Corazon:','\u2665') # Imprimimos un corazon
# print(f'Cara Sonriendo:','\U0001f600') # En la notacion extendida la U debe ser mayuscula
# print(f'Serpiente:','\U0001F40D')

# Caracteres ASCII
# caracter = chr(65)
# print(f'A mayuscula: {caracter}')
# caracter = chr(64)
# print(f'Simbolo @: {caracter}')
# caracter = chr(97)
# print(f'a minuscula: {caracter}')

# Caracteres Bytes
caracteres_en_bytes = b'Hola Mundo' # Hay que poner la b antes para indicar que es una literal en bytes
print(caracteres_en_bytes)
print(f'H en byte: {caracteres_en_bytes[0]}')

mensaje = b'Universidad Python'
print(f'La letra {chr(mensaje[1])} en byte es: {mensaje[1]}')

lista_caracteres = mensaje.split()
print(lista_caracteres) # Son literales de tipo byte, no de tipo unicode


# Convertir de str a bytes
string = 'Programación con Python'
print(f'String original:',string)

# Conversion
bytes = string.encode('UTF-8')
print(f'Bytes codificado:',bytes)

# Convertir bytes a str
string2 = bytes.decode('UTF-8')
print(f'Mensaje decodificado: {string2}')
print(string == string2)