from NumerosIdenticos import NumerosIdenticosException

resultado = None;
# a = 0; 
# b = 0;
try:
    # Si se declara adentro del try, la variable es local al try y no se puede usar fuera
    a = int(input('Primer numero: '));
    b = int(input('Segundo numero: '));
    
    if a == b:
        # Raise lanzar o arrojar una excepcion 
        # Se puede ocupar creando una clase o sin usar la clase
        
        # raise ValueError('Error de valor')
        raise NumerosIdenticosException('Numeros identicos')
    resultado = a / b ;
except ZeroDivisionError as e:  # excepcion division entre cero
    print(f'Ocurrio un error: {e}, {type(e)}')
except TypeError as e:   # Error string con int
    print(f'Ocurrio un error: {e}, {type(e)}')
except Exception as e:   # Excepcion mas general
    print(f'Ocurrio un error: {e}, {type(e)}')
else: # NO se ejecuta si hay un error
    print('El else es un bloque opcional y se ejecuta solo si no hay un error')
finally: # Haya o no haya error, este bloque se ejecuta
    print('Este bloque siempre se ejecuta: finally')
print(f'Resultado: {resultado}')
print('Continuamos.....')