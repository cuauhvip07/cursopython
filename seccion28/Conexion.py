from loggin import log
from psycopg2 import pool
import sys

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
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._PORT,
                    database=cls._DATABASE
                    )
                log.debug(f'Creacion del pool exitosa {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool {e}')
                sys.exit()
        else:
            return cls._pool;

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool {conexion}')
        return conexion
    
    @classmethod 
    def liberarconexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: {conexion}')
        
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
    
if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarconexion(conexion1)
    
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    # conexion4 = Conexion.obtenerConexion()
    # conexion5 = Conexion.obtenerConexion()
