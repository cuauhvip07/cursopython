from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5,'Rojo')
print(cuadrado1.calcularArea())
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)

# MRO - Method Resolution Order
# Da el orden de busqueda en como se esta ejecutando el codigo
print(Cuadrado.mro())