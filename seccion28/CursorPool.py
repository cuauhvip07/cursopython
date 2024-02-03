from loggin import log
from Conexion import Conexion;

class CursorPool:
    def __init__(self):
        self._conexion = None;
        self._cursor = None;
        
    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor;
    
    def __exit__(self,tipoExepcion,valorException,detalleExcepcion):
        log.debug('Se ejecute metodo __exit__')
        if valorException:
            self._conexion.rollback()
            log.error(f'Ocurrio una excepcion {valorException} {valorException} {detalleExcepcion}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')
        self._cursor.close()
        Conexion.liberarconexion(self._conexion)
        
if __name__ == '__main__':
    with CursorPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())