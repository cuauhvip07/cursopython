class Persona:
    def __init__(self,nombre,apellido,edad):
        self._nombre = nombre # Con _ significa no modificar los valores
        self.apellido = apellido
        self.edad = edad
    
    @property # Ayuda a que no pongamos el parentesis a la hora de mandarlo a llamar    Metodo get
    def nombre(self):
        return self._nombre
    
    # @nombre.setter # Ayuda a no poner el parentesis. Se debe poner el nombre y despues setter   Metodo set
    # def nombre(self,nombre):
    #     self._nombre = nombre     Asi se hace que solo sea de lectura y no se pueda modificar
    
    
    def mostrarDetalles(self):
        print(f'Nombre: {self._nombre} {self.apellido} y edad {self.edad}')


persona1 = Persona('Juan','Perez',20)
print(persona1.nombre) # Mandar de manera indirecta el nombre (No se usa parentesis)
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)