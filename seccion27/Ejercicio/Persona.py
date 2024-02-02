

class Persona:
    def __init__(self,idPersona=None,nombre=None,apellido=None,email=None):
        self._idPersona = idPersona;
        self._nombre = nombre;
        self._apellido = apellido;
        self._email = email;
    
    @property
    def idPersona(self):
        return self._idPersona;
    @property 
    def nombre(self):
        return self._nombre;
    @property 
    def apellido(self):
        return self._apellido;
    @property
    def email(self):
        return self._email;
    
    @idPersona.setter
    def idPersona(self,idPersona):
        self._idPersona = idPersona;
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre;
    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido;
    @email.setter
    def email(self,email):
        self._email = email;
        
    def __str__(self):
        return f'''
        Id: {self.idPersona}, Nombre: {self.nombre},
        Apellido: {self.apellido}, Email: {self.email}
        '''
        
if __name__ == '__main__':
    persona1 = Persona(idPersona=1,nombre='Juan',apellido='Lopez',email='jlopez@mail.com')
    print(persona1)