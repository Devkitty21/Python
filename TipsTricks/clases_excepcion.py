# Vamos a crear una clase para definir una clase de excepcion personalizada
# Ej. Validar que un nombre no pueda tener menos de 3 caracteres

# Este tipo de validacion n o indica cual es el problema en especifico

def validar(nombre_completo):
    if len(nombre_completo) < 3:
        raise ValueError
    else:
        print(f'Validacion correcta...')

nombre = 'Juan'
validar(nombre)
nombre = 'Pi'
# validar(nombre)

# Validacion personalizada, indica cual es el problema, y queda autodocumentado
# class NombreDemasiadoCorto(ValueError):
#     pass
#
# def validar_mejorado(nombre_completo):
#     if len(nombre_completo) < 3:
#         raise NombreDemasiadoCorto(nombre_completo)
#     else:
#         print('Validacion correcta!')
#
# nombre = 'Ka'
# validar_mejorado(nombre)

# Es buena idea crear una clase base y de alli extender las demas clases
class ClaseExcepcionBase(TypeError):
    pass

class NombreDemasiadoCorto(ClaseExcepcionBase):
    pass


def validar_mejorado(nombre_completo):
    if len(nombre_completo) < 3:
        raise NombreDemasiadoCorto(nombre_completo)
    else:
        print('Validacion correcta!')

nombre = 'Ka'
try:
    validar_mejorado(nombre)
except ClaseExcepcionBase as error:
    print(f'{type(error).__name__}, linea: {error.__traceback__.tb_lineno} en {__file__}: {error}')




