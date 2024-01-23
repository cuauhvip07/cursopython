from Producto import Producto
from Orden import Orden

producto1 = Producto('Jitomate',20);
producto2 = Producto('Papaya',22);
producto3 = Producto('Jicama',30);
producto4 = Producto('Sandia',32);
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
orden2 = Orden(productos2)
print(orden1)
print(orden2)
print(f'Total de la orden 1: {orden1.calcular_total()}')
print(f'Total de la orden 2: {orden2.calcular_total()}')