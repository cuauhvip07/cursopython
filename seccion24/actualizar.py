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
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s'
            valores = (
                ('Juan','Perez','jperez@mail.com',1),
                ('Ivon','Gutierrez','igutierrez@mail.com',2),
                
                )
            # cursor.execute(sentencia,valores) # Actualizar un registro
            cursor.executemany(sentencia,valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros actualizados: {registros_actualizados}')
except Exception as e:
    print(e)
finally:
    conexion.close()


