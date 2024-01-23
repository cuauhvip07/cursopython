

class Producto:
    
    numProducto = 0;
    @classmethod
    def asignacionPro(cls):
        cls.numProducto += 1;
        return cls.numProducto;
    
    def __init__(self,nombre,precio):
        self.idProducto = Producto.asignacionPro();
        self._nombre = nombre;
        self._precio = precio;
        
    @property
    def nombre(self):
        return self._nombre;
    @property
    def precio(self):
        return self._precio;
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre;
    @precio.setter
    def precio(self,precio):
        self._precio = precio
        
    def __str__(self):
        return f'Id: {self.idProducto}, Nombre: {self.nombre}, Precio: {self.precio}'

if __name__ == '__main__':
    producto1 = Producto('Camisa',20.00);
    producto2 = Producto('Chamarra',30.00);
    print(producto1)
    print(producto2)
