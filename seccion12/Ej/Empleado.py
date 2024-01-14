from Persona import *;

class Empleado(Persona):
    def __init__(self,nombre,edad,ocupacion):
        Persona.__init__(self,nombre,edad)
        self._ocupacion = ocupacion;
        
    @property
    def ocupacion(self):
        return self._ocupacion

    @ocupacion.setter
    def ocupacion(self,ocupacion):
        self._ocupacion = ocupacion
        
    def __str__(self):
        return (f'{self.nombre} trabaja en {self.ocupacion} {Persona.__str__(self)}')
        
