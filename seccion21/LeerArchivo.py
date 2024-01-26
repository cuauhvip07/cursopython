
archivo = open('/Users/cuauhtemoc_villalba/Desktop/Udemy/cursopython/seccion21/Prueba.txt','r',encoding='utf8')
# print(archivo.read()) # Debe de estar comentado si no da error con el de abajo

# Leer algunos caracteres

# print(archivo.read(5))
# print(archivo.read(2))

# Leer lineas completas

# print(archivo.readline())
# print(archivo.readline())

# Iterar el archivo 
# for linea in archivo:
#     print(linea)

# Leer lineas
# print(archivo.readlines()) # Regresa una lista

# Acceder a una linea de la lista
# print(archivo.readlines()[1]) # Mandar a llamar el indice de la lista

# Copiamos el archivo ya existente
archivo2 = open('/Users/cuauhtemoc_villalba/Desktop/Udemy/cursopython/seccion21/copia.txt','w',encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()