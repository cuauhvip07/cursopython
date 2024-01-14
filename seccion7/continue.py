# Continue hace que ejecute las siguientes lineas que siguen.
i = 0
for i in range(6):
    if(i % 2 != 0):
        continue
    print(f'Valor {i}')