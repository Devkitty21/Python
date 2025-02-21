from logger_base import log
from CursorDelPool import CursorDelPool
from conexion import Conexion
from usuario import Usuario

class UsuarioDAO:

    # Definimos las constantes

    _SELECT = 'SELECT * FROM usuarios ORDER BY id_usuario'
    _INSERT = 'INSERT INTO usuarios (username,password) VALUES(%s,%s)'
    _UPDATE = 'UPDATE usuarios SET username=%s, password=%s WHERE id_usuario =%s '
    _DELETE = 'DELETE FROM usuarios WHERE id_usuario = %s'


    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insert(cls,usuario):
        log.debug(f'Usuario a insertar: {usuario}')
        with CursorDelPool() as cursor:
            valores = (usuario.usuario,usuario.password)
            cursor.execute(cls._INSERT,valores)
            return cursor.rowcount

    @classmethod
    def update(cls,usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a actualizar: {usuario}')
            valor = (usuario.usuario,usuario.password,usuario.id_usuario)
            cursor.execute(cls._UPDATE,valor)
            return cursor.rowcount

    @classmethod
    def delete(cls,usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valor_id_usuario = (usuario.id_usuario,)
            cursor.execute(cls._DELETE,valor_id_usuario)
            return cursor.rowcount




if __name__ == '__main__':
    # Seleccionar usuario
    UsuarioDAO.seleccionar()

    # #Insertando un usuario
    # usuario = Usuario(username='Admin',password='test')
    # usuario1 = Usuario(username='Root',password='Root')
    # personas_insertadas = UsuarioDAO.insert(usuario1)
    # log.info(f'Personas insertadas: {personas_insertadas}')

    # Actualizar usuario
    # usuario = Usuario(username='Cat',password='123',id_usuario=4)
    # personas_actualizadas = UsuarioDAO.update(usuario)
    # log.info(f'Persona actualizadas: {personas_actualizadas}')

    # Eliminar usuario
    # usuario = Usuario(id_usuario=6)
    # usuarios_eliminados = UsuarioDAO.delete(usuario)
    # log.info(f'Persona eliminada: {usuarios_eliminados}')