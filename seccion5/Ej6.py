#Tienda de libros 
# El usuario debe de proporcionar el nombre del libro, el Id del libro, el precio, e indicar si el envio es gratuito y al ultimo desplegar la informacion del libro

nombreLi = input('Nombre del libro: ')
idLi = int(input('Id del libro: '))
precioLi = float(input('Precio del libro $'))
envioLi = input('¿El envio del libro es gratuito? (True / False): ')

if(envioLi == 'True'):
    envioLi = 'El envio del libro es gratuito'
elif(envioLi == 'False'):
    envioLi = 'El envio del libro NO es gratuito'
else:
    envioLi = 'Valor incorrecto, debe de escribir True o False'

print(f'Titulo libro: {nombreLi} \nId del libro: {idLi} \nPrecio del libro ${precioLi} \nEnvio del libro {envioLi}')