

class MiClase:
    # Los valores de clase son globales
    variable_clase = 'Valor variable clase';
    
    # Los valores de instancia solamente se ocuopan en la clase
    def __init__(self,variableInstancia):
        self.variableInstancia = variableInstancia
    
    @staticmethod
    def metodoEstatico():
        print(MiClase.variable_clase)
        
    @classmethod # Si recibe un contexto de clase
    def metodoClase(cls):
        print(cls.variable_clase)
        
    def metodo_instancia(self):
        self.metodoClase()
        self.metodoEstatico();
        print(self.variableInstancia);

MiClase.metodoClase()

miObjeto1 = MiClase('Valor de instancia');
miObjeto1.metodoClase();
miObjeto1.metodo_instancia()