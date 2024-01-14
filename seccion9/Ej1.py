
# Crear una funcion  para sumar los valores recibidos de tipo numerico, utilizando argumentos variables *args como parametro de la funcion y regresar como resultado la suma de todos los valores pasados como argumentos

def suma(*valores):
    total = 0
    for numero in valores:
        total  +=  numero;
    print(f'El total de la suma es: {total}')

suma(1,2,3,4,5,6,7,8,9)
