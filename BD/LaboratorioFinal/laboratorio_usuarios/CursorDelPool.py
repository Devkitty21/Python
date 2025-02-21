from logger_base import log
from conexion import Conexion

class CursorDelPool:

    def __init__(self):
        self._conexion = None
        self._cursor = None


    def __enter__(self):
        if self._cursor is None:
                self._conexion = Conexion.obtenerConexion()
                self._cursor = self._conexion.cursor()
                return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        if valor_excepcion:
            self._conexion.rollback()
            log.error(f'Se ha producido un error en la transaccion, rollback en proceso: {tipo_excepcion},{valor_excepcion},{detalle_excepcion}')

        else:
            self._conexion.commit()
            log.info('Se ha hecho commit de la transaccion')
            self._cursor.close()
            Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.info('Dentro del bloque with')
        cursor.execute('SELECT * FROM usuarios')
        log.info(cursor.fetchall())