import psycopg2 as bd

conexion = bd.connect(
    user='postgres',
    password='root',
    host='localhost',
    port='5432',
    database='test_db'
)
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
            valores = ('Juan','Asmo','jasmo@mail.com')
            cursor.execute(sentencia,valores)
            registrosInsertados = cursor.rowcount
            
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan Carlos','Juarez','jcjuarez@mail.com',1)
            cursor.execute(sentencia,valores)
except Exception as e:
    print(e)
    opcion = None
finally:
    conexion.close()

print('Se hizo commit')