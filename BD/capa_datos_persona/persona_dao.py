from conexion import Conexion
from cursor_del_pool import CursorDelPool
from persona import Persona
from logger_base import log

class PersonaDAO:
    '''
    DAO significa (DATA ACCESS OBJECT)
    CRUD significa (Create-Read-Update-Delete)
    '''

    _SELECT = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERT = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s, %s, %s)'
    _UPDATE = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s'
    _DELETE = "DELETE FROM persona WHERE id_persona = %s"

    # Metodo seleccionar
    @classmethod
    def seleccionar(cls): # Metodo para seleccionar
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas

    @classmethod # Metodo para insertar
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERT, valores)
            log.info(f'Persona insertada: {persona}')
            return cursor.rowcount

    @classmethod # Metodo para actualizar
    def update(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email,persona.id_persona)
            cursor.execute(cls._UPDATE,valores)
            log.info(f'Persona Actualizada: {persona}')
            return cursor.rowcount

    @classmethod # Metodo para eliminar
    def delete(cls, persona):
        with CursorDelPool() as cursor:
            valor = (persona.id_persona,)
            cursor.execute(cls._DELETE,valor)
            log.info(f'Objeto eliminado: {persona}')
            return cursor.rowcount

if __name__ == '__main__':
    # # Eliminar
    # persona = Persona(10)
    # persona_eliminada = PersonaDAO.delete(persona)
    # log.info(f'Persona eliminada: {persona_eliminada}')
    #
    # # Update
    # persona = Persona(21,'Saioa','Adalsaro','saldasoro@gmail.com')
    # persona_actualizada = PersonaDAO.update(persona)
    # log.info(f'Persona actualizada: {persona_actualizada}')
    #
    #
    # Insertar un registro
    # persona1 = Persona(nombre='Pedro',apellido='Najera',email='pnajera@gmail.com')
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f'Personas insertadas: {personas_insertadas}')

    # Seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.info(persona)

