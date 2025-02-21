from UsuarioDAO import UsuarioDAO
from usuario import Usuario
from logger_base import log
from CursorDelPool import CursorDelPool
import sys

while True:
    print('\nMenu principal'.center(30, '-'))
    print(f"""1.) Listar usuarios
2.) Agregar usuarios
3.) Actualizar usuarios
4.) Eliminar usuarios
5.) Salir""")

    opcion = int(input('[+] Introduce una opcion (1-5): '))

    if opcion == 1:
        with CursorDelPool() as cursor:
            try:
                usuarios = UsuarioDAO.seleccionar()
                for usuario in usuarios:
                    log.info(usuario)
            except Exception as error:
                log.error(f'Se ha producido un error: {error}, {type(error)}')

    elif opcion == 2:
        usuario_var = input('Introduce el nombre del usuario: ')
        password_var = input('Introduce la password del usuario: ')
        usuario = Usuario(username=usuario_var, password=password_var)
        usuario_insertados = UsuarioDAO.insert(usuario)
        log.info(f'Usuario insertados = {usuario_insertados}')

    elif opcion == 3:
        usuario_var = input('Escribe el nuevo usuario: ')
        password_var = input('Escribe la password nueva: ')
        id_persona_var = input('Introduce el id de la persona donde quieres que se apliquen los cambios: ')
        usuario = Usuario(id_usuario=id_persona_var,username=usuario_var,password=password_var)
        usuarios_actualizados = UsuarioDAO.update(usuario)
        log.info(f'Usuarios actualizados: {usuarios_actualizados}')

    elif opcion == 4:
        id_persona_var = input('Introduce el id de la persona que quieres eliminar: ')
        usuario = Usuario(id_usuario=id_persona_var)
        usuarios_eliminados = UsuarioDAO.delete(usuario)
        log.info(f'Usuario eliminados: {usuarios_eliminados}')

    elif opcion == 5:
        log.debug('Saliendo del sistema... Hasta la proxima!')
        sys.exit()
    else:
        print(f'La opcion {opcion} no es correcta!')
