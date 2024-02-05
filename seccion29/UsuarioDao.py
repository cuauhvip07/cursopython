from loggin import log
from CursorPool import CursorPool;
from Usuario import Usuario;

class UsuarioDao:
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY idusuario'
    _INSERTAR = 'INSERT INTO usuario(username,password) VALUES (%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE idusuario = %s'
    _DELETE = 'DELETE FROM usuario WHERE idusuario=%s'
    
    @classmethod
    def seleccionar(cls):
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR);
            valor = cursor.fetchall()
            valores = []
            for value in valor:
                usuario = Usuario(value[0],value[1],value[2])
                valores.append(usuario)
            return valores
    
    @classmethod
    def insertar(cls,usuario):
        with CursorPool() as cursor:
            valores = (usuario.nombre,usuario.password)
            cursor.execute(cls._INSERTAR,valores)
    
    @classmethod
    def actualizar(cls,usuario):
        with CursorPool() as cursor:
            valores = (usuario.nombre,usuario.password,usuario.idUsuario)
            cursor.execute(cls._ACTUALIZAR,valores)
            
    @classmethod
    def eliminar(cls,usuario):
        with CursorPool() as cursor:
            valor = (usuario.idUsuario,)
            cursor.execute(cls._DELETE,valor)
            
if __name__ == '__main__':
    
    # # Eliminar
    # usuario3 = Usuario(idUsuario=1)
    # UsuarioDao.eliminar(usuario3)
    
    # # Actualizar
    # usuario2 = Usuario(nombre='Pepe',password='678',idUsuario='2')
    # UsuarioDao.actualizar(usuario2)
    
    # # Insertar
    # usuario1 = Usuario(nombre='Claudia',password='456')
    # UsuarioDao.insertar(usuario1)
    
    
    # Seleccionar
    persona1 = UsuarioDao.seleccionar()
    for persona in persona1:
        print(persona)