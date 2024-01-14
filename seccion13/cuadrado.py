from herenciaMultiple import FiguraGeometrica;
from color import Color;

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado) # Manera mas generica
        Color.__init__(self,color) # Manera mas generica
        
    def calcularArea(self):
        return self.alto * self.ancho