
# Tipos numericos
# Solamente con 0 dara False, los demas daran True

valor = 0 # False
valor = -10 # True
resultado = bool(valor)
# print(resultado)

# str
# False para cadenas '' (Vacias)

valor = '' # False
valor = 'Hola' #True
resultado = bool(valor)
# print(resultado)

# Arrays , diccionarios 
# False -> Arrays,diccionarios vacias

valor = [] #False
valor = ['Hola'] # True
resultado = bool(valor)
print(resultado)

if '':
    print('Regreso verdadero')
else:
    print('Regreso falso')