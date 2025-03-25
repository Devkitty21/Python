from contextlib import contextmanager

with open('prueba.txt','w') as archivo:
   archivo.write('Hola desde Python')
   # Se cierra de manera automatica

# Esto es equivalente a:
# archivo = open('prueba.txt','w')
# try:
#     archivo.write('Hola desde Python')
# finally:
#     archivo.close()


# Esto NO es equivalente
archivo = open('prueba.txt','w')
archivo.write('Hola sin with')
# Esto no asegura el cierre de recursos en caso de error
archivo.close()

# Manejo de Context Manager en Clases
# 1. Implementando el protocolo con las funciones (__enter__) y (__exit__)
# 2.Utilizando la libreria de contextlib

# Veamos la opcion1
class ManejoArchivos():
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Entrando en la funcion de __enter__')
        self.archivo = open(self.nombre, 'w')
        return self.archivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Entrando a la funcion __exit__')
        if self.archivo: # Si self.archivo no tiene el valor de None
            self.archivo.close()


# Este metodo es un generador, en primer lugar adqiere el recurso
# posteriormente suspende temporalmente la ejecucion al utilizar yield
# cuando termina de ser utilizado este metodo, regresa a la ejecucion y cierra el recurso que se ha utilizado

# 2. Utilizando la libreira de contextlib
@contextmanager
def manejador_archivos(nombre_archivo):
    try:
        archivo = open(nombre_archivo, 'w')
        yield archivo
    finally:
        archivo.close()

# Ejercicio de identador
class Identador:
    def __init__(self):
        self.nivel = 0

    def __enter__(self):
        self.nivel += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.nivel -= 1
        return self

    def imprimir(self, texto):
        print(f'{"    " * self.nivel}{texto}')


# Mismo ejercicio identador pero con context lib]
class Identador2():
    def __init__(self):
        self.nivel = 0

    @contextmanager
    def identador(self):
        try:
            self.nivel += 1
            yield self
        finally:
            self.nivel -= 1

    def imprimir(self, texto):
        print('  '* self.nivel + texto)


# Prueba

if __name__ == '__main__':
    # Prueba implementando el protocolo de ContextManage
    with ManejoArchivos('prueba.txt') as archivo:
        archivo.write('Prueba desde Manejo archivo')

    # Prueba con la libreria contextlib
    with manejador_archivos('prueba.txt') as archivo:
        archivo.write('prueba desde decorador')
        archivo.write('\nadios')

    # Prueba de identador
    with Identador() as identador:
        identador.imprimir('primer nivel')
        with identador:
            identador.imprimir('segundo nivel ')
            identador.imprimir('continua segundo nivel')
            with identador:
                identador.imprimir('tercer nivel')
                identador.imprimir('continua tercer nivel')
        identador.imprimir('Fin primer nivel')

        print('\n')
        objeto = Identador2()
        with objeto.identador():
            objeto.imprimir('primer nivel')
            objeto.imprimir('Continau primer nivel')
            with objeto.identador():
                objeto.imprimir('segundo nivel')
                objeto.imprimir('Continua segundo nivel')




