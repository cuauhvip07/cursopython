from Empleado import Empleado
from Gerente import Gerente

def imprimirDetalles(objeto):
    print(objeto);
    print(type(objeto));
    if isinstance(objeto, Gerente): # Si existe esa instancia
        print(objeto.departamento);
    
empleado1 = Empleado('Carlos',5000)
imprimirDetalles(empleado1)

gerente1 = Gerente('Juan',3000,'Sistemas');
imprimirDetalles(gerente1)