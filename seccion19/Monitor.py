
class Monitor:
    
    sumadorId = 0;
    @classmethod
    def monitorId(cls):
        cls.sumadorId += 1;
        return cls.sumadorId;
    
    def __init__(self,marca,tamanio):
        self._idMonitor = Monitor.monitorId();
        self._marca = marca;
        self._tamanio = tamanio;
        
    @property 
    def marca(self):
        return self._marca;
    @property 
    def tamanio(self):
        return self._tamanio;
    
    @marca.setter 
    def marca(self,marca):
        self._marca = marca;
    @tamanio.setter
    def tamanio(self,tamanio):
        self._tamanio = tamanio
        
    def __str__(self):
        return f'Id: {self._idMonitor}, Marca: {self.marca}, Tamaño: {self.tamanio}'
        
        
if __name__ == '__main__':
    monitor1 = Monitor('HP','20"');
    monitor2 = Monitor('Linux','22"');
    print(monitor1)
    print(monitor2)