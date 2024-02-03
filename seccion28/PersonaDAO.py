from Conexion import Conexion
from Persona import Persona
from loggin import log
from CursorPool import CursorPool

class PersonaDAO:
    '''
    DAO (Data Access Object)
    '''
    
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona';
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s'
    _ELIINAR = 'DELETE FROM persona WHERE id_persona = %s';
    
    
    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls,persona):
        with CursorPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls,persona):
        with CursorPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'Persona Actualizada {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls,persona):
        with CursorPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIINAR,valores)
            log.debug(f'Objeto eliminado {persona}')
            return cursor.rowcount





if __name__ == '__main__':
    
    #Eliminar
    persona1 = Persona(id_persona=23);
    persona_eliminada = PersonaDAO.eliminar(persona1);
    log.debug(f'Personas eliminadas {persona_eliminada}');
    
    # # Actualizar un registro
    # persona1 = Persona(nombre='Alejandrina',apellido='Poli',email='apoli@mail.com',id_persona='23')
    # personas_actualizadas = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas actualizadas {personas_actualizadas}')
    
    # # Insertar un registro
    # persona1 = Persona(nombre='Alejandra',apellido='Tellez',email='atellez@mail.com')
    # personas_insertdas = PersonaDAO.insertar(persona1)
    # log.debug(f'Personas insertadas: {personas_insertdas}')
    
    
    # Seleccionar
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)