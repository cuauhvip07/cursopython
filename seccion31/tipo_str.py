# Profundizando en el tipo str
import math
from mi_clase import Miclase

# Concatenacion automatica en python
mensaje = 'Hola'  'Mundo'
# print(mensaje)
mensaje += 'Claro' 'aqui'
# print(mensaje)

# Solicitar ayuda
help(str.center) #El segundo es el modulo que quieres saber como se ocupa
help(math)
help(Miclase) # Llama la documentacion de la clase
print(Miclase.__doc__)
print(Miclase.__init__.__doc__)
print(Miclase.mi_metodo().__doc__)