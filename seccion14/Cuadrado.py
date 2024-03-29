from FiguraGeometrica import FiguraGeometrica;
from Color import Color

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado);
        Color.__init__(self,color);
        
    def calcularArea(self):
        return f'El area es: {self.alto * self.ancho}'
        
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'