import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='root',
    host='localhost',
    port='5432',
    database='test_db'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            valores = input('Ingrese los id\'s (separelos por comas): ')
            llaves_primarias = (tuple(valores.split(',')),)
            cursor.execute(sentencia,llaves_primarias)
            datos = cursor.fetchall()
            for dato in datos:
                print(dato)
except Exception as e:
    print(e)
finally:
    conexion.close()