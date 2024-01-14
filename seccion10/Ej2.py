"""
Esta clase va a tener dos atributos (altura y base) y un metodo llamado Calcular Area, donde se va a multiplicar la base por la altura, los valores los da el usuario
"""

class AreaRectangulo:
    def __init__(self,base,altura):
        self.base = base;
        self.altura = altura;
        
    def area(self):
        return self.base * self.altura;


base = float(input('Proporcione la base: '))
altura = float(input('Proporcione la altura: '))

rectangulo1 = AreaRectangulo(base,altura);

print(f'Area del rectangulo: {rectangulo1.area()}')