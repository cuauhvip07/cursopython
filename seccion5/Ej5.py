#Instrucciones de tareas: 
#Solicitar al usuario dos valores, y determinar cual numero es el mayor

numero1 = float(input('Proporcione el numero1: '))
numero2 = float(input('Proporcione el numero2: '))

if(numero1 > numero2):
    print(f'{numero1} es mas grande')
elif (numero1 < numero2):
    print(f'{numero2} es mas grande')
else:
    print('Los dos numeros son iguales')