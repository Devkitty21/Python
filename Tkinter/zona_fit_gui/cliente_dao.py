
from conexion import Conexion
from cliente import Cliente

class ClienteDAO:

    SELECCIONAR = 'SELECT * FROM cliente'
    INSERTAR = 'INSERT INTO cliente(nombre,apellido,membresia) VALUES(%s,%s,%s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre = %s, apellido = %s, membresia = %s WHERE id = %s'
    ELIMINAR = 'DELETE FROM cliente WHERE id =%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0],registro[1],registro[2],registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as error:
            print(f'Ha sucedido un error, {error}, {type(error)}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberarConexion(conexion)

    @classmethod
    def insertar(cls,cliente):
        conexion =None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre ,cliente.apellido,cliente.membresia)
            cursor.execute(cls.INSERTAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as error:
            print(f'Ha ocurrido un error: {error}, {type(error)}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberarConexion(conexion)

    @classmethod
    def actualizar(cls,cliente):
        conexion = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre,cliente.apellido,cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR,valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as error:
            print(f'Ha ocurrido un error: {error}, {type(error)}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberarConexion(conexion)

    @classmethod
    def eliminar(cls,cliente):
        conexion = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = conexion.cursor()
            valor = (cliente.id,)
            cursor.execute(cls.ELIMINAR,valor)
            conexion.commit()
            return cursor.rowcount
        except Exception as error:
            print(f'Ha ocurrido un error: {error}, {type(error)}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberarConexion(conexion)


if __name__ == '__main__':
    # Eliminar cliente

    # cliente1 = Cliente(id='8')
    # clientes_eliminados = ClienteDAO.eliminar(cliente1)
    # print(f'Clientes eliminados: {clientes_eliminados}')

    # Actualizar un cliente

    # cliente1 = Cliente(id=8,nombre='Paulo',apellido='Vieira',membresia='150')
    # clientes_actualizados = ClienteDAO.actualizar(cliente1)
    # print(f'Clientes actualizados: {clientes_actualizados}')



    # Insertar un cliente

    # cliente1 = Cliente(nombre='Oier',apellido='Davila',membresia="12")
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')


    # Seleccionar los clientes

    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)