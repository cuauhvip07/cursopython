
try:
    archivo = open('/Users/cuauhtemoc_villalba/Desktop/Udemy/cursopython/seccion22/archivo.txt','w',encoding='utf8');

    archivo.write('Hola\n')
    archivo.write('Esta es otra info');
except Exception as e:
    print(e);
finally:
    archivo.close();