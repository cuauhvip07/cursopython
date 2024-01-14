# Instrucciones
#El usuario proporciona un valor entre 0 y 10
# Si esta entre 9 y 10 impirmir una A
# Si esta entre 8 y menor a 9: Imprimir una B
# Si esta entre 7 y menor a 8: Imprimir una C
# Si esta entre 6 y menor a 7: Imprimir una D
# Si esta entre 0 y menor a 6: Imprimir una F
# Cualquier otro valor debe de imprimir: Valor incorrecto 

calificacion = int(input('Proporcione su calificacion: '))

if(9 <= calificacion <=10):
    print('A')
elif( 8 <= calificacion < 9):
    print('B')
elif( 7 <= calificacion < 8):
    print('C')
elif( 6 <= calificacion < 7):
    print('D')
elif( 0 <= calificacion < 6):
    print('F')
else:
    print('Valor incorrecto')