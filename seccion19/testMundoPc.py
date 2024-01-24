from Monitor import Monitor
from Raton import Raton;
from Teclado import Teclado;
from Computadora import Computadora;
from Orden import Orden

teclado1 = Teclado('USB','Apple');
raton1 = Raton('Cable','HP');
monitor1 = Monitor('Linux','20"');
computadora1 = Computadora('Mac',monitor1,teclado1,raton1)
print(computadora1)

teclado2 = Teclado('USB','Hp');
raton2 = Raton('USB','Apple');
monitor2 = Monitor('HLde','24"');
computadora2 = Computadora('Windows',monitor2,teclado2,raton2)
print(computadora2)

computadoras1 = [computadora1,computadora2]

orden1 = Orden(computadoras1)
print(orden1)