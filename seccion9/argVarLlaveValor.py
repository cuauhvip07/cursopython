
def listarTerminos(**terminos): # El doble asterisco es para mandar diccionarios
    for llave,valor in terminos.items():
        print(f'{llave}: {valor}')
        
listarTerminos(IDE='Integrated Develoment Envioronmet', PK = 'Primary Key')