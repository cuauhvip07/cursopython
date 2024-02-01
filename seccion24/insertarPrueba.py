import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='root',
    host='localhost',
    port='5432',
    database='test_db'
)
opcion = None
while opcion != 1:
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
                nombre = input('Ingrese su nombre: ')
                apellido = input('Ingrese su apellido: ')
                email = input('Ingrese su email: ')
                valores = (nombre,apellido,email)
                cursor.execute(sentencia,valores)
                registrosInsertados = cursor.rowcount
                print(f'Registros insertados: {registrosInsertados}')
                opcion = int(input('Si desea agregar un nuevo registro ingrese 0 de lo contrario 1: '))
    except Exception as e:
        print(e)
        opcion = None
else:
    conexion.close()