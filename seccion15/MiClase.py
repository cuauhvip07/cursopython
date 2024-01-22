

class MiClase:
    # Los valores de clase son globales
    variable_clase = 'Valor variable clase';
    
    # Los valores de instancia solamente se ocuopan en la clase
    def __init__(self,variableInstancia):
        self.variableInstancia = variableInstancia


# Accediendo al valor de clase
print(MiClase.variable_clase)


MiClase.variable_clase2 = 'Valor variable clase 2';
print(MiClase.variable_clase2)

# Accediendo al valor de instancia
miClase = MiClase('Valor variable instancia');
print(miClase.variableInstancia)
print(miClase.variable_clase) # Tambien desde el objeto se puede recuperar la variable de clase