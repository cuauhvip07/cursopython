# Ejercicio: Convertidor de temperatura
# Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa 


# Funcion de F a C
def fac(valor1):
    return  5 / 9 * (valor1 - 32 );

farenheit = float(input('Proporcione su valor en Farenheit: '))
# F a C
cel = fac(farenheit)
print(f'De Fahrenheit a Celsius {cel}')


# Funcion de C a F
def caf(valor2):
    return (9 / 5 * valor2) + 32

celsius = float(input('Proporcione su valor en Celsius: '))
# C a F
far = caf(celsius)
print(f'De Celsius a Fahrenheit: {far}')

