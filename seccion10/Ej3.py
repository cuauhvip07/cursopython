"""
Crear la clase de cubo para definir el atributo de ancho,alto y profundidad y un metodo llamado calcularVolumen y se multiplican los tres valores. Se debe de porporcionar el resultado del volumen de la figura
"""

class Cubo:
    def __init__(self,ancho,alto,profundidad):
        self.ancho = ancho;
        self.alto = alto;
        self.profundidad = profundidad;
        
    def calcularVolumen(self):
        return self.ancho * self.alto * self.profundidad;
    

ancho = float(input('Proporcione el ancho: '))
alto = float(input('Proporcione el alto: '))
profundidad = float(input('Proporcione la profundidad: '))

cubo1 = Cubo(ancho,alto,profundidad)
print(f'Volumen cubo: {cubo1.calcularVolumen()}')