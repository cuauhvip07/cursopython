
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre;
        self.edad = edad
        
    def __add__(self,other): # add es es la suma obj1 + obj2
        return self.nombre + other.nombre
    
    def __sub__(self,other): # Resta obj1 - obj2
        return self.edad - other.edad;

persona1 = Persona('Juan',30)
persona2 = Persona('Carlos',10)
print(persona1 + persona2)
print(persona1 - persona2)