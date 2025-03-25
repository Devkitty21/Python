# Tip. Las aserciones nos pueden ayudar a depurar nuestros programas de errores
# que no nos podemos recuperar

# Ejemplo 1. Revisamos si la division es entre 0
def dividir(a,b):
    # Nos aseguramos que el valor de b no es cero para poder continuar
    assert b != 0, 'Division entre cero' # El mensaje es opcional pero sera parte cuando se mande la excepcion
    print(f'Resultado division: {a/b}')

# Ejemplo 2. Realizamos el calculo del promedio de una lista de calificaciones

def obtener_promedio(calificaciones):
    # Si la lista de calificaciones esta vacia no deberia continuar el programa
    assert len(calificaciones) != 0, 'Lista de calificaciones vacia'
    print(f'El promedio de calificaciones es: {sum(calificaciones)/len(calificaciones)}')


# Ejemplo 3. Realizamos un descuento al producto proporcionado
def aplicar_descuento(productos, descuento):
    precio_con_descuento = productos['precio'] * (1.0-descuento)
    print(f'Nuevo Precio del producto: {precio_con_descuento:.2f}')
    assert 0<= precio_con_descuento <= productos['precio'], f'Descuento Invalido {precio_con_descuento:.2f}'
    print('Descuento Valido')

# Ejemplo 4. Comprobamos si el divisior no es un numero
def password(password):
    assert 8>= len(password), 'Password demasiado larga'
    print(f'Password valida: {password}')



if __name__ == '__main__':
    # Prueba Ejemplo 1. Division entre 0
    dividir(10,2)
    # Prueba Ejemplo 2. Calculo del promedio de calificaciones
    calificaciones = [10,8,7,9]
    # calificaciones = []
    obtener_promedio(calificaciones)
    # Prueba Ejemplo 3. Aplicar descuento a un producto
    producto = {
        'nombre':'Camisa',
        'precio':1500
    }
    # aplicar_descuento(producto, 1.50)
    aplicar_descuento(producto, 0.50)
    # Ejemplo 4. Contraseña muy larga
    # password('hola12345') Error
    password('hola1234')
