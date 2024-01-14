# Set
#Los sets no mantinen un orden
# No puedes guardar datos duplicados 
# No puedes modificar los elementos que hay en un set
# Puedes agregar mas elementos o eliminarlos

planetas = {'mercurio', 'tierra', 'saturno'}


print(len(planetas))
print('mercurio' in planetas) #Conocer si un valor esta en el set
planetas.add('Urano')
planetas.remove('mercurio') # Arroja un error si no lo encunetra
planetas.discard('tierra') # No arroja un error
planetas.clear() # Limpiar el set
del planetas # Eliminar el set
print(planetas)