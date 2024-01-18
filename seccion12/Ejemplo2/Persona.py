class Persona():
    def __init__(self,nombre,edad):
        self._nombre = nombre;
        self._edad = edad;
        
    @property
    def nombre(self):
        return self._nombre;
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre;
        
    @property
    def edad(self):
        return self._edad;
    
    @edad.setter
    def edad(self,edad):
        self._edad = edad;
        
    def __str__(self):
        print(f'{self.nombre} tiene {self.edad} años');

