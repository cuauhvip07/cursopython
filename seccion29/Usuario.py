from loggin import log

class Usuario:
    def __init__(self,idUsuario=None,nombre=None,password=None):
        self._idUsuario = idUsuario;
        self._nombre = nombre;
        self._password = password;
        
    @property
    def idUsuario(self):
        return self._idUsuario;
    @property
    def nombre(self):
        return self._nombre
    @property
    def password(self):
        return self._password;
    
    @idUsuario.setter
    def idUsuario(self,idUsuario):
        self._idUsuario = idUsuario;
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre;
    @password.setter
    def password(self,password):
        self._password = password;
        
    def __str__(self):
        return f'Id: {self.idUsuario}, Usuario: {self.nombre} Password: {self.password}'
if __name__ == '__main__':
    persona1 = Usuario(1,'Gabriel','231')
    print(persona1)