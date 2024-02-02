import psycopg2
from loggin import log
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'root'
    _PORT = '5432'
    _HOST = 'localhost'
    _conexion = None;
    _cursor = None;
    
    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = psycopg2.connect(
                user=cls._USERNAME,
                password=cls._PASSWORD,
                port=cls._PORT,
                host=cls._HOST,
                database=cls._DATABASE
                )
                log.debug(f'Base de datos conectada')
                return cls._conexion
            except Exception as e:
                log.error(f'Error conexion a la base de datos{e}')
                sys.exit()
        else:
            return cls._conexion
        
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Cursor conectado con exito {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Error al conectar cursor {e}')
                sys.exit()
        else:
            return cls._cursor
        
        
if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()