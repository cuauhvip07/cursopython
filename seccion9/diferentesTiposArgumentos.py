def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres = ['Juan','Karla','Gomez']
desplegarNombres(nombres) # En modo de arreglo
desplegarNombres('Cuauh') # En modo de string
desplegarNombres((10,12)) # En modo de tupla