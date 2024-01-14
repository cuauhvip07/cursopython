# Ejercicio: Calculadora de impuestos.
# Crar una funcion para calcular el total de un pago incluyendo un impuesto aplicado. 
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto + (impuesto/100)

def calcImpuestos(monto,iva):
    
    total = monto + monto * (iva / 100);
    print(f'Pago con impuesto ${total}');

monto = float(input('Proporcione el pago sin impuestos: '))
iva = int(input('Proporcione el monto del impuesto: '))

calcImpuestos(monto,iva);