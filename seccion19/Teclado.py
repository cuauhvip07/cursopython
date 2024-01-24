from DispositivoEntrada import DispositivoEntrada;

class Teclado(DispositivoEntrada):
    
    sumadorId = 0;
    @classmethod
    def sumId(cls):
        cls.sumadorId += 1;
        return cls.sumadorId;
    
    def __init__(self,tipoEntrada,marca):
        self._idTeclado = Teclado.sumId();
        
        DispositivoEntrada.__init__(self,tipoEntrada,marca);
        
    def __str__(self):
        return f'Id: {self._idTeclado}, Marca: {self.marca}, Tipo de Entrada: {self.tipoEntrada}';
    
if __name__ == '__main__':
    teclado1 = Teclado('USB','Apple')
    teclado2 = Teclado('USB2','Apple2')

    print(teclado1)
    print(teclado2)
