from FiguraGeometrica import FiguraGeometrica;
from color import Color

class Rectangulo(FiguraGeometrica,Color):
    def __init__(self,alto,ancho,color):
        FiguraGeometrica.__init__(self,alto,ancho);
        Color.__init__(self,color);
        
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}. El area es: {self.alto * self.ancho}';
    

