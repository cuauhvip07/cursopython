# En el siguiente ejercicio se solicita calcular el area y el perimetro de un rectangulo

alto = float(input("Proporcione el alto del rectangulo: "))
ancho = float(input("Proporcione el ancho del rectangulo: "))

area = alto * ancho
perimetro = (alto*2) + (ancho*2)

print(f'Area: {area}\nPerimetro: {perimetro}');