from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas as cp;

opcion = None;

while opcion != 4:
    try:
        print('Menu')
        print('1. Agregar una pelicula')
        print('2. Listar Peliculas')
        print('3. Eliminar archivo de Peliculas')
        print('4. Salir')
        opcion = int(input('Ingrese una opcion: '))
        
        if opcion == 1:
            nombre = input('Nombre de la pelicula: ')
            pelicula = Pelicula(nombre)
            cp.agregar_peliculas(pelicula)
            
        elif opcion == 2:
            cp.listar_peliculas()
            
        elif opcion == 3:
            cp.eliminar()
    except Exception as e:
        print(e)
        opcion = None
else:
    print('Fin del programa')