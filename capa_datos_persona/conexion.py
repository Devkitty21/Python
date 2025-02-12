import psycopg2 as db
from logger_base import log
import sys

class Conexion:
    # Definimos las constantes de la clase de forma privada
    # Estas variables no se deben de modificar a no ser que vayamos a cambiar de base de datos
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    # Metodo para la conexion a la base de datos
    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                # Hacemos la conexion con la base de datos usando los atributos de clase
                cls._conexion = db.connect(host=cls._HOST,
                                           port=cls._DB_PORT,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           database=cls._DATABASE)

                log.info(f'Conexion Existosa: {cls._conexion}')
                return cls._conexion

            except Exception as error:
                log.error(f'Ocurrio un error al obtener la conexion: {error}')
                sys.exit()
        else:
            return cls._conexion

    # Metodo para la creacion/obtencion del cursor
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.info(f'Se ha abierto correctamente el cursor: {cls._cursor}')
                return cls._cursor

            except Exception as error:
                log.error(f'Error a la hora de obtener el cursor: {error}')
                sys.exit()
        else:
            return cls._cursor

#     Cerrar conexion a la base de datos
    @classmethod
    def cerrarConexion(cls):
        try:
            cls.obtenerConexion().close()
            log.info(f'La conexion se ha cerrado con exito: {cls._conexion}')

        except Exception as error:
            log.error(f'Ha ocurrido un error al cerrar la conexion: {error}')

    @classmethod
    def cerrarCursor(cls):
        try:
            cls.obtenerCursor().close()
            log.info(f'El cursor se ha cerrado con exito: {cls.obtenerCursor()}')

        except Exception as error:
            log.error(f'Se ha producido un error a la hora de cerrar el cursor: {error}')
if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()