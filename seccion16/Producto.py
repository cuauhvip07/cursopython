

class Producto:
    contador_productos = 0;
    
    @classmethod
    def sumadorProducto(cls):
        cls.contador_productos += 1;
        return cls.contador_productos;
    
    def __init__(self,nombre,precio):
        self.idProducto = Producto.sumadorProducto();
        self._nombre = nombre;
        self._precio = precio
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
        
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self,precio):
        self._precio = precio
        
    def __str__(self):
        return f'Id producto {self.idProducto}, Nombre: {self.nombre}, Precio: ${self.precio}.00'
    
if __name__ == '__main__':
    producto1 = Producto('Jitomate',20);
    producto2 = Producto('Papaya',22);
    print(producto1)
    print(producto2)