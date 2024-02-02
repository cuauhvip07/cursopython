import psycopg2;

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
                sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona = %s'
                nombre = input('Ingrese nombre: ')
                apellido = input('Ingrese apellido: ')
                email = input('Ingrese nuevo correo: ')
                num = input('Ingrese id: ')
                actualizar = (nombre,apellido,email,num)
                cursor.execute(sentencia,actualizar)
                info = cursor.rowcount
                print(f'Se actulizaron: {info}')
                opcion = int(input('Si desea actualzar uno nuevo presione 0, de lo contrario 1: '))
        
    except Exception as e:
        print(e)
        opcion = None
else:
    conexion.close()