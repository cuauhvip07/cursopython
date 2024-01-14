# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas. Puede ser cualquier valor positivo 

def numerosDescendentes(numero):
    if(numero >= 1):
        print(numero)
        numerosDescendentes(numero - 1)

numerosDescendentes(5);
