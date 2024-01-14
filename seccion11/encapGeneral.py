class Fruta:
    def __init__(self,nombre,color,precio):
        self._nombre = nombre;
        self._color = color;
        self._precio = precio;
        
    @property
    def nombre(self):
        return self._nombre;
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre;
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self,color):
        self._color = color
        
    @property
    def precio(self):
        return self._precio;
    
    @precio.setter
    def precio(self,precio):
        self._precio = precio
    
    def mostrarDetalles(self):
        print(f'Fruta {self._nombre}, precio: {self._precio}, color: {self._color}')
        
    def __del__(self): # Usando del podemos ver las frutas que eliminamos
        print(f'Fruta:{self._nombre}, Color: {self._color}, Precio: {self._precio}')

if(__name__ == '__main__'): # Si lo estas ejecutando del archivo base mandara un __main__

    fruta1 = Fruta('Piña','Amarillo',200)
    fruta1.mostrarDetalles()
    fruta1.nombre = 'Melon'
    fruta1.color = 'Cafe claro'
    fruta1.precio = 400
    fruta1.mostrarDetalles()

