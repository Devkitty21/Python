from psycopg2 import pool
from logger_base import log
import sys

class Conexion:

    # Definimos las constantes

    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _POOL = None


    # Metodo para crear una pool

    @classmethod
    def obtenerPool(cls):
        if cls._POOL is None:
            try:
                cls._POOL = pool.SimpleConnectionPool(dbname=cls._DATABASE,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      host=cls._HOST,
                                                      maxconn=cls._MAX_CON,
                                                      minconn=cls._MIN_CON)
                log.debug(cls._POOL)
                return cls._POOL
            except Exception as error:
                log.error(f'Se ha producido un error: {error} {type(error)}')
                sys.exit()
        else:
            return cls._POOL

    # Metodo para obtener una conexion del pool
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.info(f'Se ha obtenido la conexion del pool: {conexion}')
        return conexion

    # Metodo para liberar conexion
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.info(f'La conexion se ha devuelto al pool correctamente: {conexion}')

    # Metodo para cerrar conexion
    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()
        log.debug(f'Se han cerrado todas las conexiones correctamente')



if __name__ == '__main__':
    Conexion.obtenerPool()
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    Conexion.cerrarConexion()
