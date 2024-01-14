class Persona:
    def __init__(self,nombre,apellido,edad,*valores,**terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores;
        self.terminos = terminos;
        
    def mostrarDetalles(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


persona1 = Persona('Juan','Perez',20,'3227834',23,2,1, m = 'manzana', p = 'pera')
persona1.mostrarDetalles()