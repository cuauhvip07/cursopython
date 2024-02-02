from Conexion import Conexion;
from Persona import Persona
from loggin import log


class PersonaDAO:
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'
    
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona1 = Persona(registro[0],registro[1],registro[2],registro[3])
                    personas.append(persona1)
                return personas
            
    @classmethod 
    def insertar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre,persona.apellido,persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada con exito: {persona}')
                return cursor.rowcount
            
    @classmethod
    def actualizar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre,persona.apellido,persona.email,persona.idPersona)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug(f'Actualizacion exitosa {persona}')
                return cursor.rowcount
            
    @classmethod
    def eliminar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.idPersona,)
                cursor.execute(cls._ELIMINAR,valores)
                log.debug(f'Eliminado con exito {persona}');
                return cursor.rowcount

if __name__ == '__main__':
    
    # Eliminar
    persona1 = Persona(idPersona = 22);
    personas_eliminadas = PersonaDAO.eliminar(persona1);
    log.debug(f'Eliminados: {personas_eliminadas}')
    
    # #Actualizar
    # persona1 = Persona(nombre='Karime',apellido='Mendez',email='kmendez@mail.com',idPersona='20')
    # personas_actualizadas = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas actualizadas {personas_actualizadas}')
    
    # #Insertar
    # persona1 = Persona(nombre='Gaboriel',apellido='Pedraza',email='gpedraza@mail,com')
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f'Personas insertadas:{personas_insertadas}')
    
    # Seleccionar
    personass = PersonaDAO.seleccionar()
    for persona in personass:
        log.debug(persona)