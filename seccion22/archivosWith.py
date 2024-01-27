# Primera manera de usar with

# with open('/Users/cuauhtemoc_villalba/Desktop/Udemy/cursopython/seccion22/archivo.txt','r',encoding='utf8') as archivo:

from ManejoArchivos import ManejoArchivos
with ManejoArchivos('/Users/cuauhtemoc_villalba/Desktop/Udemy/cursopython/seccion22/archivo.txt') as archivo:
    print(archivo.read())