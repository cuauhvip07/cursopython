# Crear una funcion para multiplicar los valores recibidos de tipo numerico, utilizando argumentos variables *args como parametro de la funcion y regresar como resultado la multiplicacion de todos los valores pasados como argumentos

def multiplicacion(*numeros):
    total = 1;
    for numero in numeros:
        total *= numero;
    print(f'El resultado de las multiplicaciones es: {total}')


multiplicacion(10,10,20,2)