from DispositivoEntrada import DispositivoEntrada;

class Raton(DispositivoEntrada):
    contadorId = 0;
    
    @classmethod
    def nuevoId(cls):
        cls.contadorId += 1;
        return cls.contadorId;
    
    def __init__(self,tipoEntrada,marca):
        self._idRaton = Raton.nuevoId();
        DispositivoEntrada.__init__(self,tipoEntrada,marca);
        
    def __str__(self):
        return f'Id {self._idRaton}, Marca: {self.marca}, Tipo de entrada: {self.tipoEntrada}'

if __name__ == '__main__':
    
    raton1 = Raton('USB','Mac')
    raton2 = Raton('Bluetooth','Mac2')
    print(raton1)
    print(raton2)