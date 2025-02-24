from mysql.connector import pooling # Importamos esta clase para poder crear un pool
from mysql.connector import Error

class Conexion:
    # Esto son constantes por lo cual sus valores no se deben de modificar
    DATABASE = 'zona_fit_db'
    USER = 'root'
    PASSWORD = 'admin'
    HOST = 'localhost'
    DB_PORT = 3306
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtenerPool(cls):
        if cls.pool is None: # Se crea el obtejo pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    user=cls.USER,
                    password=cls.PASSWORD,
                    host=cls.HOST,
                    database=cls.DATABASE

                )
                print(f'Nombre del pool: {cls.pool.pool_name}')
                print(f'Tamanio del pool: {cls.pool.pool_size}')
                return cls.pool
            except Error as error:
                print(f'Ocurrio un error al obtener el pool: {error}, {type(error)}')
        else:
            return cls.pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().get_connection()
        print(f'Se ha obtenido la conexion {conexion} correctamente!')
        return conexion
    @classmethod
    def liberarConexion(cls,conexion):
        conexion.close()
        print(f'Se ha devuelto la conexion {conexion} correctamente!')
