import psycopg2

# Conexion de la base de datos
conexion = psycopg2.connect(
    user='postgres',
    password='root',
    host='localhost',
    port='5432',
    database='test_db'
    )
#print(conexion)

try:
    with conexion:
        #cursor -> Objeto permite ejecutar secuencias SQL
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
            valores = (
                ('Angel','Quintana','aquintana@mail.com'),
                ('Marcos','Cantu','ccantu@mail.com'),
                ('Maria','Gonzales','mgonzales@mail.com')
                )
            # cursor.execute(sentencia,valores) #Agregar UN registro
            cursor.executemany(sentencia,valores)
            #conexionn.commit() # Guarda los cambios en la BD no es necesario por el with
            registrosInsertados = cursor.rowcount
            print(f'Registros insertados: {registrosInsertados}')
except Exception as e:
    print(e)
finally:
    conexion.close()


