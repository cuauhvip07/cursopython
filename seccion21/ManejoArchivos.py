
# w = Writte -> Escribir
# r = Read -> Lee archivos. Abre archivos, error si no lo encuentra
# a = Append -> Abre archivos para unir, crea uno si no existe
# x = Create -> Crea un archivo especifico, error si existe
# b = Binary -> Modo binario Ejemplo. Imagenes

try:
    # Open -> Abrir el archivo ya existente o se crea automaticamente
    archivo = open('/Users/cuauhtemoc_villalba/Desktop/Udemy/cursopython/seccion21/Prueba.txt','w',encoding='utf8'); # Usar asentos
    # write -> Agregar informacion al archivo
    archivo.write('Agregando información\n')
    archivo.write('Cuauhtémoc Villalba\n')
    archivo.write('28-01-2024')
except Exception as e:
    print(e);
finally:
    archivo.close();
    print('Archivo cerrado')