class Persona(object): # no es necesario el object
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
        
    def __str__(self): # Se llama de manera automatica
        return f'[Persona: {self._nombre}, Edad: {self._edad}]'


class Empleado(Persona): # Se pone el padre y para poner mas padres se separan con ,
    def __init__(self,nombre,edad,sueldo): # Se ponen las variables del padre
        super().__init__(nombre,edad) # Mandar a llamar el constructor del padre
        self._sueldo = sueldo
    
    @property
    def sueldo(self):
        return self._sueldo;
    
    @sueldo.setter
    def sueldo(self,sueldo):
        self._sueldo = sueldo
        
    def __str__(self):
        return f'Empleado: sueldo: {self._sueldo} {super().__str__()} ' # Se ocupa el str del padre



