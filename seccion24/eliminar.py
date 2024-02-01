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
            sentencia = 'DELETE FROM persona WHERE id_persona = %s'
            valores=(6,)
            cursor.execute(sentencia,valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print(e)
finally:
    conexion.close()


