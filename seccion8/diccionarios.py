# diccionario (key,value)

diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}


print(len(diccionario))

print(diccionario['IDE']) # Acceder el valor con la llave
print(diccionario.get('OOP')) #Otra forma de recuperar el elemento

diccionario['IDE'] = 'integrated development environment' # Modificar un elemento
print(diccionario)


#Reccorrer los elementos de un dicionario

for termino in diccionario:
    print(termino) # Imprime la llave
    
for termino in diccionario.items(): #Imprime llave y valor
    print(termino) 

for termino in diccionario.keys(): #Imprime llave 
    print(termino)

for termino in diccionario.values(): #Imprime los valores
    print(termino) 



print('IDE' in diccionario) # Comprobar existencia de algun elemento

diccionario['PK'] = 'Primary Key'# Agregar un elemento

diccionario.pop('DBMS') # Remover un elemento

diccionario.clear() # Limpiar el diccionario 

del diccionario
print(diccionario) # Eliminar el diccionario

