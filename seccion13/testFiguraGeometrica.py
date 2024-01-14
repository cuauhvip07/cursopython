from cuadrado import Cuadrado
from herenciaMultiple import FiguraGeometrica;

cuadrado1 = Cuadrado(5,'Verde')
print(cuadrado1.ancho)
print(cuadrado1.color)
print(cuadrado1.calcularArea())

# MRO - Method Resolution Order   Orden en que se llaman las clases
print(Cuadrado.mro())

# ABC
# No se puede instanciar una clase abstracta
# figura = FiguraGeometrica()