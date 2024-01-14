from FiguraGeometrica import FiguraGeometrica;
from color import Color;

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado);
        Color.__init__(self,color);
        
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}. El area del cuadrado es: {self.alto * self.ancho}'
    

