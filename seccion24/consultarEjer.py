import psycopg2;

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
            sentencia = 'SELECT * FROM persona where id_persona IN %s'
            valor = input('Ingrese los id\'s a buscar (separelos por comas: ')
            llaves_primarias = (tuple(valor.split(',')),)
            cursor.execute(sentencia,llaves_primarias)
            informacion = cursor.fetchall()
            for info in informacion:
                print(info)

except Exception as e:
    print(e)
finally:
    conexion.close()