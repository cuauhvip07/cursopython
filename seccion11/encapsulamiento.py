class Persona:
    def __init__(self,nombre,apellido,edad):
        self._nombre = nombre # Con _ significa no modificar los valores  Esto es encapsulamiento
        self.apellido = apellido
        self.edad = edad
        
    def mostrarDetalles(self):
        print(f'Nombre: {self._nombre} {self.apellido} y edad {self.edad}')


persona1 = Persona('Juan','Perez',20)
persona1._nombre = 'Carlos' # El _ Significa que no cambies de esta manera el codigo
persona1.mostrarDetalles()