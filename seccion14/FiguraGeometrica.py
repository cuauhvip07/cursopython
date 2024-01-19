
class FiguraGeometrica:
    def __init__(self,alto,ancho):
        if self._validarValor(alto) and self._validarValor(ancho):
            self._alto = alto;
            self._ancho = ancho;
        else:
            print('Ingrese valores entre 0 y 10')
            self._alto = 0;
            self._ancho = 0;
        
    @property
    def alto(self):
        return self._alto;
    
    @property
    def ancho(self):
        return self._ancho;
    
    @alto.setter
    def alto(self,alto):
        if self._validarValor(alto):
            self._alto = alto;
        else:
            self._alto = 0;
        
    @ancho.setter
    def ancho(self,ancho):
        if self._validarValor(ancho):
            self._ancho = ancho;
        else:
            self._ancho = 0;
        
    def __str__(self):
        return f'Alto:{self._alto}, Ancho:{self._ancho}';
    
    def _validarValor(self,valor):
        return True if 0 < valor <= 10 else False