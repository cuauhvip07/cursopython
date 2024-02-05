from loggin import log
from Conexion import Conexion

class CursorPool:
    def __init__(self):
        self._conn = None;
        self._cursor = None;
        
    def __enter__(self):
        self._conn = Conexion.obtenerConexion()
        self._cursor = self._conn.cursor()
        return self._cursor
        
    def __exit__(self,tipoExcepcion,valorExcepcion,detalleExcepcion):
        if valorExcepcion:
            self._conn.rollback()
        else:
            self._conn.commit()
        self._cursor.close()
        Conexion.liberarConexion(self._conn)
        
        
if __name__ == '__main__':
    with CursorPool() as cursor:
        cursor.execute('SELECT * FROM usuario');
        log.debug(cursor.fetchall())