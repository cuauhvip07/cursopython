from UsuarioDao import UsuarioDao as usr;
from Usuario import Usuario;

    
opcion = None;

while opcion != 5:
    try:
        print('Binevenido al menu')
        print('1.-Listar Usuario')
        print('2.-Agregar Usuario')
        print('3.-Actualizar Usuario')
        print('4.-Eliminar Usuario')
        print('5.-Salir')
        opcion = int(input('Seleccione un opcion (1-5): '))
    except Exception as e:
        print(f'Error, seleccion un valor valido {e}')
        
    if opcion == 1:
        print('Mostrando lista de usuarios'.center(10,'*'))
        persona1 = usr.seleccionar()
        for persona in persona1:
            print(persona)
    
    elif opcion == 2:
        print('Ingrese los datos para añadir')
        nombre = input('Nombre: ')
        password = input('Password: ')
        persona1 = Usuario(nombre=nombre,password=password)
        usr.insertar(persona1)
        print('Usuario añadido con exito')
        
    elif opcion == 3:
        print('Ingrese los datos para actualizar')
        nombre = input('Nombre: ')
        password = input('Password: ')
        idUsuario = input('Id del usuario: ')
        persona1 = Usuario(nombre=nombre,password=password,idUsuario=idUsuario)
        usr.actualizar(persona1)
        print('Usuario actualizado con exito')
    
    elif opcion == 4:
        print('Ingrese los datos para eliminar registro')
        idUsuario = input('Id del usuario: ')
        persona1 = Usuario(idUsuario=idUsuario)
        usr.eliminar(persona1)
        print('Usuario eliminado con exito')