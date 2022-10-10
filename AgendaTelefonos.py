#Opción 1:
#Lista para nombres
#Lista para telefonos

#Opcion 2
#Lista para nombres y telefonos
#Ejemplo [Juan - Teléfono, Pepe - Teléfono]

#Opción 1:

vNombres = []
vTelefonos = []

Nombre1=input("Dime un nombre:")
Telefono1=int(input("Dime su teléfono:"))

vNombres.append(Nombre1)
vTelefonos.append(Telefono1)

print(vNombres)
print(vTelefonos)

print("El nombre de tu contacto es:", vNombres, "su número es:", vTelefonos)
