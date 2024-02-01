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
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id\'s a eliminar (separados por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            cursor.execute(sentencia,llaves_primarias)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print(e)
finally:
    conexion.close()


