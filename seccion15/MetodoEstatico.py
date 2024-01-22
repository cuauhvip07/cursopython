

class MiClase:
    # Los valores de clase son globales
    variable_clase = 'Valor variable clase';
    
    # Los valores de instancia solamente se ocuopan en la clase
    def __init__(self,variableInstancia):
        self.variableInstancia = variableInstancia
    
    @staticmethod # No recibe un contexto de clase 
    def metodoEstatico():
        print(MiClase.variable_clase)

MiClase.metodoEstatico()