# Metodo split -> Crea una lista

cursos = 'Java, JavaScript python'
listaCursos = cursos.split()
print(listaCursos)

cursosComa = 'Java,JavaScript,Python'
listaCursos2 = cursosComa.split(',')
print(listaCursos2)

cursosComa = 'Java,JavaScript,Python'
listaCursos2 = cursosComa.split(',', 1) # Solamente una coma sera separado
print(listaCursos2)