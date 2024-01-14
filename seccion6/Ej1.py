# Dependiendo el mes saber que estacion del año estamos 

mes = int(input('Proporcione mes del año (1-12): '));
estacion = None;

if(mes == 12 or 1 <= mes <= 3 ):
    estacion = 'Invierno';
elif(4 <= mes <= 6):
    estacion = 'Primavera';
elif(7 <= mes <= 9):
    estacion = 'Verano';
elif(10 <= mes <= 11):
    estacion = 'Otoño';
else:
    print('Error. Ingrese un valor valido entre 1 y 12');
    mes = 'Mes incorrecto'

print(f'Para el mes {mes} la estacion es: {estacion}')