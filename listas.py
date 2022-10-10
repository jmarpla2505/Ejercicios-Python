#Listas en python
#Definición e inicialización
vNombres = []

#Insertar un dato
vNombres.insert(0,"Juan")
vNombres.insert(1,"Pepe")
vNombres.insert(2,"Inés")
vNombres.append("Minerva")
vNombres.insert(1,"Julian")

#Eliminar elementos de la lista

vNombres.remove("Pepe")
print("El nombre borrado es", vNombres.pop(1))

#Ordenar una lista
#Con reverse puedo ordenar en orden inverso
vNombres.sort(reverse=True)

#Contar el número de  elementos de la lista
print(vNombres.count("Inés"))
print("La lista tiene", len(vNombres), "elementos")
print(vNombres)