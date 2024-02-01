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
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            # id_persona = input('Ingrese el valor de id_persona: ')
            # llaves_primarias = ((1,2,3),) # Ejemplo con codigo duro
            entrada = input('Proporciona los id\'s a buscar (separado por comas):' )
            llaves_primarias = (tuple(entrada.split(',')),) # Quita las comas y regresa solo numeros
            cursor.execute(sentencia,llaves_primarias)
            # registros = cursor.fetchall()  # Solicitar todos los registros
            registros = cursor.fetchall() # Regresa un registro
            for registro in registros:
                print(registro)
except Exception as e:
    print(e)
finally:
    conexion.close()


