nombre = ['Juan','Karla','Ricardo','Maria'];

print(nombre) #Imprimir todos los elementos de la lista
print(nombre[0]) #Imprimir el primero de la lsita
print(nombre[-1]) #Imrpimir el ultimo de la lista

print(nombre[0:2]) #Imprimir elementos de un rango, sin incluir el valor de 2
print(nombre[:3]) # Ir del inicio de la lista hasta el indice 3 sin incluirlo
print(nombre[1:]) #Desde el indice indicado hasta el final

nombre[3] = 'Cuauh' #Cambiar el valor
print(nombre)

for elemento in nombre: #Iterar una lista
    print(elemento);

print(len(nombre)) # Conocer la cantidad de elementos de la lista

nombre.append('Cuauh Guapo') #Agregar un nuevo elemento a la lista

nombre.insert(1,'Ishma') #Insertar un elemento en un indice deseado

nombre.remove('Cuauh Guapo') # Eliminar un elemento

nombre.pop(2) # Remueve el ultimo elemento o puedes poner el indice de cual eliminar


del nombre[0]; #Otra manera de elininar el elemento especificando un indice

nombre.clear() #Elimninar todos los elementos de la lista

del nombre #Elimina por completo de la memoria el arreglo
print(nombre)

