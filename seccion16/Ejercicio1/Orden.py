from Producto import Producto

class Orden:
    
    contadorId = 0;
    
    @classmethod
    def contadorIds(cls):
        cls.contadorId += 1;
        return cls.contadorId;
    
    def __init__(self,productos):
        self.idOrden = Orden.contadorIds()
        self._productos = productos;
        
    @property
    def productos(self):
        return self._productos
    @productos.setter
    def productos(self,productos):
        self._productos = productos;
        
    def precioTotal(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total
        
    def __str__(self):
        infoProductos = '';
        for producto in self.productos:
            infoProductos += producto.__str__() + '|';
        return f'Orden: {self.idOrden}, \nProductos:{infoProductos}'
    

producto1 = Producto('Jitomate',20);
producto2 = Producto('Papaya',22);
producto3 = Producto('Melon',25);
producto4 = Producto('Uva',30);
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
orden2 = Orden(productos2)
print(orden1)
print(orden2)
print(orden1.precioTotal())
print(orden2.precioTotal())