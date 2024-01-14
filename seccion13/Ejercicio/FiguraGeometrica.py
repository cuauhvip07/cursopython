class FiguraGeometrica:
    def __init__(self,alto,ancho):
        if(self._validaValor(alto)):
            self._alto = alto;
        else:
            self._alto = 0;
            print('Los valores deben de ser positivos')
        if(self._validaValor(ancho)):
            self._ancho = ancho;
        else:
            self._ancho = 0
            print('Los valores deben de ser positivos')
        
    @property 
    def alto(self):
        return self._alto;
    
    @property
    def ancho(self):
        return self._ancho;
    
    @alto.setter
    def alto(self,alto):
        self._alto = alto;
        
    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho;
        
    def __str__(self):
        return f'El alto es: {self.alto} y el ancho es: {self.ancho}';
    
    def _validaValor(self,valor):
        return True if valor > 0 else False