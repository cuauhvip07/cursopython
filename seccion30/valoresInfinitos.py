import math 
from decimal import Decimal

# Menejo de valores infinitos
# Infinito Positivo
infinitoPositivo = float('inf') # Asignando valor infinito
print(f'Es infinito: {math.isinf(infinitoPositivo)}') # Saber si es infinito

# Infinito Negativo 

infinitoNegativo = float('-inf')
print(f'Es infinito: {math.isinf(infinitoNegativo)}')


# Utilizando la libreria math
infinitoPo = math.inf
print(f'Es infinito: {math.isinf(infinitoPo)}')

infinitoNeg = -math.inf
print(f'Es infinito: {math.isinf(infinitoNeg)}')


# Utilizando libreria decimal

infinitoPosi = Decimal('Infinity')
print(f'Es infinito: {math.isinf(infinitoPosi)}')

infinitoNega = Decimal('-Infinity')
print(f'Es infinito: {math.isinf(infinitoNega)}')