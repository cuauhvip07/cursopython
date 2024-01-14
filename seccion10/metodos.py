class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre;
        self.apellido = apellido;
        self.edad = edad;
        
    def mostrarInfo(self):
        print(f'Su nombre es: {self.nombre} {self.apellido} y tiene {self.edad} años')
        
persona1 = Persona('Cuauhtemoc','Villalba',21)
persona1.mostrarInfo();

persona2 = Persona('Carlos','Gomez',21)
persona2.mostrarInfo()

class Fruta:
    def __init__(this,nombre,precio,peso): # En lugar de self se puede usar this u otra variable
        this.nombre = nombre;
        this.precio = precio;
        this.peso = peso;
    
    def infoFruta(this):
        print(f'La fruta {this.nombre} tiene un precio de ${this.precio} y pesa {this.peso}');


fruta1 = Fruta('Manzana',50,'20Kg')
fruta1.infoFruta();

fruta1.caducidad = '20 Dias' # Se pueden crear atributos que no se comparten con otros objetos
print(fruta1.caducidad)

fruta2 = Fruta('Pera',10,'1 KG');
fruta2.infoFruta()
# En fruta2 no se puede mandar a llamara fruta2.caducidad ya que solo existe en fruta1