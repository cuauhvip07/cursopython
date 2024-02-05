from loggin import log
import sys
from psycopg2 import pool

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'root'
    _PORT = '5432'
    _HOST = 'localhost'
    _MINCON = 1
    _MAXCON = 5
    _pool = None;
    
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MINCON,
                    cls._MAXCON,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    host=cls._HOST,
                    port=cls._PORT,
                    database=cls._DATABASE
                )
                return cls._pool
                
            except Exception as e:
                sys.exit()
        
        else:
            return cls._pool;
        
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        return conexion
    
    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        
if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)