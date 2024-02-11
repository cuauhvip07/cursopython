
tuplaStr = ('Hola','Mundo','Aqui')
mensaje = ' '.join(tuplaStr)
print(mensaje)

listaCursos = ['Python','JavaScript','CSS']
mensaje2 = ', '.join(listaCursos)
print(mensaje2)

# Solo se deben de usar cadenas
diccionario = {'nombre':'Juan','apellido':'Perez'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'Llaves: {llaves}, type: {type(llaves)}')
print(f'Valores: {valores}, type: {type(valores)}')