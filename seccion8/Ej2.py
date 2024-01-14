#Dada lasiguiente tupla
#Crear una lista que solo incluya los numeros menores a 5
listados = []
tupla = (13,1,8,3,2,5,8)


for numero in tupla:
    if (numero < 5):
        listados.append(numero)
print(listados)
print('Fin de los numeros menores a 5')