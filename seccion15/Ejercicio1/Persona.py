class Persona:
    contadorPersonas = 0;
    
    @classmethod
    def generarSiguienteValor(cls):
        cls.contadorPersonas += 1
        return cls.contadorPersonas
    
    def __init__(self,nombre,edad):
        self.idPersona = Persona.generarSiguienteValor();
        self.nombre = nombre;
        self.edad = edad;
        
    def __str__(self):
        return f'El id {self.idPersona} es de {self.nombre} y tiene {self.edad} años'
    
persona1 = Persona('Cuauhtemoc',21)
persona2 = Persona('Carlos',22)
print(persona1)
print(persona2)

print(f'Valor contado de personas: {Persona.contadorPersonas}')