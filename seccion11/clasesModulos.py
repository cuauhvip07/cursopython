from encapGeneral import Fruta;

print('Creacion objetos'.center(50,'-'))
fruta2 = Fruta('Manzana','Rojo',30);
fruta2.mostrarDetalles()

print('Eliminacion de objetos'.center(50,'-'))
del fruta2

print(__name__)