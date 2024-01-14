#ABC = Abstract Base Class 

from abc import ABC, abstractclassmethod;

class FiguraGeometrica(ABC):
    def __init__(self,ancho,alto):
        self._ancho = ancho;
        self._alto = alto;

    @property
    def ancho(self):
        return self._ancho;
    
    @property 
    def alto(self):
        return self._alto;
    
    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho;
    
    @alto.setter
    def alto(self,alto):
        self._alto = alto;
        
    @abstractmethod
    def calcular_area(self):
        pass