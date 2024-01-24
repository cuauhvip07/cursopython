from Monitor import Monitor
from Raton import Raton;
from Teclado import Teclado;

class Computadora(Monitor,Raton,Teclado):
    
    contadorId = 0;
    @classmethod
    def compuId(cls):
        cls.contadorId += 1;
        return cls.contadorId;
    
    def __init__(self,nombre,monitor,teclado,raton):
        self._idComputadora = Computadora.compuId();
        self._nombre = nombre;
        self._monitor = monitor;
        self._teclado = teclado;
        self._raton = raton;
        
    def __str__(self):
        return f'''
    {self._nombre}: {self._idComputadora}
    Monitor: {self._monitor}
    Teclado: {self._teclado}
    Raton: {self._raton}
    '''

if __name__ == '__main__':
    teclado1 = Teclado('USB','Apple');
    raton1 = Raton('Cable','HP');
    monitor1 = Monitor('Linux','20"');
    computadora1 = Computadora('Mac',monitor1,teclado1,raton1)
    print(computadora1)