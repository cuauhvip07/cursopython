from Producto import Producto

class Orden:
    contador_ordenes = 0
    
    @classmethod
    def sumadorOrdenes(cls):
        cls.contador_ordenes += 1;
        return cls.contador_ordenes;
    
    def __init__(self,productos):
        self.idOrden = Orden.sumadorOrdenes();
        self._productos = list(productos)
        
    @property
    def productos(self):
        return self._productos;
    
    @productos.setter
    def productos(self,productos):
        self._productos = productos
        
    def agregar_producto(self,producto):
        self.productos.append(producto)
        
    def calcular_total(self):
        total = 0;
        for producto in self.productos:
            total += producto.precio
        return total;
    
    def __str__(self):
        productos_str = ''
        for producto in self.productos:
            productos_str += producto.__str__() + '|'
            
        return f'Orden: {self.idOrden}, \nProductos: {productos_str}'
    
if __name__ == '__main__':
    producto1 = Producto('Jitomate',20);
    producto2 = Producto('Papaya',22);
    productos1 = [producto1, producto2]
    orden1 = Orden(productos1)
    print(orden1)