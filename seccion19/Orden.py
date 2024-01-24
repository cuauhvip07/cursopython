

class Orden:
    contadorId = 0;
    
    @classmethod
    def ordenId(cls):
        cls.contadorId += 1;
        return cls.contadorId 
    
    def __init__(self,computadoras):
        self._idOrden = Orden.ordenId();
        self._computadoras = list(computadoras)
        
    def agregarComputadora(self,compu):
        self._computadoras.append(compu);
        
    def __str__(self):
        computadorasStr = '';
        for computadora in self._computadoras:
            computadorasStr += computadora.__str__()
        
        return f'''
        Orden: {self._idOrden}
        Computadoras: {computadorasStr}
    '''