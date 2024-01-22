
class Producto:
    idProducto = 0;
    
    @classmethod
    def nuevoProducto(cls):
        cls.idProducto += 1; # Se añade el nuevo id
        return cls.idProducto; # Se retorna el valor
    
    def __init__(self,nombre,peso):
        self.numProducto = Producto.nuevoProducto();
        self.nombre = nombre;
        self.peso = peso;
        
    def __str__(self):
        return f'Producto: [{self.numProducto},{self.nombre},{self.peso}]'
    
producto1 = Producto('Jitomate','3kg')
producto2 = Producto('Tomate','1kg')
print(producto1)
print(producto2)
print(f'Total de productos: {Producto.idProducto}')
