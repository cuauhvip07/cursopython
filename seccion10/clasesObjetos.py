class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona('Cuauhtemoc','Villalba',21)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Juan','Perez',24)
print(f'El ojeto se llama: {persona2.nombre} {persona2.apellido} y su edad es de: {persona2.edad} años')

class Carro:
    def __init__(self,nombre,marca,precio):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio

carro1 = Carro('Camaro','Chevrolet',12000)
print(f'El carro1 {carro1.nombre} de la marca {carro1.marca} tiene un precio de ${carro1.precio}')

carro2 = Carro('AX23','Lambo',2314134)
print(f'El carro2 {carro2.nombre} de la marca {carro2.marca} tiene un precio de ${carro2.precio}')

#Modificar los elementos (Tambien se puede usando encapsulamiento)
carro2.nombre = 'AZ12'
carro2.precio = 438739

print(f'El carro2 {carro2.nombre} de la marca {carro2.marca} tiene un precio de ${carro2.precio}')


