from loggin import log
import psycopg2 as bd
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'root'
    _PORT = '5432'
    _HOST = 'localhost'
    _conexion = None;
    _cursor = None
    
    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._PORT,
                    database=cls._DATABASE
                )
                log.debug(f'Conexion exitosa {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener la conexion{e}')
                sys.exit()
        else:
            return cls._conexion;
    
    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                lob.error(f'Ocurrio una excepcion al obtener el cursor{e}')
                sys.exit()
        else:
            return cls._cursor;
if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()