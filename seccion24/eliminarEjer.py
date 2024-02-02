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
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            valores = input('Ingrese los id\'s a eliminar (separelos con comas): ')
            llaves_primarias = (tuple(valores.split(',')),)
            cursor.execute(sentencia,llaves_primarias)
            registros_eliminados = cursor.rowcount
            print(f'Numero de elementos eliminados: {registros_eliminados}')
except Exception as e:
    print(e)
finally:
    conexion.close()