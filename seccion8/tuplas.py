# No se puede añadir, eliminar o editar
frutas = ('Naranja','Platano','Guayaba');

print(len(frutas))
print(frutas[0])
print(frutas[-1])

for fruta in frutas:
    print(fruta, end= ' '); #el end es para que no tenga salto de lineas
    
frutaLista = list(frutas) #Pasar de una tupla a una lista
frutaLista[0] = 'Pera'
frutas = tuple(frutaLista)
print(frutas)