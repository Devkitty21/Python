import psycopg2 as db
from logger_base import log
import sys
from psycopg2 import pool

# Pool de conexiones o conjunto de conexiones es lo mismo

class Conexion:
    # Definimos las constantes de la clase de forma privada
    # Estas variables no se deben de modificar a no ser que vayamos a cambiar de base de datos
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    #Configuracion de pool
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON,
                                                      host= cls._HOST,
                                                      port=cls._DB_PORT,
                                                      user = cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      dbname = cls._DATABASE
                                                      )
                log.info(f'Se ha creado el pool correctamente: {cls._pool}')
                return cls._pool
            except Exception as error:
                log.error(f'Se ha captado un error: {error}')
                sys.exit()
        else:
            return cls._pool


    # Metodo para obtener una conexion del pool
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.info(f'Conexion obtenida del pool: {conexion}')
        return conexion

#     Metodo para liberar una conexion
    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.info(f'Se ha devuelvo la conexion al pull: {conexion}')

    # Metodo para cerrar todas las conexiones
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        log.info(f'Se ha cerrado correctamente el pool')

if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    # conexion6 = Conexion.obtenerConexion() Esto indicara error porque el maximo de conexiones en el pool son 5
