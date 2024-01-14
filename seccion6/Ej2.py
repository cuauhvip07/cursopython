# Dependiendo la edad, tendra la informacion

edad = int(input('Proporcione su edad: '))

if( 0 <= edad <= 10):
    print('La infancia es increible')
elif(11 <= edad <= 20):
    print('Muchos cambios y muchos estudios')
elif(21 <= edad <= 30):
    print('Amor y comienza el trabajo')
else:
    print('Etapa de la vida no reconocida')