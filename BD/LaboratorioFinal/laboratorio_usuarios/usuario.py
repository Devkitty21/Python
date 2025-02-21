from logger_base import log

class Usuario:

    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario
        self._username = username  # Cambiado a atributo privado
        self._password = password  # Usar atributo privado directamente

    def __str__(self):
        return f'Usuario: {self._id_usuario}, {self._username}, {self._password}'

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def usuario(self):
        return self._username

    @usuario.setter
    def usuario(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password


if __name__ == '__main__':
    usuario = Usuario(username='Diogo', password='123')
    log.info(usuario)
    usuario2 = Usuario(id_usuario=1,username='Saioa',password='Aldasoro')
    log.info(usuario2)